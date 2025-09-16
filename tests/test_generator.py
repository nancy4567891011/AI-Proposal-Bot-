from __future__ import annotations

import pytest

from itinerary_generator import TravelItineraryGenerator, render_itinerary_html


def test_generate_tokyo_itinerary_contains_expected_sections():
    generator = TravelItineraryGenerator()
    itinerary = generator.generate_itinerary("东京", budget=24000, travellers=2)

    assert itinerary["destination"] == "日本东京"
    assert itinerary["recommended_days"] >= 4
    assert len(itinerary["daily_plans"]) == itinerary["recommended_days"]
    assert itinerary["budget"]["total"] == pytest.approx(24000)

    html = render_itinerary_html(itinerary)
    assert "<!DOCTYPE html>" in html
    assert "东京定制行程" in html
    assert "当地特色美食推荐" in html


def test_per_person_budget_multiplier_and_group_label():
    generator = TravelItineraryGenerator()
    itinerary = generator.generate_itinerary(
        "法国巴黎",
        budget=15000,
        travellers=3,
        per_person_budget=True,
    )

    assert itinerary["budget"]["total"] == pytest.approx(45000)
    assert "家庭" in itinerary["group_label"]
    assert itinerary["recommended_days"] >= 4


def test_unknown_destination_uses_generic_profile():
    generator = TravelItineraryGenerator()
    itinerary = generator.generate_itinerary("火星探索基地", budget=8000, travellers=2)

    assert itinerary["destination_key"] == "generic"
    assert itinerary["daily_plans"]
    html = render_itinerary_html(itinerary)
    assert "梦想之旅" in html


def test_invalid_inputs_raise_errors():
    generator = TravelItineraryGenerator()

    with pytest.raises(ValueError):
        generator.generate_itinerary("东京", budget=0, travellers=1)

    with pytest.raises(ValueError):
        generator.generate_itinerary("东京", budget=5000, travellers=0)
