from typing import Optional, List, Dict, Any

from zeep import Client
from pathlib import Path
import json


TEDB_WSDL_URL = "https://ec.europa.eu/taxation_customs/tedb/ws/VatRetrievalService.wsdl"


EU_STATES = [
    'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','EL','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE'
]


def fetch_vat_rates(date_from: str, date_to: str, iso_list: Optional[List[str]] = None) -> Dict[str, Any]:
    client = Client(TEDB_WSDL_URL)
    svc = client.service
    if not iso_list:
        iso_list = [s for s in EU_STATES if s != 'GR']
    req = {
        'memberStates': {'isoCode': iso_list},
        'from': date_from,
        'to': date_to,
    }
    res = svc.retrieveVatRates(**req)
    # zeep returns an object; the CLI mapper will serialize
    from zeep.helpers import serialize_object
    doc = serialize_object(res)
    # Also persist raw fetched data for transparency
    raw_dir = Path('data/raw')
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f'tedb_{date_from}_to_{date_to}.json'
    try:
        raw_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    except Exception:
        # Best-effort; if serialization fails on exotic types, skip raw write
        pass
    return doc


