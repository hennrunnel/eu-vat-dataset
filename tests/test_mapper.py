import json
from pathlib import Path

from vatkit.mapper import map_tedb_to_unified


def test_map_tedb_to_unified_basic(tmp_path: Path):
    sample = {
        "vatRateResults": [
            {
                "memberState": "EE",
                "type": "REDUCED",
                "rate": {"type": "STANDARD_RATE", "value": 24.0},
                "situationOn": "2024-01-01",
                "category": {"identifier": "STANDARD_RATE"},
            },
            {
                "memberState": "EE",
                "type": "REDUCED",
                "rate": {"type": "REDUCED_RATE", "value": 9.0},
                "situationOn": "2024-01-01",
                "category": {"identifier": "PHARMACEUTICAL_PRODUCTS"},
            },
        ]
    }
    unified = map_tedb_to_unified(sample)
    countries = {c["iso2"]: c for c in unified["countries"]}
    assert "EE" in countries
    cats = {c["label"]: c for c in countries["EE"]["categories"]}
    assert cats["Standard"]["rate_percent"] == 24.0
    assert cats["Pharmaceutical Products"]["rate_percent"] == 9.0


