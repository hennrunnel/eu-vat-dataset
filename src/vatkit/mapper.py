from typing import Dict, Any, List, Optional


ISO2_TO_COUNTRY = {
    'AT': 'Austria','BE':'Belgium','BG':'Bulgaria','HR':'Croatia','CY':'Cyprus','CZ':'Czech Republic','DK':'Denmark',
    'EE':'Estonia','FI':'Finland','FR':'France','DE':'Germany','EL':'Greece','GR':'Greece','HU':'Hungary','IE':'Ireland',
    'IT':'Italy','LV':'Latvia','LT':'Lithuania','LU':'Luxembourg','MT':'Malta','NL':'Netherlands','PL':'Poland','PT':'Portugal',
    'RO':'Romania','SK':'Slovakia','SI':'Slovenia','ES':'Spain','SE':'Sweden'
}


def map_tedb_to_unified(doc: Dict[str, Any], only_date: Optional[str] = None) -> Dict[str, Any]:
    results = doc.get('vatRateResults', []) or []
    if only_date:
        results = [i for i in results if (i.get('situationOn') or '') == only_date]
    by_state: Dict[str, Dict[str, Dict[str, Any]]] = {}

    def label_for(item: Dict[str, Any]) -> str:
        rate = (item.get('rate') or {}).get('type') or ''
        cat = item.get('category') or {}
        identifier = str(cat.get('identifier', '')).strip()
        description = str(cat.get('description', '')).strip()
        if rate.upper() == 'STANDARD_RATE':
            return 'Standard'
        if identifier:
            return identifier.replace('_', ' ').title()
        if description:
            return description
        t = str(item.get('type', '')).title()
        return t or 'Rate'

    for item in results:
        iso2 = str(item.get('memberState', '')).upper()
        if not iso2:
            continue
        try:
            value = float(((item.get('rate') or {}).get('value')))
        except Exception:
            continue
        if value < 0 or value > 50:
            continue
        label = label_for(item)
        rate_type = (item.get('rate') or {}).get('type') or ''
        category_id = (item.get('category') or {}).get('identifier')
        date_s = (item.get('situationOn') or '')
        state_map = by_state.setdefault(iso2, {})
        prev = state_map.get(label)
        if prev is None or date_s > prev.get('_date', ''):
            state_map[label] = {
                'label': label,
                'rate_percent': value,
                **({'category_id': category_id} if category_id else {}),
                **({'rate_type': rate_type} if rate_type else {}),
                '_date': date_s,
            }

    countries: List[Dict[str, Any]] = []
    for iso2, cats in sorted(by_state.items()):
        name = ISO2_TO_COUNTRY.get(iso2, iso2)
        categories = [
            {k: v for k, v in entry.items() if k != '_date'}
            for entry in cats.values()
        ]
        countries.append({'iso2': iso2 if iso2 != 'EL' else 'GR', 'name': name, 'categories': categories})

    return {'countries': countries}


