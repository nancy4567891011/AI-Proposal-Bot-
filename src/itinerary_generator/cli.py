"""Command line interface for the travel itinerary generator."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Optional

from .generator import TravelItineraryGenerator
from .renderer import render_itinerary_html


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="travel-itinerary",
        description="生成带有美观样式的旅游定制行程 HTML 方案",
    )
    parser.add_argument("destination", help="目的地名称，例如：东京、云南大理、法国巴黎")
    parser.add_argument("budget", type=float, help="预算金额，默认为总预算")
    parser.add_argument("travellers", type=int, help="出行人数")
    parser.add_argument(
        "--per-person",
        action="store_true",
        help="预算是否为人均预算，启用后将自动乘以人数得到总预算",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="输出 HTML 文件路径；若省略则直接输出到控制台",
    )
    parser.add_argument(
        "--currency-symbol",
        default="¥",
        help="货币符号，默认使用人民币符号 ¥",
    )
    parser.add_argument("--contact-phone", help="联系电话", default=None)
    parser.add_argument("--contact-wechat", help="微信号", default=None)
    parser.add_argument("--contact-email", help="邮箱", default=None)
    parser.add_argument("--contact-company", help="服务机构或公司名称", default=None)
    parser.add_argument("--cta-link", help="立即预订按钮链接", default=None)
    parser.add_argument("--cta-label", help="立即预订按钮文字", default=None)
    return parser


def _contact_kwargs_from_namespace(namespace: argparse.Namespace) -> dict[str, str]:
    mapping = {
        "phone": namespace.contact_phone,
        "wechat": namespace.contact_wechat,
        "email": namespace.contact_email,
        "company": namespace.contact_company,
        "cta_link": namespace.cta_link,
        "cta_label": namespace.cta_label,
    }
    return {key: value for key, value in mapping.items() if value}


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    generator = TravelItineraryGenerator(currency_symbol=args.currency_symbol)
    contact_info = _contact_kwargs_from_namespace(args)

    itinerary = generator.generate_itinerary(
        destination=args.destination,
        budget=args.budget,
        travellers=args.travellers,
        per_person_budget=args.per_person,
        currency_symbol=args.currency_symbol,
        contact_info=contact_info or None,
    )

    html = render_itinerary_html(itinerary)

    if args.output:
        args.output.write_text(html, encoding="utf-8")
        print(f"已生成旅游方案：{args.output}")
    else:
        print(html)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
