## EU VAT Rates and Categories by Member State — Dataset

- Retrieved at: 2025-08-26 (UTC)
- Context: Public dataset generated from the European Commission's TEDB to feed Voog's upcoming multi‑VAT support with up‑to‑date official EU VAT categories and rates for multilingual websites and stores.
- Sources:
  - TEDB (EC UI): https://ec.europa.eu/taxation_customs/tedb/#/home
  - TEDB VAT SOAP WSDL: https://ec.europa.eu/taxation_customs/tedb/ws/VatRetrievalService.wsdl
- Coverage: EU members = 27
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
| AT | Austria | Foodstuffs | 10.0 |
| AT | Austria | Cultural Events | 13.0 |
| AT | Austria | Parking | 13.0 |
| AT | Austria | Transport Passengers | 13.0 |
| AT | Austria | Writers Services | 13.0 |
| AT | Austria | Sporting Events | 13.0 |
| AT | Austria | Region | 19.0 |
| AT | Austria | Zero Reduced Rate | 10.0 |
| AT | Austria | Supply Water | 10.0 |
| AT | Austria | Loan Libraries | 10.0 |
| AT | Austria | Newspapers | 10.0 |
| AT | Austria | Periodicals | 10.0 |
| AT | Austria | Pharmaceutical Products | 0.0 |
| AT | Austria | Street Cleaning | 10.0 |
| AT | Austria | Accommodation | 10.0 |
| AT | Austria | Restaurant | 10.0 |
| AT | Austria | Broadcasting Services | 10.0 |
| AT | Austria | Bicycles Repair | 10.0 |
| AT | Austria | Clothing Repair | 10.0 |
| AT | Austria | Shoes Repair | 10.0 |
| AT | Austria | Social Wellbeing | 10.0 |
| AT | Austria | Tapestries | 13.0 |
| AT | Austria | Pictures | 13.0 |
| AT | Austria | Impressions | 13.0 |
| AT | Austria | Sculptures | 13.0 |
| AT | Austria | Postage | 13.0 |
| AT | Austria | Zoological | 13.0 |
| AT | Austria | 100 Years Old | 13.0 |
| AT | Austria | Photographs | 13.0 |
| AT | Austria | Agricultural Production | 13.0 |
| AT | Austria | Solar Panels | 0.0 |
| AT | Austria | Standard | 20.0 |
| BE | Belgium | Writers Services | 0.0 |
| BE | Belgium | Medical Care | 0.0 |
| BE | Belgium | Transport Passengers | 0.0 |
| BE | Belgium | Cultural Events | 0.0 |
| BE | Belgium | Loan Libraries | 0.0 |
| BE | Belgium | Sporting Facilities | 0.0 |
| BE | Belgium | Zero Rate | 0.0 |
| BE | Belgium | Foodstuffs | 6.0 |
| BE | Belgium | Medical Equipment | 6.0 |
| BE | Belgium | Agricultural Production | 6.0 |
| BE | Belgium | Temporary | 6.0 |
| BE | Belgium | Pharmaceutical Products | 0.0 |
| BE | Belgium | Super Temporary | 0.0 |
| BE | Belgium | Undertakers Services | 6.0 |
| BE | Belgium | Photographs | 6.0 |
| BE | Belgium | Tapestries | 6.0 |
| BE | Belgium | Pictures | 6.0 |
| BE | Belgium | Enamels | 6.0 |
| BE | Belgium | Impressions | 6.0 |
| BE | Belgium | Sculpture Casts | 6.0 |
| BE | Belgium | Ceramics | 6.0 |
| BE | Belgium | Sculptures | 6.0 |
| BE | Belgium | Zoological | 6.0 |
| BE | Belgium | 100 Years Old | 6.0 |
| BE | Belgium | Supply Water | 6.0 |
| BE | Belgium | Housing Provision | 6.0 |
| BE | Belgium | Private Dwellings | 6.0 |
| BE | Belgium | Accommodation | 6.0 |
| BE | Belgium | Sporting Events | 0.0 |
| BE | Belgium | Shoes Repair | 6.0 |
| BE | Belgium | Clothing Repair | 6.0 |
| BE | Belgium | Bicycles Repair | 6.0 |
| BE | Belgium | Social Wellbeing | 6.0 |
| BE | Belgium | Parking | 12.0 |
| BE | Belgium | Restaurant | 12.0 |
| BE | Belgium | Postage | 6.0 |
| BE | Belgium | Supply Electricity | 6.0 |
| BE | Belgium | Supply Gas | 6.0 |
| BE | Belgium | Supply Heating | 6.0 |
| BE | Belgium | Plant | 6.0 |
| BE | Belgium | New Parking Rate | 12.0 |
| BE | Belgium | Sustainable Energy | 6.0 |
| BE | Belgium | Construction | 6.0 |
| BE | Belgium | Renovation | 6.0 |
| BE | Belgium | Solar Panels | 6.0 |
| BE | Belgium | Wood | 6.0 |
| BE | Belgium | Bicycles Rental | 6.0 |
| BE | Belgium | Fossil Fuel | 12.0 |
| BE | Belgium | Wood Article98 | 6.0 |
| BE | Belgium | Standard | 21.0 |
| BG | Bulgaria | Loan Libraries | 9.0 |
| BG | Bulgaria | Pharmaceutical Products | 9.0 |
| BG | Bulgaria | Accommodation | 9.0 |
| BG | Bulgaria | Restaurant | 9.0 |
| BG | Bulgaria | Foodstuffs | 9.0 |
| BG | Bulgaria | Sporting Events | 9.0 |
| BG | Bulgaria | Temporary Exemption Rate | 9.0 |
| BG | Bulgaria | Sporting Facilities | 9.0 |
| BG | Bulgaria | Zero Rate | 0.0 |
| BG | Bulgaria | Supply Gas | 9.0 |
| BG | Bulgaria | Supply Heating | 9.0 |
| BG | Bulgaria | Standard | 20.0 |
| CY | Cyprus | Foodstuffs | 5.0 |
| CY | Cyprus | Pharmaceutical Products | 5.0 |
| CY | Cyprus | Agricultural Production | 5.0 |
| CY | Cyprus | Medical Equipment | 5.0 |
| CY | Cyprus | Children Car Seats | 5.0 |
| CY | Cyprus | Zoological | 5.0 |
| CY | Cyprus | 100 Years Old | 5.0 |
| CY | Cyprus | Undertakers Services | 0.0 |
| CY | Cyprus | Supply Water | 5.0 |
| CY | Cyprus | Street Cleaning | 5.0 |
| CY | Cyprus | Housing Provision | 5.0 |
| CY | Cyprus | Transport Passengers | 5.0 |
| CY | Cyprus | Writers Services | 5.0 |
| CY | Cyprus | Medical Care | 5.0 |
| CY | Cyprus | Cultural Events | 0.0 |
| CY | Cyprus | Sporting Events | 5.0 |
| CY | Cyprus | Hairdressing | 5.0 |
| CY | Cyprus | Accommodation | 9.0 |
| CY | Cyprus | Restaurant | 9.0 |
| CY | Cyprus | Books | 3.0 |
| CY | Cyprus | Newspapers | 3.0 |
| CY | Cyprus | Periodicals | 3.0 |
| CY | Cyprus | Waste Treatment Refusal | 3.0 |
| CY | Cyprus | Waste Treatment | 3.0 |
| CY | Cyprus | Theatre Performances | 3.0 |
| CY | Cyprus | Private Dwellings | 0.0 |
| CY | Cyprus | Social Wellbeing | 0.0 |
| CY | Cyprus | Loan Libraries | 5.0 |
| CY | Cyprus | Temporary | 5.0 |
| CY | Cyprus | Standard | 19.0 |
| CZ | Czech Republic | Foodstuffs | 12.0 |
| CZ | Czech Republic | Pharmaceutical Products | 12.0 |
| CZ | Czech Republic | Loan Libraries | 0.0 |
| CZ | Czech Republic | Tapestries | 0.0 |
| CZ | Czech Republic | Children Car Seats | 12.0 |
| CZ | Czech Republic | Pictures | 0.0 |
| CZ | Czech Republic | Impressions | 0.0 |
| CZ | Czech Republic | Sculptures | 0.0 |
| CZ | Czech Republic | Sculpture Casts | 0.0 |
| CZ | Czech Republic | Postage | 0.0 |
| CZ | Czech Republic | Zoological | 0.0 |
| CZ | Czech Republic | Supply Water | 12.0 |
| CZ | Czech Republic | Street Cleaning | 15.0 |
| CZ | Czech Republic | Transport Passengers | 12.0 |
| CZ | Czech Republic | Accommodation | 12.0 |
| CZ | Czech Republic | Restaurant | 12.0 |
| CZ | Czech Republic | Window Cleaning | 10.0 |
| CZ | Czech Republic | Medical Care | 12.0 |
| CZ | Czech Republic | Social Wellbeing | 12.0 |
| CZ | Czech Republic | Domestic Care | 12.0 |
| CZ | Czech Republic | Cultural Events | 12.0 |
| CZ | Czech Republic | Writers Services | 15.0 |
| CZ | Czech Republic | Sporting Events | 12.0 |
| CZ | Czech Republic | Sporting Facilities | 10.0 |
| CZ | Czech Republic | Undertakers Services | 12.0 |
| CZ | Czech Republic | Medical Equipment | 12.0 |
| CZ | Czech Republic | Housing Provision | 12.0 |
| CZ | Czech Republic | Private Dwellings | 12.0 |
| CZ | Czech Republic | Zero Reduced Rate | 0.0 |
| CZ | Czech Republic | Newspapers | 10.0 |
| CZ | Czech Republic | Periodicals | 12.0 |
| CZ | Czech Republic | Supply Heating | 12.0 |
| CZ | Czech Republic | Shoes Repair | 10.0 |
| CZ | Czech Republic | Clothing Repair | 10.0 |
| CZ | Czech Republic | Bicycles Repair | 10.0 |
| CZ | Czech Republic | Hairdressing | 10.0 |
| CZ | Czech Republic | Plant | 12.0 |
| CZ | Czech Republic | Standard | 21.0 |
| DE | Germany | Zero Reduced Rate | 7.0 |
| DE | Germany | Foodstuffs | 7.0 |
| DE | Germany | Broadcasting Services | 0.0 |
| DE | Germany | Pictures | 7.0 |
| DE | Germany | Impressions | 7.0 |
| DE | Germany | Sculptures | 7.0 |
| DE | Germany | Sculpture Casts | 7.0 |
| DE | Germany | Supply Water | 7.0 |
| DE | Germany | Medical Equipment | 7.0 |
| DE | Germany | Transport Passengers | 7.0 |
| DE | Germany | Loan Libraries | 7.0 |
| DE | Germany | Newspapers | 7.0 |
| DE | Germany | Periodicals | 7.0 |
| DE | Germany | Cultural Events | 7.0 |
| DE | Germany | Writers Services | 7.0 |
| DE | Germany | Accommodation | 7.0 |
| DE | Germany | Social Wellbeing | 7.0 |
| DE | Germany | Medical Care | 7.0 |
| DE | Germany | Zoological | 7.0 |
| DE | Germany | Supply Electricity | 0.0 |
| DE | Germany | Zero Rate | 0.0 |
| DE | Germany | Pharmaceutical Products | 7.0 |
| DE | Germany | Plant | 7.0 |
| DE | Germany | Supply Gas | 7.0 |
| DE | Germany | Restaurant | 7.0 |
| DE | Germany | Postage | 7.0 |
| DE | Germany | Standard | 19.0 |
| DK | Denmark | Transport Passengers | 0.0 |
| DK | Denmark | Social Wellbeing | 0.0 |
| DK | Denmark | Writers Services | 0.0 |
| DK | Denmark | Cultural Events | 0.0 |
| DK | Denmark | Sporting Facilities | 0.0 |
| DK | Denmark | Sporting Events | 0.0 |
| DK | Denmark | Undertakers Services | 0.0 |
| DK | Denmark | Zero Rate | 0.0 |
| DK | Denmark | Zero Reduced Rate | 0.0 |
| DK | Denmark | Standard | 25.0 |
| EE | Estonia | Medical Equipment | 9.0 |
| EE | Estonia | Zero Rate | 0.0 |
| EE | Estonia | Pharmaceutical Products | 9.0 |
| EE | Estonia | Accommodation | 13.0 |
| EE | Estonia | Loan Libraries | 9.0 |
| EE | Estonia | Newspapers | 9.0 |
| EE | Estonia | Standard | 24.0 |
| GR | Greece | Foodstuffs | 13.0 |
| GR | Greece | Zero Reduced Rate | 0.0 |
| GR | Greece | Supply Gas | 6.0 |
| GR | Greece | Supply Electricity | 6.0 |
| GR | Greece | Pharmaceutical Products | 6.0 |
| GR | Greece | Loan Libraries | 6.0 |
| GR | Greece | Newspapers | 6.0 |
| GR | Greece | Periodicals | 6.0 |
| GR | Greece | Cultural Events | 6.0 |
| GR | Greece | Supply Heating | 6.0 |
| GR | Greece | Medical Equipment | 6.0 |
| GR | Greece | Agricultural Production | 6.0 |
| GR | Greece | Transport Passengers | 13.0 |
| GR | Greece | Accommodation | 13.0 |
| GR | Greece | Domestic Care | 13.0 |
| GR | Greece | Social Wellbeing | 13.0 |
| GR | Greece | Supply Water | 13.0 |
| GR | Greece | Region | 17.0 |
| GR | Greece | Children Car Seats | 13.0 |
| GR | Greece | Pictures | 13.0 |
| GR | Greece | Impressions | 13.0 |
| GR | Greece | Sculpture Casts | 13.0 |
| GR | Greece | Postage | 13.0 |
| GR | Greece | Zoological | 13.0 |
| GR | Greece | 100 Years Old | 13.0 |
| GR | Greece | Restaurant | 13.0 |
| GR | Greece | Medical Care | 6.0 |
| GR | Greece | Sporting Facilities | 13.0 |
| GR | Greece | Agricultural Equipment | 13.0 |
| GR | Greece | Sporting Events | 13.0 |
| GR | Greece | Non Owned Residency Renovation | 4.0 |
| GR | Greece | Standard | 24.0 |
| ES | Spain | Super Temporary | 4.0 |
| ES | Spain | Foodstuffs | 10.0 |
| ES | Spain | Supply Water | 10.0 |
| ES | Spain | Pharmaceutical Products | 10.0 |
| ES | Spain | Agricultural Production | 10.0 |
| ES | Spain | Tapestries | 10.0 |
| ES | Spain | Medical Equipment | 10.0 |
| ES | Spain | Pictures | 10.0 |
| ES | Spain | Impressions | 10.0 |
| ES | Spain | Photographs | 10.0 |
| ES | Spain | Sculptures | 10.0 |
| ES | Spain | Sculpture Casts | 10.0 |
| ES | Spain | Ceramics | 10.0 |
| ES | Spain | Enamels | 10.0 |
| ES | Spain | Postage | 10.0 |
| ES | Spain | Zoological | 10.0 |
| ES | Spain | 100 Years Old | 10.0 |
| ES | Spain | Street Cleaning | 10.0 |
| ES | Spain | Transport Passengers | 10.0 |
| ES | Spain | Private Dwellings | 10.0 |
| ES | Spain | Accommodation | 10.0 |
| ES | Spain | Restaurant | 10.0 |
| ES | Spain | Sporting Events | 10.0 |
| ES | Spain | Social Wellbeing | 10.0 |
| ES | Spain | Cultural Events | 10.0 |
| ES | Spain | Supply Electricity | 10.0 |
| ES | Spain | Exemption Superreduced | 4.0 |
| ES | Spain | Standard | 7.0 |
| FI | Finland | Foodstuffs | 14.0 |
| FI | Finland | Pharmaceutical Products | 14.0 |
| FI | Finland | Loan Libraries | 14.0 |
| FI | Finland | Photographs | 14.0 |
| FI | Finland | Tapestries | 14.0 |
| FI | Finland | Pictures | 14.0 |
| FI | Finland | Impressions | 14.0 |
| FI | Finland | Sculptures | 14.0 |
| FI | Finland | Sculpture Casts | 14.0 |
| FI | Finland | Transport Passengers | 14.0 |
| FI | Finland | Accommodation | 14.0 |
| FI | Finland | Cultural Events | 14.0 |
| FI | Finland | Broadcasting Services | 10.0 |
| FI | Finland | Writers Services | 14.0 |
| FI | Finland | Sporting Facilities | 10.0 |
| FI | Finland | Sporting Events | 14.0 |
| FI | Finland | Zero Reduced Rate | 0.0 |
| FI | Finland | Restaurant | 14.0 |
| FI | Finland | Newspapers | 10.0 |
| FI | Finland | Periodicals | 10.0 |
| FI | Finland | Standard | 25.5 |
| FR | France | Foodstuffs | 5.5 |
| FR | France | Agricultural Production | 10.0 |
| FR | France | Pharmaceutical Products | 10.0 |
| FR | France | Newspapers | 2.1 |
| FR | France | Periodicals | 2.1 |
| FR | France | Broadcasting Services | 10.0 |
| FR | France | Cultural Events | 10.0 |
| FR | France | Medical Equipment | 5.5 |
| FR | France | Photographs | 5.5 |
| FR | France | Loan Libraries | 5.5 |
| FR | France | Tapestries | 5.5 |
| FR | France | Pictures | 5.5 |
| FR | France | Impressions | 5.5 |
| FR | France | Sculpture Casts | 5.5 |
| FR | France | Postage | 5.5 |
| FR | France | Zoological | 5.5 |
| FR | France | 100 Years Old | 5.5 |
| FR | France | Supply Electricity | 5.5 |
| FR | France | Supply Gas | 5.5 |
| FR | France | Supply Heating | 5.5 |
| FR | France | Street Cleaning | 10.0 |
| FR | France | Medical Care | 0.0 |
| FR | France | Region | 13.0 |
| FR | France | Private Dwellings | 10.0 |
| FR | France | Housing Provision | 10.0 |
| FR | France | Domestic Care | 5.5 |
| FR | France | Supply Water | 10.0 |
| FR | France | Sporting Events | 5.5 |
| FR | France | Writers Services | 10.0 |
| FR | France | Transport Passengers | 10.0 |
| FR | France | Accommodation | 10.0 |
| FR | France | Restaurant | 10.0 |
| FR | France | Window Cleaning | 0.0 |
| FR | France | Super Temporary | 2.1 |
| FR | France | Zero Reduced Rate | 0.0 |
| FR | France | Antiques | 5.5 |
| FR | France | Standard | 20.0 |
| FR | France | Solar Panels | 5.5 |
| HR | Croatia | Medical Equipment | 5.0 |
| HR | Croatia | Loan Libraries | 5.0 |
| HR | Croatia | Foodstuffs | 5.0 |
| HR | Croatia | Pharmaceutical Products | 5.0 |
| HR | Croatia | Cultural Events | 5.0 |
| HR | Croatia | Restaurant | 13.0 |
| HR | Croatia | Agricultural Production | 5.0 |
| HR | Croatia | Newspapers | 5.0 |
| HR | Croatia | Periodicals | 5.0 |
| HR | Croatia | Supply Water | 13.0 |
| HR | Croatia | Accommodation | 13.0 |
| HR | Croatia | Writers Services | 13.0 |
| HR | Croatia | Children Car Seats | 13.0 |
| HR | Croatia | Undertakers Services | 13.0 |
| HR | Croatia | Street Cleaning | 13.0 |
| HR | Croatia | Supply Electricity | 13.0 |
| HR | Croatia | Supply Gas | 5.0 |
| HR | Croatia | Zero Reduced Rate | 5.0 |
| HR | Croatia | Sporting Events | 5.0 |
| HR | Croatia | Supply Heating | 5.0 |
| HR | Croatia | Wood Article98 | 5.0 |
| HR | Croatia | Standard | 25.0 |
| HU | Hungary | Zero Rate | 0.0 |
| HU | Hungary | Foodstuffs | 5.0 |
| HU | Hungary | Pharmaceutical Products | 5.0 |
| HU | Hungary | Medical Equipment | 5.0 |
| HU | Hungary | Loan Libraries | 5.0 |
| HU | Hungary | Housing Provision | 5.0 |
| HU | Hungary | Accommodation | 5.0 |
| HU | Hungary | Restaurant | 5.0 |
| HU | Hungary | Broadcasting Services | 5.0 |
| HU | Hungary | Writers Services | 5.0 |
| HU | Hungary | Cultural Events | 18.0 |
| HU | Hungary | Supply Heating | 5.0 |
| HU | Hungary | Transport Passengers | 5.0 |
| HU | Hungary | Newspapers | 0.0 |
| HU | Hungary | Antiques | 5.0 |
| HU | Hungary | Standard | 27.0 |
| IE | Ireland | Zero Reduced Rate | 0.0 |
| IE | Ireland | Zero Rate | 0.0 |
| IE | Ireland | Loan Libraries | 0.0 |
| IE | Ireland | Sporting Facilities | 9.0 |
| IE | Ireland | Foodstuffs | 13.5 |
| IE | Ireland | Parking | 13.5 |
| IE | Ireland | Pharmaceutical Products | 0.0 |
| IE | Ireland | Photographs | 13.5 |
| IE | Ireland | Tapestries | 13.5 |
| IE | Ireland | Ceramics | 13.5 |
| IE | Ireland | Agricultural Production | 13.5 |
| IE | Ireland | Medical Equipment | 0.0 |
| IE | Ireland | Window Cleaning | 13.5 |
| IE | Ireland | Street Cleaning | 13.5 |
| IE | Ireland | Medical Care | 0.0 |
| IE | Ireland | Cultural Events | 13.5 |
| IE | Ireland | Shoes Repair | 0.0 |
| IE | Ireland | Clothing Repair | 0.0 |
| IE | Ireland | Bicycles Repair | 13.5 |
| IE | Ireland | Hairdressing | 13.5 |
| IE | Ireland | Super Temporary | 4.8 |
| IE | Ireland | Pictures | 13.5 |
| IE | Ireland | Impressions | 13.5 |
| IE | Ireland | Sculptures | 13.5 |
| IE | Ireland | Sculpture Casts | 13.5 |
| IE | Ireland | Enamels | 13.5 |
| IE | Ireland | 100 Years Old | 13.5 |
| IE | Ireland | Supply Gas | 13.5 |
| IE | Ireland | Supply Electricity | 13.5 |
| IE | Ireland | Housing Provision | 13.5 |
| IE | Ireland | Private Dwellings | 13.5 |
| IE | Ireland | Supply Heating | 13.5 |
| IE | Ireland | Accommodation | 13.5 |
| IE | Ireland | Restaurant | 13.5 |
| IE | Ireland | Standard | 23.0 |
| IE | Ireland | Solar Panels | 0.0 |
| IT | Italy | Foodstuffs | 10.0 |
| IT | Italy | Newspapers | 4.0 |
| IT | Italy | Periodicals | 4.0 |
| IT | Italy | Broadcasting Services | 4.0 |
| IT | Italy | Housing Provision | 10.0 |
| IT | Italy | Agricultural Production | 10.0 |
| IT | Italy | Social Wellbeing | 5.0 |
| IT | Italy | Transport Passengers | 5.0 |
| IT | Italy | Pharmaceutical Products | 5.0 |
| IT | Italy | Medical Equipment | 5.0 |
| IT | Italy | Private Dwellings | 10.0 |
| IT | Italy | Accommodation | 10.0 |
| IT | Italy | Sporting Events | 10.0 |
| IT | Italy | Street Cleaning | 10.0 |
| IT | Italy | Supply Electricity | 10.0 |
| IT | Italy | Pictures | 10.0 |
| IT | Italy | Sculptures | 10.0 |
| IT | Italy | Tapestries | 10.0 |
| IT | Italy | Enamels | 10.0 |
| IT | Italy | Supply Water | 10.0 |
| IT | Italy | Cultural Events | 10.0 |
| IT | Italy | Restaurant | 10.0 |
| IT | Italy | Supply Gas | 10.0 |
| IT | Italy | Zero Reduced Rate | 10.0 |
| IT | Italy | Zero Rate | 0.0 |
| IT | Italy | Writers Services | 10.0 |
| IT | Italy | Undertakers Services | 0.0 |
| IT | Italy | Medical Care | 0.0 |
| IT | Italy | Domestic Care | 0.0 |
| IT | Italy | Loan Libraries | 4.0 |
| IT | Italy | Super Temporary | 4.0 |
| IT | Italy | Postage | 10.0 |
| IT | Italy | Supply Heating | 10.0 |
| IT | Italy | Children Car Seats | 5.0 |
| IT | Italy | Sustainable Energy | 5.0 |
| IT | Italy | Exemption Superreduced | 4.0 |
| IT | Italy | Fossil Fuel | 10.0 |
| IT | Italy | Wood | 10.0 |
| IT | Italy | Chemical Fertilisers | 4.0 |
| IT | Italy | Temporary Exemption Rate | 4.0 |
| IT | Italy | Live Equines | 5.0 |
| IT | Italy | Standard | 22.0 |
| LT | Lithuania | Medical Equipment | 5.0 |
| LT | Lithuania | Pharmaceutical Products | 5.0 |
| LT | Lithuania | Zero Reduced Rate | 9.0 |
| LT | Lithuania | Loan Libraries | 9.0 |
| LT | Lithuania | Supply Heating | 9.0 |
| LT | Lithuania | Transport Passengers | 9.0 |
| LT | Lithuania | Accommodation | 9.0 |
| LT | Lithuania | Newspapers | 5.0 |
| LT | Lithuania | Periodicals | 5.0 |
| LT | Lithuania | Supply Water | 9.0 |
| LT | Lithuania | Restaurant | 9.0 |
| LT | Lithuania | Writers Services | 9.0 |
| LT | Lithuania | Sporting Events | 9.0 |
| LT | Lithuania | Sporting Facilities | 9.0 |
| LT | Lithuania | Wood | 9.0 |
| LT | Lithuania | Standard | 21.0 |
| LU | Luxembourg | Foodstuffs | 3.0 |
| LU | Luxembourg | Agricultural Production | 8.0 |
| LU | Luxembourg | Pharmaceutical Products | 3.0 |
| LU | Luxembourg | Sporting Events | 0.0 |
| LU | Luxembourg | Transport Passengers | 0.0 |
| LU | Luxembourg | Zero Reduced Rate | 7.0 |
| LU | Luxembourg | Supply Water | 3.0 |
| LU | Luxembourg | Medical Equipment | 3.0 |
| LU | Luxembourg | Loan Libraries | 3.0 |
| LU | Luxembourg | Street Cleaning | 3.0 |
| LU | Luxembourg | Accommodation | 3.0 |
| LU | Luxembourg | Restaurant | 3.0 |
| LU | Luxembourg | Writers Services | 3.0 |
| LU | Luxembourg | Broadcasting Services | 3.0 |
| LU | Luxembourg | Cultural Events | 3.0 |
| LU | Luxembourg | Sporting Facilities | 3.0 |
| LU | Luxembourg | Undertakers Services | 3.0 |
| LU | Luxembourg | Supply Gas | 8.0 |
| LU | Luxembourg | Supply Electricity | 8.0 |
| LU | Luxembourg | Tapestries | 8.0 |
| LU | Luxembourg | Pictures | 8.0 |
| LU | Luxembourg | Impressions | 8.0 |
| LU | Luxembourg | Sculptures | 8.0 |
| LU | Luxembourg | Postage | 8.0 |
| LU | Luxembourg | Sculpture Casts | 8.0 |
| LU | Luxembourg | Zoological | 8.0 |
| LU | Luxembourg | 100 Years Old | 8.0 |
| LU | Luxembourg | Supply Heating | 8.0 |
| LU | Luxembourg | Window Cleaning | 8.0 |
| LU | Luxembourg | Shoes Repair | 8.0 |
| LU | Luxembourg | Clothing Repair | 8.0 |
| LU | Luxembourg | Bicycles Repair | 7.0 |
| LU | Luxembourg | Hairdressing | 8.0 |
| LU | Luxembourg | Ceramics | 8.0 |
| LU | Luxembourg | Enamels | 8.0 |
| LU | Luxembourg | Photographs | 8.0 |
| LU | Luxembourg | Parking | 13.0 |
| LU | Luxembourg | Super Temporary | 3.0 |
| LU | Luxembourg | Temporary | 8.0 |
| LU | Luxembourg | Child Wear | 3.0 |
| LU | Luxembourg | Exemption Superreduced | 3.0 |
| LU | Luxembourg | New Parking Rate | 14.0 |
| LU | Luxembourg | Wine Fresh Grape | 14.0 |
| LU | Luxembourg | Fuel Mineral Oil | 14.0 |
| LU | Luxembourg | Cleaning Product | 14.0 |
| LU | Luxembourg | Printed Advertising Material | 14.0 |
| LU | Luxembourg | Heat Cooling Steam | 14.0 |
| LU | Luxembourg | Credit Management | 14.0 |
| LU | Luxembourg | Security Management | 14.0 |
| LU | Luxembourg | Certain Agricultural Input | 3.0 |
| LU | Luxembourg | Plant | 8.0 |
| LU | Luxembourg | Waste Treatment | 3.0 |
| LU | Luxembourg | Waste Treatment Refusal | 3.0 |
| LU | Luxembourg | Solar Panels | 3.0 |
| LU | Luxembourg | Fossil Fuel | 8.0 |
| LU | Luxembourg | Chemical Pesticides Environment | 8.0 |
| LU | Luxembourg | Holiday Accommodation | 3.0 |
| LU | Luxembourg | Food Service | 3.0 |
| LU | Luxembourg | Royalties | 3.0 |
| LU | Luxembourg | Wood Article98 | 8.0 |
| LU | Luxembourg | Wood | 8.0 |
| LU | Luxembourg | Bicycles Electric | 8.0 |
| LU | Luxembourg | Bicycles Rental | 8.0 |
| LU | Luxembourg | Household | 8.0 |
| LU | Luxembourg | Greenhouse Gas | 14.0 |
| LU | Luxembourg | Certain Broadcasting Services | 3.0 |
| LU | Luxembourg | Sporting Facility Access | 3.0 |
| LU | Luxembourg | Funeral | 3.0 |
| LU | Luxembourg | Event Access | 3.0 |
| LU | Luxembourg | Residential Renovation | 3.0 |
| LU | Luxembourg | Non Owned Residency Renovation | 3.0 |
| LU | Luxembourg | Chemical Fertilisers | 3.0 |
| LU | Luxembourg | Housing Provision | 3.0 |
| LU | Luxembourg | Temporary Exemption Rate | 8.0 |
| LU | Luxembourg | Standard | 17.0 |
| LU | Luxembourg | Antiques | 8.0 |
| LV | Latvia | Foodstuffs | 12.0 |
| LV | Latvia | Pharmaceutical Products | 12.0 |
| LV | Latvia | Medical Equipment | 12.0 |
| LV | Latvia | Supply Heating | 12.0 |
| LV | Latvia | Periodicals | 5.0 |
| LV | Latvia | Loan Libraries | 5.0 |
| LV | Latvia | Newspapers | 5.0 |
| LV | Latvia | Transport Passengers | 12.0 |
| LV | Latvia | Accommodation | 12.0 |
| LV | Latvia | Medical Care | 0.0 |
| LV | Latvia | Social Wellbeing | 0.0 |
| LV | Latvia | Writers Services | 0.0 |
| LV | Latvia | Cultural Events | 0.0 |
| LV | Latvia | Sporting Events | 0.0 |
| LV | Latvia | Wood Article98 | 12.0 |
| LV | Latvia | Standard | 21.0 |
| MT | Malta | Pharmaceutical Products | 0.0 |
| MT | Malta | Transport Passengers | 0.0 |
| MT | Malta | Broadcasting Services | 0.0 |
| MT | Malta | Medical Care | 0.0 |
| MT | Malta | Supply Water | 0.0 |
| MT | Malta | Social Wellbeing | 0.0 |
| MT | Malta | Zero Reduced Rate | 0.0 |
| MT | Malta | Foodstuffs | 0.0 |
| MT | Malta | Housing Provision | 0.0 |
| MT | Malta | Supply Electricity | 5.0 |
| MT | Malta | Medical Equipment | 5.0 |
| MT | Malta | Periodicals | 5.0 |
| MT | Malta | Newspapers | 5.0 |
| MT | Malta | Loan Libraries | 5.0 |
| MT | Malta | Cultural Events | 5.0 |
| MT | Malta | Clothing Repair | 5.0 |
| MT | Malta | Impressions | 5.0 |
| MT | Malta | Sculpture Casts | 5.0 |
| MT | Malta | Enamels | 5.0 |
| MT | Malta | Postage | 5.0 |
| MT | Malta | 100 Years Old | 5.0 |
| MT | Malta | Domestic Care | 5.0 |
| MT | Malta | Bicycles Repair | 5.0 |
| MT | Malta | Shoes Repair | 5.0 |
| MT | Malta | Pictures | 5.0 |
| MT | Malta | Sculptures | 5.0 |
| MT | Malta | Tapestries | 5.0 |
| MT | Malta | Ceramics | 5.0 |
| MT | Malta | Photographs | 5.0 |
| MT | Malta | Zoological | 5.0 |
| MT | Malta | Accommodation | 7.0 |
| MT | Malta | Sporting Facilities | 7.0 |
| MT | Malta | Security Management | 12.0 |
| MT | Malta | Credit Management | 12.0 |
| MT | Malta | Hiring Short Period | 12.0 |
| MT | Malta | Body Care Services | 12.0 |
| MT | Malta | Standard | 18.0 |
| NL | Netherlands | Foodstuffs | 9.0 |
| NL | Netherlands | Writers Services | 9.0 |
| NL | Netherlands | Cultural Events | 9.0 |
| NL | Netherlands | Sporting Facilities | 9.0 |
| NL | Netherlands | Sporting Events | 9.0 |
| NL | Netherlands | Shoes Repair | 9.0 |
| NL | Netherlands | Clothing Repair | 9.0 |
| NL | Netherlands | Bicycles Repair | 9.0 |
| NL | Netherlands | Hairdressing | 9.0 |
| NL | Netherlands | Ceramics | 9.0 |
| NL | Netherlands | Enamels | 9.0 |
| NL | Netherlands | Photographs | 9.0 |
| NL | Netherlands | Tapestries | 9.0 |
| NL | Netherlands | Sculpture Casts | 9.0 |
| NL | Netherlands | Pharmaceutical Products | 9.0 |
| NL | Netherlands | Medical Equipment | 9.0 |
| NL | Netherlands | Zero Reduced Rate | 9.0 |
| NL | Netherlands | Zero Rate | 0.0 |
| NL | Netherlands | Supply Water | 9.0 |
| NL | Netherlands | Agricultural Production | 9.0 |
| NL | Netherlands | Transport Passengers | 9.0 |
| NL | Netherlands | Loan Libraries | 9.0 |
| NL | Netherlands | Newspapers | 9.0 |
| NL | Netherlands | Periodicals | 9.0 |
| NL | Netherlands | Private Dwellings | 9.0 |
| NL | Netherlands | Window Cleaning | 9.0 |
| NL | Netherlands | Accommodation | 9.0 |
| NL | Netherlands | Restaurant | 9.0 |
| NL | Netherlands | Pictures | 9.0 |
| NL | Netherlands | Impressions | 9.0 |
| NL | Netherlands | Sculptures | 9.0 |
| NL | Netherlands | Postage | 9.0 |
| NL | Netherlands | Zoological | 9.0 |
| NL | Netherlands | 100 Years Old | 9.0 |
| NL | Netherlands | Supply Heating | 9.0 |
| NL | Netherlands | Supply Gas | 9.0 |
| NL | Netherlands | Supply Electricity | 9.0 |
| NL | Netherlands | Antiques | 9.0 |
| NL | Netherlands | Solar Panels | 0.0 |
| NL | Netherlands | Live Equines | 9.0 |
| NL | Netherlands | Standard | 21.0 |
| NL | Netherlands | Plant | 9.0 |
| PL | Poland | Street Cleaning | 8.0 |
| PL | Poland | Transport Passengers | 8.0 |
| PL | Poland | Accommodation | 8.0 |
| PL | Poland | Agricultural Production | 8.0 |
| PL | Poland | Restaurant | 8.0 |
| PL | Poland | Loan Libraries | 5.0 |
| PL | Poland | Newspapers | 8.0 |
| PL | Poland | Sporting Facilities | 8.0 |
| PL | Poland | Shoes Repair | 8.0 |
| PL | Poland | Clothing Repair | 8.0 |
| PL | Poland | Bicycles Repair | 8.0 |
| PL | Poland | Hairdressing | 8.0 |
| PL | Poland | Undertakers Services | 8.0 |
| PL | Poland | Pharmaceutical Products | 5.0 |
| PL | Poland | Medical Equipment | 8.0 |
| PL | Poland | Cultural Events | 8.0 |
| PL | Poland | Broadcasting Services | 8.0 |
| PL | Poland | Writers Services | 8.0 |
| PL | Poland | Housing Provision | 8.0 |
| PL | Poland | Private Dwellings | 8.0 |
| PL | Poland | Sporting Events | 8.0 |
| PL | Poland | Zero Rate | 0.0 |
| PL | Poland | Foodstuffs | 5.0 |
| PL | Poland | Periodicals | 5.0 |
| PL | Poland | Children Car Seats | 5.0 |
| PL | Poland | Supply Water | 8.0 |
| PL | Poland | Photographs | 8.0 |
| PL | Poland | Tapestries | 8.0 |
| PL | Poland | Pictures | 8.0 |
| PL | Poland | Impressions | 8.0 |
| PL | Poland | Sculptures | 8.0 |
| PL | Poland | Sculpture Casts | 8.0 |
| PL | Poland | Postage | 8.0 |
| PL | Poland | Zoological | 8.0 |
| PL | Poland | 100 Years Old | 8.0 |
| PL | Poland | Temporary Exemption Rate | 8.0 |
| PL | Poland | Supply Gas | 0.0 |
| PL | Poland | Supply Electricity | 5.0 |
| PL | Poland | Supply Heating | 5.0 |
| PL | Poland | Standard | 23.0 |
| PT | Portugal | Foodstuffs | 6.0 |
| PT | Portugal | Agricultural Production | 6.0 |
| PT | Portugal | Street Cleaning | 6.0 |
| PT | Portugal | Housing Provision | 6.0 |
| PT | Portugal | Private Dwellings | 6.0 |
| PT | Portugal | Transport Passengers | 6.0 |
| PT | Portugal | Accommodation | 6.0 |
| PT | Portugal | Zero Reduced Rate | 6.0 |
| PT | Portugal | Tapestries | 6.0 |
| PT | Portugal | Pictures | 6.0 |
| PT | Portugal | Impressions | 6.0 |
| PT | Portugal | Medical Care | 6.0 |
| PT | Portugal | Domestic Care | 6.0 |
| PT | Portugal | Bicycles Repair | 6.0 |
| PT | Portugal | Sculpture Casts | 6.0 |
| PT | Portugal | Supply Water | 13.0 |
| PT | Portugal | Pharmaceutical Products | 6.0 |
| PT | Portugal | Medical Equipment | 6.0 |
| PT | Portugal | Loan Libraries | 6.0 |
| PT | Portugal | Sculptures | 6.0 |
| PT | Portugal | Ceramics | 6.0 |
| PT | Portugal | Enamels | 6.0 |
| PT | Portugal | Photographs | 6.0 |
| PT | Portugal | Parking | 13.0 |
| PT | Portugal | Region | 16.0 |
| PT | Portugal | Restaurant | 13.0 |
| PT | Portugal | Supply Gas | 6.0 |
| PT | Portugal | Supply Electricity | 6.0 |
| PT | Portugal | Sustainable Energy | 6.0 |
| PT | Portugal | Temporary Exemption Rate | 6.0 |
| PT | Portugal | New Parking Rate | 13.0 |
| PT | Portugal | Fossil Fuel | 13.0 |
| PT | Portugal | Standard | 23.0 |
| RO | Romania | Transport Passengers | 5.0 |
| RO | Romania | Accommodation | 11.0 |
| RO | Romania | Restaurant | 11.0 |
| RO | Romania | Foodstuffs | 11.0 |
| RO | Romania | Agricultural Production | 11.0 |
| RO | Romania | Pharmaceutical Products | 11.0 |
| RO | Romania | Medical Equipment | 0.0 |
| RO | Romania | Cultural Events | 11.0 |
| RO | Romania | Housing Provision | 11.0 |
| RO | Romania | Sporting Events | 9.0 |
| RO | Romania | Sporting Facilities | 5.0 |
| RO | Romania | Supply Water | 11.0 |
| RO | Romania | Loan Libraries | 11.0 |
| RO | Romania | Temporary | 5.0 |
| RO | Romania | Wood Article98 | 11.0 |
| RO | Romania | Private Dwellings | 0.0 |
| RO | Romania | Sustainable Energy | 11.0 |
| RO | Romania | Standard | 21.0 |
| SE | Sweden | Foodstuffs | 12.0 |
| SE | Sweden | Writers Services | 6.0 |
| SE | Sweden | Cultural Events | 6.0 |
| SE | Sweden | Loan Libraries | 6.0 |
| SE | Sweden | Sporting Events | 6.0 |
| SE | Sweden | Sporting Facilities | 6.0 |
| SE | Sweden | Transport Passengers | 6.0 |
| SE | Sweden | Broadcasting Services | 0.0 |
| SE | Sweden | Undertakers Services | 0.0 |
| SE | Sweden | Zero Rate | 0.0 |
| SE | Sweden | Zero Reduced Rate | 0.0 |
| SE | Sweden | Tapestries | 12.0 |
| SE | Sweden | Pictures | 12.0 |
| SE | Sweden | Impressions | 12.0 |
| SE | Sweden | Sculpture Casts | 12.0 |
| SE | Sweden | Sculptures | 12.0 |
| SE | Sweden | Newspapers | 6.0 |
| SE | Sweden | Periodicals | 6.0 |
| SE | Sweden | Restaurant | 12.0 |
| SE | Sweden | Accommodation | 12.0 |
| SE | Sweden | Postage | 12.0 |
| SE | Sweden | Zoological | 12.0 |
| SE | Sweden | 100 Years Old | 12.0 |
| SE | Sweden | Shoes Repair | 12.0 |
| SE | Sweden | Clothing Repair | 12.0 |
| SE | Sweden | Bicycles Repair | 12.0 |
| SE | Sweden | Medical Equipment | 6.0 |
| SE | Sweden | Standard | 25.0 |
| SI | Slovenia | Medical Equipment | 9.5 |
| SI | Slovenia | Foodstuffs | 9.5 |
| SI | Slovenia | Pharmaceutical Products | 9.5 |
| SI | Slovenia | Pictures | 9.5 |
| SI | Slovenia | Impressions | 9.5 |
| SI | Slovenia | Sculptures | 9.5 |
| SI | Slovenia | Sculpture Casts | 9.5 |
| SI | Slovenia | Postage | 9.5 |
| SI | Slovenia | Zoological | 9.5 |
| SI | Slovenia | 100 Years Old | 9.5 |
| SI | Slovenia | Agricultural Production | 9.5 |
| SI | Slovenia | Supply Water | 9.5 |
| SI | Slovenia | Street Cleaning | 9.5 |
| SI | Slovenia | Housing Provision | 9.5 |
| SI | Slovenia | Private Dwellings | 9.5 |
| SI | Slovenia | Transport Passengers | 9.5 |
| SI | Slovenia | Accommodation | 9.5 |
| SI | Slovenia | Restaurant | 9.5 |
| SI | Slovenia | Window Cleaning | 9.5 |
| SI | Slovenia | Domestic Care | 9.5 |
| SI | Slovenia | Cultural Events | 9.5 |
| SI | Slovenia | Writers Services | 9.5 |
| SI | Slovenia | Sporting Facilities | 9.5 |
| SI | Slovenia | Shoes Repair | 9.5 |
| SI | Slovenia | Clothing Repair | 9.5 |
| SI | Slovenia | Bicycles Repair | 9.5 |
| SI | Slovenia | Hairdressing | 9.5 |
| SI | Slovenia | Undertakers Services | 9.5 |
| SI | Slovenia | Sporting Events | 9.5 |
| SI | Slovenia | Ceramics | 9.5 |
| SI | Slovenia | Enamels | 9.5 |
| SI | Slovenia | Photographs | 9.5 |
| SI | Slovenia | Zero Reduced Rate | 9.5 |
| SI | Slovenia | Loan Libraries | 5.0 |
| SI | Slovenia | Tapestries | 9.5 |
| SI | Slovenia | Supply Heating | 9.5 |
| SI | Slovenia | Supply Gas | 9.5 |
| SI | Slovenia | Supply Electricity | 9.5 |
| SI | Slovenia | Rescue Equipment | 5.0 |
| SI | Slovenia | Plant | 9.5 |
| SI | Slovenia | Bicycles Rental | 9.5 |
| SI | Slovenia | Standard | 22.0 |
| SK | Slovakia | Newspapers | 5.0 |
| SK | Slovakia | Medical Equipment | 5.0 |
| SK | Slovakia | Accommodation | 5.0 |
| SK | Slovakia | Social Wellbeing | 5.0 |
| SK | Slovakia | Foodstuffs | 5.0 |
| SK | Slovakia | Housing Provision | 5.0 |
| SK | Slovakia | Pharmaceutical Products | 5.0 |
| SK | Slovakia | Supply Electricity | 19.0 |
| SK | Slovakia | Restaurant | 5.0 |
| SK | Slovakia | Sporting Facilities | 10.0 |
| SK | Slovakia | Cultural Events | 5.0 |
| SK | Slovakia | Admission Sporting Events | 5.0 |
| SK | Slovakia | Sporting Events | 5.0 |
| SK | Slovakia | Periodicals | 10.0 |
| SK | Slovakia | Standard | 23.0 |

### Notes

- TEDB is the authoritative EC source for VAT rates.
- Latest per category is selected by situationOn.
