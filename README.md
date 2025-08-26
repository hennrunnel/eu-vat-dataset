## EU VAT Rates and Categories by Member State — Dataset

- Retrieved at: 2025-08-26 (UTC)
- Context: Public dataset generated from the European Commission's TEDB to feed Voog's upcoming multi‑VAT support with up‑to‑date official EU VAT categories and rates for multilingual websites and stores.
- Sources:
  - TEDB (EC UI): https://ec.europa.eu/taxation_customs/tedb/#/home
  - TEDB VAT SOAP WSDL: https://ec.europa.eu/taxation_customs/tedb/ws/VatRetrievalService.wsdl
- Coverage: EU members = 0
- Schema:
  - country_fields: iso2, name
  - category_fields: label, rate_percent, category_id, rate_type

EU VAT rates and categories aggregated from the European Commission’s Taxes in Europe Database (TEDB).

This repository feeds Voog’s upcoming multi‑VAT support to help merchants stay compliant across the EU.
Voog lets you build multilingual websites and online stores that scale internationally.
[Start your 30‑day free trial](https://www.voog.com).

### Usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m vatkit.cli
```

This will fetch from TEDB, map categories, and update this README and `data/parsed/latest.json`.

Official VAT category reference:
- Annex III to the VAT Directive (eligible reduced-rate categories): https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32006L0112#d1e32-69-1
- TEDB documentation entry point: https://ec.europa.eu/taxation_customs/tedb/#/home

### Dataset (full)

| iso2 | country | category_label | rate_percent |
| --- | --- | --- | --- |

### Notes

- TEDB is the authoritative EC source for VAT rates.
- Latest per category is selected by situationOn.
