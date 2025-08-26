import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_json(unified: Dict[str, Any]) -> Path:
    out = Path('data/parsed/latest.json')
    ensure_dir(out.parent)
    out.write_text(json.dumps(unified, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
    return out


def write_markdown(unified: Dict[str, Any]) -> Path:
    out = Path('README.md')
    # Build table header
    headers = ['iso2', 'country', 'category_label', 'rate_percent']
    lines = []
    countries = unified.get('countries', [])
    # Always use today's UTC date
    today_utc = datetime.utcnow().date().isoformat()
    # Plain text header (no YAML frontmatter)
    header = [
        '## EU VAT Rates and Categories by Member State — Dataset',
        '',
        f'- Retrieved at: {today_utc} (UTC)',
        "- Context: Public dataset generated from the European Commission's TEDB to feed Voog's upcoming multi‑VAT support with up‑to‑date official EU VAT categories and rates for multilingual websites and stores.",
        '- Sources:',
        '  - TEDB (EC UI): https://ec.europa.eu/taxation_customs/tedb/#/home',
        '  - TEDB VAT SOAP WSDL: https://ec.europa.eu/taxation_customs/tedb/ws/VatRetrievalService.wsdl',
        f'- Coverage: EU members = {len(countries)}',
        '- Schema:',
        '  - country_fields: iso2, name',
        '  - category_fields: label, rate_percent, category_id, rate_type',
        '',
    ]
    lines.extend(header)
    # Intro with Voog blurb and CTA
    intro = [
        'EU VAT rates and categories aggregated from the European Commission’s Taxes in Europe Database (TEDB).',
        '',
        'This repository feeds Voog’s upcoming multi‑VAT support to help merchants stay compliant across the EU.',
        'Voog lets you build multilingual websites and online stores that scale internationally.',
        '[Start your 30‑day free trial](https://www.voog.com).',
        '',
        '### Usage',
        '',
        '```bash',
        'python3 -m venv .venv',
        'source .venv/bin/activate',
        'pip install -r requirements.txt',
        'PYTHONPATH=src python -m vatkit.cli',
        '```',
        '',
        'This will fetch from TEDB, map categories, and update this README and `data/parsed/latest.json`.',
        '',
        'Official VAT category reference:',
        '- Annex III to the VAT Directive (eligible reduced-rate categories): https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32006L0112#d1e32-69-1',
        '- TEDB documentation entry point: https://ec.europa.eu/taxation_customs/tedb/#/home',
        '',
        '### Dataset (full)',
        '',
    ]
    lines.extend(intro)
    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
    for c in countries:
        iso2 = c.get('iso2', '')
        country = c.get('name', '')
        for cat in c.get('categories', []):
            label = str(cat.get('label', ''))
            rate = cat.get('rate_percent')
            rate_s = str(rate)
            lines.append(f"| {iso2} | {country} | {label} | {rate_s} |")
    # Notes
    lines.extend([
        '',
        '### Notes',
        '',
        '- TEDB is the authoritative EC source for VAT rates.',
        '- Latest per category is selected by situationOn.',
    ])
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return out


