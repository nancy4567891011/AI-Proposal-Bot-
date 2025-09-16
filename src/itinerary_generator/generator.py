"""Core logic to build a customised travel itinerary."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, Iterable, List, Mapping, Optional
import re

from .data import DESTINATIONS, GENERIC_PROFILE, DestinationProfile

DEFAULT_CONTACT = {
    "company": "TravelMaster 定制中心",
    "phone": "400-800-1234",
    "wechat": "TravelMasterVIP",
    "email": "service@travelmaster.com",
    "cta_link": "https://example.com/contact",
    "cta_label": "立即预订",
}


def _normalize_destination(value: str) -> str:
    normalized = re.sub(r"[\s·,./\\-]+", "", value.strip().lower())
    normalized = re.sub(r"(travel|tour|trip|city)", "", normalized)
    return normalized


def _format_currency(value: float, currency_symbol: str) -> str:
    rounded = round(value)
    return f"{currency_symbol}{rounded:,.0f}"


class TravelItineraryGenerator:
    """Generate data structures representing a travel itinerary."""

    def __init__(self, *, currency_symbol: str = "¥", profiles: Optional[Mapping[str, DestinationProfile]] = None) -> None:
        self.currency_symbol = currency_symbol
        if profiles is None:
            profiles = DESTINATIONS
        self.profiles = dict(profiles)

    def available_destinations(self) -> Iterable[str]:
        for profile in self.profiles.values():
            yield profile.display_name

    def generate_itinerary(
        self,
        destination: str,
        budget: float,
        travellers: int,
        *,
        per_person_budget: bool = False,
        currency_symbol: Optional[str] = None,
        contact_info: Optional[Mapping[str, str]] = None,
    ) -> Dict[str, Any]:
        if budget <= 0:
            raise ValueError("budget must be greater than zero")
        if travellers <= 0:
            raise ValueError("travellers must be greater than zero")

        profile = self._resolve_profile(destination)
        currency = currency_symbol or self.currency_symbol
        total_budget = budget * travellers if per_person_budget else budget
        per_person = total_budget / travellers

        recommended_days = self._calculate_days(total_budget, travellers, profile)
        daily_plans = self._build_daily_plans(profile, recommended_days)
        budget_breakdown = self._build_budget_breakdown(total_budget)
        contact = self._merge_contact(contact_info)

        return {
            "destination": profile.display_name,
            "destination_key": profile.key,
            "country": profile.country,
            "tagline": profile.tagline,
            "cover_image": profile.cover_image,
            "recommended_days": recommended_days,
            "budget": {
                "total": total_budget,
                "per_person": per_person,
                "currency_symbol": currency,
                "total_formatted": _format_currency(total_budget, currency),
                "per_person_formatted": _format_currency(per_person, currency),
            },
            "travellers": travellers,
            "group_label": self._group_label(travellers),
            "daily_plans": daily_plans,
            "foods": [asdict(item) for item in profile.foods],
            "souvenirs": [asdict(item) for item in profile.souvenirs],
            "experiences": [asdict(item) for item in profile.experiences],
            "accommodation_tips": list(profile.accommodation_tips),
            "transport_tips": list(profile.transport_tips),
            "extra_tips": list(profile.extra_tips),
            "budget_breakdown": budget_breakdown,
            "contact": contact,
        }

    def _resolve_profile(self, destination: str) -> DestinationProfile:
        normalized = _normalize_destination(destination)
        for profile in self.profiles.values():
            for alias in profile.all_aliases():
                alias_normalized = _normalize_destination(alias)
                if alias_normalized == normalized or alias_normalized in normalized or normalized in alias_normalized:
                    return profile
        return GENERIC_PROFILE

    def _calculate_days(self, total_budget: float, travellers: int, profile: DestinationProfile) -> int:
        per_person = total_budget / travellers
        raw_days = per_person / max(profile.ideal_daily_cost, 1)
        if raw_days < profile.min_days:
            recommended = profile.min_days
        else:
            recommended = int(round(raw_days))
        recommended = max(profile.min_days, recommended)
        recommended = min(profile.max_days, recommended)
        return recommended

    def _build_daily_plans(self, profile: DestinationProfile, days: int) -> List[Dict[str, Any]]:
        plans: List[Dict[str, Any]] = []
        for index in range(days):
            theme = profile.daily_themes[index % len(profile.daily_themes)]
            morning = profile.morning_options[index % len(profile.morning_options)]
            afternoon = profile.afternoon_options[index % len(profile.afternoon_options)]
            evening = profile.evening_options[index % len(profile.evening_options)]
            accommodation_tip = profile.accommodation_tips[index % len(profile.accommodation_tips)]
            transport_tip = profile.transport_tips[index % len(profile.transport_tips)]
            plans.append(
                {
                    "day": index + 1,
                    "theme": theme,
                    "morning": asdict(morning),
                    "afternoon": asdict(afternoon),
                    "evening": asdict(evening),
                    "accommodation_tip": accommodation_tip,
                    "transport_tip": transport_tip,
                }
            )
        return plans

    def _build_budget_breakdown(self, total_budget: float) -> List[Dict[str, Any]]:
        allocation = [
            ("住宿", 0.35),
            ("交通", 0.2),
            ("餐饮", 0.2),
            ("体验活动", 0.15),
            ("其他/备用", 0.1),
        ]
        remaining = total_budget
        breakdown: List[Dict[str, Any]] = []
        for label, ratio in allocation:
            amount = round(total_budget * ratio, 2)
            breakdown.append(
                {
                    "label": label,
                    "amount": amount,
                    "ratio": ratio,
                }
            )
            remaining -= amount
        if breakdown:
            breakdown[-1]["amount"] = round(breakdown[-1]["amount"] + remaining, 2)
        return breakdown

    def _merge_contact(self, contact_info: Optional[Mapping[str, str]]) -> Dict[str, str]:
        contact = dict(DEFAULT_CONTACT)
        if contact_info:
            contact.update({key: str(value) for key, value in contact_info.items()})
        return contact

    @staticmethod
    def _group_label(travellers: int) -> str:
        if travellers <= 1:
            return "高端独行/商务访客"
        if travellers == 2:
            return "情侣/好友双人行"
        if travellers <= 5:
            return "家庭或亲友小团"
        if travellers <= 10:
            return "精品小团队"
        return "企业团建/大型团组"
