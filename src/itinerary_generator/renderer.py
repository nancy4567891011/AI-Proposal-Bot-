"""HTML renderer for the generated itinerary data."""

from __future__ import annotations

from html import escape
from typing import Any, Dict, Iterable


def _safe_url(url: str) -> str:
    return url.replace("'", "%27")


def _format_amount(amount: float, symbol: str) -> str:
    return f"{symbol}{amount:,.0f}" if amount >= 100 else f"{symbol}{amount:,.2f}" if amount % 1 else f"{symbol}{int(amount)}"


def render_itinerary_html(itinerary: Dict[str, Any]) -> str:
    """Render the itinerary dictionary returned by :class:`TravelItineraryGenerator`."""

    budget = itinerary["budget"]
    symbol = budget["currency_symbol"]
    cover = _safe_url(itinerary["cover_image"])
    destination = escape(itinerary["destination"])
    tagline = escape(itinerary.get("tagline", ""))
    country = escape(itinerary.get("country", ""))
    recommended_days = itinerary["recommended_days"]
    group_label = escape(itinerary["group_label"])
    total_budget = budget["total_formatted"]
    per_person_budget = budget["per_person_formatted"]

    parts: list[str] = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html lang=\"zh-CN\">")
    parts.append("<head>")
    parts.append("  <meta charset=\"UTF-8\">")
    parts.append("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
    parts.append(f"  <title>{destination} · 定制行程方案</title>")
    parts.append("  <style>")
    parts.append(
        "    body { font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; margin: 0; background:#f5f7fb; color:#1f2d3d; }"
    )
    parts.append(
        "    header { position: relative; height: 360px; color: white; display:flex; flex-direction:column; justify-content:center; align-items:flex-start; padding:40px; background: linear-gradient(135deg, rgba(0,0,0,.55), rgba(0,0,0,.35)), url('"
        + cover
        + "') no-repeat center/cover; }"
    )
    parts.append("    header h1 { font-size: 2.8rem; margin:0 0 10px; letter-spacing:2px; }")
    parts.append("    header p { font-size: 1.2rem; margin:0; max-width:600px; }")
    parts.append("    main { max-width: 1100px; margin: -60px auto 60px; background:white; border-radius:24px; box-shadow:0 24px 60px rgba(15,41,77,0.16); overflow:hidden; }")
    parts.append("    section { padding: 50px 60px; border-bottom: 1px solid #eef2fb; }")
    parts.append("    section:last-of-type { border-bottom:none; }")
    parts.append("    h2 { font-size: 1.8rem; margin-bottom: 20px; color:#1c4fd1; }")
    parts.append("    .summary { display:flex; flex-direction:column; gap:20px; }")
    parts.append("    .summary-cards { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:18px; }")
    parts.append("    .summary-card { background:#f6f9ff; border-radius:16px; padding:18px; box-shadow: inset 0 0 0 1px rgba(28,79,209,0.08); }")
    parts.append("    .summary-card h3 { margin:0 0 8px; font-size:1.1rem; color:#2648b1; }")
    parts.append("    .summary-card p { margin:0; line-height:1.6; font-size:0.98rem; color:#3a4764; }")
    parts.append("    .day-card { border-radius:18px; padding:24px; margin-bottom:22px; background:linear-gradient(135deg, #f8fbff 0%, #ffffff 100%); box-shadow:0 12px 24px rgba(28,79,209,0.08); }")
    parts.append("    .day-card h3 { margin-top:0; color:#2c3a5f; }")
    parts.append("    .activities { display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin:20px 0; }")
    parts.append("    .activity { background:white; border-radius:14px; box-shadow:0 6px 16px rgba(19,64,116,0.08); overflow:hidden; display:flex; flex-direction:column; }")
    parts.append("    .activity img { width:100%; height:150px; object-fit:cover; }")
    parts.append("    .activity-content { padding:16px; }")
    parts.append("    .activity-content h4 { margin:0 0 8px; font-size:1.05rem; color:#2144a9; }")
    parts.append("    .activity-content p { margin:0; font-size:0.95rem; line-height:1.6; color:#4b5874; }")
    parts.append("    .logistics { display:flex; flex-wrap:wrap; gap:12px; margin-top:12px; }")
    parts.append("    .logistics-item { background:#edf3ff; border-radius:12px; padding:12px 16px; font-size:0.95rem; color:#2d4a9e; }")
    parts.append("    .recommendation-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:18px; }")
    parts.append("    .recommendation-card { border-radius:16px; background:white; box-shadow:0 10px 20px rgba(28,79,209,0.08); overflow:hidden; }")
    parts.append("    .recommendation-card img { width:100%; height:150px; object-fit:cover; }")
    parts.append("    .recommendation-card h4 { margin:0; padding:16px 16px 4px; font-size:1.1rem; color:#2144a9; }")
    parts.append("    .recommendation-card p { margin:0; padding:0 16px 18px; color:#4b5874; line-height:1.6; font-size:0.94rem; }")
    parts.append("    .budget-breakdown { display:grid; gap:12px; margin-top:20px; }")
    parts.append("    .budget-item { background:#f6f9ff; padding:14px 18px; border-radius:14px; box-shadow: inset 0 0 0 1px rgba(28,79,209,0.06); }")
    parts.append("    .budget-label { font-weight:600; color:#2648b1; }")
    parts.append("    .budget-bar { margin-top:10px; height:8px; border-radius:999px; background:rgba(28,79,209,0.12); overflow:hidden; }")
    parts.append("    .budget-bar span { display:block; height:100%; background:linear-gradient(135deg,#3f7dfc,#1c4fd1); }")
    parts.append("    .tips-columns { display:grid; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap:18px; }")
    parts.append("    .tips-columns ul { padding-left:18px; margin:0; }")
    parts.append("    .tips-columns li { margin-bottom:10px; line-height:1.6; color:#415174; }")
    parts.append("    .cta { text-align:center; margin-top:32px; }")
    parts.append("    .cta a { display:inline-block; background:linear-gradient(135deg,#ff8a4c,#ff6a3d); color:white; padding:14px 32px; border-radius:999px; font-size:1.1rem; text-decoration:none; box-shadow:0 12px 24px rgba(255,122,68,0.35); }")
    parts.append("    .contact-info { display:flex; justify-content:center; flex-wrap:wrap; gap:18px; margin-top:18px; font-size:0.96rem; color:#3a4764; }")
    parts.append("    footer { text-align:center; padding:30px; font-size:0.85rem; color:#6b7a99; }")
    parts.append("    @media (max-width: 720px) { header { padding:30px; height:300px; } section { padding: 40px 24px; } main { margin-top:-40px; } }")
    parts.append("  </style>")
    parts.append("</head>")
    parts.append("<body>")
    parts.append("  <header>")
    parts.append(f"    <h1>{destination}定制行程</h1>")
    subtitle_parts = [destination]
    if country:
        subtitle_parts.append(country)
    subtitle = " · ".join(part for part in subtitle_parts if part)
    if tagline:
        parts.append(f"    <p>{subtitle}｜{tagline}</p>")
    else:
        parts.append(f"    <p>{subtitle}</p>")
    parts.append("  </header>")
    parts.append("  <main>")
    parts.append("    <section class=\"summary\">")
    parts.append("      <h2>行程概览</h2>")
    parts.append("      <div class=\"summary-cards\">")
    parts.append(
        "        <div class=\"summary-card\"><h3>预算规划</h3><p>总预算："
        + total_budget
        + "<br>人均预算："
        + per_person_budget
        + "</p></div>"
    )
    parts.append(
        f"        <div class=\"summary-card\"><h3>出行天数</h3><p>建议安排 {recommended_days} 天，行程紧凑而不失悠闲。</p></div>"
    )
    parts.append(
        f"        <div class=\"summary-card\"><h3>适合人群</h3><p>{group_label}</p></div>"
    )
    parts.append(
        f"        <div class=\"summary-card\"><h3>服务亮点</h3><p>{escape('专属顾问全程跟进 · 精选酒店与地道体验')}</p></div>"
    )
    parts.append("      </div>")

    if itinerary["budget_breakdown"]:
        parts.append("      <div class=\"budget-breakdown\">")
        parts.append("        <h3 style=\"color:#2144a9;margin-top:10px;\">预算分配建议</h3>")
        for item in itinerary["budget_breakdown"]:
            width = int(item["ratio"] * 100)
            amount_formatted = _format_amount(item["amount"], symbol)
            label = escape(item["label"])
            parts.append("        <div class=\"budget-item\">")
            parts.append(f"          <div class=\"budget-label\">{label}</div>")
            parts.append(f"          <div class=\"budget-amount\">建议投入：{amount_formatted}</div>")
            parts.append("          <div class=\"budget-bar\"><span style=\"width: " + str(width) + "%\"></span></div>")
            parts.append("        </div>")
        parts.append("      </div>")
    parts.append("    </section>")

    parts.append("    <section>")
    parts.append("      <h2>每日行程安排</h2>")
    for plan in itinerary["daily_plans"]:
        day_title = f"Day {plan['day']} · {escape(plan['theme'])}"
        parts.append("      <div class=\"day-card\">")
        parts.append(f"        <h3>{day_title}</h3>")
        parts.append("        <div class=\"activities\">")
        for label, activity in (("上午", plan["morning"]), ("下午", plan["afternoon"]), ("晚上", plan["evening"])):
            parts.append("          <div class=\"activity\">")
            parts.append(f"            <img src=\"{_safe_url(activity['image_url'])}\" alt=\"{escape(activity['title'])}\">")
            parts.append("            <div class=\"activity-content\">")
            parts.append(f"              <h4>{label} · {escape(activity['title'])}</h4>")
            parts.append(f"              <p>{escape(activity['description'])}</p>")
            parts.append("            </div>")
            parts.append("          </div>")
        parts.append("        </div>")
        parts.append("        <div class=\"logistics\">")
        parts.append(f"          <div class=\"logistics-item\"><strong>交通建议</strong>：{escape(plan['transport_tip'])}</div>")
        parts.append(f"          <div class=\"logistics-item\"><strong>住宿建议</strong>：{escape(plan['accommodation_tip'])}</div>")
        parts.append("        </div>")
        parts.append("      </div>")
    parts.append("    </section>")

    def _render_highlights(title: str, items: Iterable[Dict[str, Any]]) -> None:
        items = list(items)
        if not items:
            return
        parts.append("    <section>")
        parts.append(f"      <h2>{escape(title)}</h2>")
        parts.append("      <div class=\"recommendation-grid\">")
        for item in items:
            parts.append("        <div class=\"recommendation-card\">")
            parts.append(f"          <img src=\"{_safe_url(item['image_url'])}\" alt=\"{escape(item['title'])}\">")
            parts.append(f"          <h4>{escape(item['title'])}</h4>")
            parts.append(f"          <p>{escape(item['description'])}</p>")
            parts.append("        </div>")
        parts.append("      </div>")
        parts.append("    </section>")

    _render_highlights("当地特色美食推荐", itinerary.get("foods", []))
    _render_highlights("必买伴手礼", itinerary.get("souvenirs", []))
    _render_highlights("特色体验项目", itinerary.get("experiences", []))

    parts.append("    <section>")
    parts.append("      <h2>贴心提示</h2>")
    parts.append("      <div class=\"tips-columns\">")
    if itinerary.get("accommodation_tips"):
        parts.append("        <div><h3>住宿亮点</h3><ul>")
        for tip in itinerary["accommodation_tips"]:
            parts.append(f"          <li>{escape(tip)}</li>")
        parts.append("        </ul></div>")
    if itinerary.get("transport_tips"):
        parts.append("        <div><h3>交通建议</h3><ul>")
        for tip in itinerary["transport_tips"]:
            parts.append(f"          <li>{escape(tip)}</li>")
        parts.append("        </ul></div>")
    if itinerary.get("extra_tips"):
        parts.append("        <div><h3>行前须知</h3><ul>")
        for tip in itinerary["extra_tips"]:
            parts.append(f"          <li>{escape(tip)}</li>")
        parts.append("        </ul></div>")
    parts.append("      </div>")
    parts.append("    </section>")

    contact = itinerary.get("contact", {})
    parts.append("    <section>")
    parts.append("      <h2>联系我们</h2>")
    parts.append("      <div class=\"cta\">")
    cta_label = escape(contact.get("cta_label", "立即咨询"))
    cta_link = _safe_url(contact.get("cta_link", "#"))
    parts.append(f"        <a href=\"{cta_link}\" target=\"_blank\">{cta_label}</a>")
    parts.append("      </div>")
    contact_items = []
    if contact.get("phone"):
        contact_items.append("电话：" + escape(contact["phone"]))
    if contact.get("wechat"):
        contact_items.append("微信：" + escape(contact["wechat"]))
    if contact.get("email"):
        contact_items.append("邮箱：" + escape(contact["email"]))
    if contact.get("company"):
        contact_items.append("服务机构：" + escape(contact["company"]))
    if contact_items:
        parts.append("      <div class=\"contact-info\">")
        for item in contact_items:
            parts.append(f"        <span>{item}</span>")
        parts.append("      </div>")
    parts.append("    </section>")

    parts.append("  </main>")
    parts.append("  <footer>")
    parts.append("    本方案由TravelMaster旅行顾问团队匠心打造 · 支持进一步深度定制")
    parts.append("  </footer>")
    parts.append("</body>")
    parts.append("</html>")

    return "\n".join(parts)
