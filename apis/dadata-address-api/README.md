# DaData Address APIs

[Русская версия](README.ru.md)

> Address suggestions, address cleaning, direct geocoding and reverse geocoding from DaData, scoped separately from DaData company data.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | DaData / LLC Data Q |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** Russian web forms, CRM/ERP address entry, backend standardization of Russian address records, and address-to-coordinate workflows where DaData's FIAS/GAR/KLADR enrichment is useful.

**Avoid when:** you need a full official address registry copy, global house-level standardization, routing, or unattended batch processing through Suggestions.

**Bottom line:** DaData is the strongest first candidate for Russian address autocomplete and a practical candidate for cleaning and geocoding. The main procurement trap is endpoint mix: Suggestions, reverse geocoding, address cleaning and direct geocoding are billed and limited differently.

## Product Boundary

This profile is separate from [`DaData API`](../dadata/README.md). The existing profile remains the provider-wide and company/counterparty reference. This profile covers:

- address suggestions;
- address cleaning and standardization;
- direct geocoding through address cleaning;
- reverse geocoding by coordinates;
- FIAS/GAR, KLADR and postal enrichment where documented.

Company autocomplete, company lookup, party enrichment and counterparty screening remain outside this profile.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Address suggestions in B2C/B2B forms | Strong | Official docs confirm interactive suggestions by address fragments, postal code, typo correction and granular parts. |
| Russian CRM/ERP address normalization | Strong | Cleaning API splits fields, calculates postal code, returns coordinates and registry identifiers. |
| Direct geocoding in Russia | Strong | Official direct geocoding page uses the address cleaning endpoint. |
| Reverse geocoding in Russia | Strong | Official reverse geocoding endpoint returns nearby houses, streets and cities by coordinates. |
| Bulk address file processing | Medium | Cleaning is the right API family, but public docs show one address per request. |
| Global address validation | Weak | Detailed cleaning/geocoding is Russia-only; Suggestions outside key countries is shallower. |
| Routing or distance calculation | Not applicable | DaData address APIs are not routing APIs. |

## Technical Access

| Field | Address Suggestions | Cleaning / Direct Geocoding | Reverse Geocoding |
|---|---|---|---|
| Protocol | HTTP JSON | HTTP JSON | HTTP JSON |
| Method | POST | POST | POST |
| Base endpoint | `https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address` | `https://cleaner.dadata.ru/api/v1/clean/address` | `https://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/address` |
| Authentication | API token | API token plus secret key | API token |
| Browser use | Supported for suggestions | Not supported because secret key would be exposed | Backend or controlled client use should be reviewed |
| Format | JSON / UTF-8 | JSON / UTF-8 | JSON / UTF-8 |
| OpenAPI | Provider-published API-family schemas; endpoint scope needs recheck | Provider-published API-family schemas; endpoint scope needs recheck | Provider-published API-family schemas; endpoint scope needs recheck |

## Limits and Pricing

| Item | Confirmed value | Status |
|---|---|---|
| Free tier | 10,000 subscription-service requests/day after registration | verified |
| Suggestions rate limit | 30 requests/second per IP | verified |
| Suggestions query limit | 300 characters | verified |
| Cleaning rate limit | 20 requests/second per IP | verified |
| Cleaning payload | One address per request | verified |
| New connections | 60/minute per IP for Suggestions and Cleaning | verified |
| Address cleaning | 0.20 RUB per address | verified |
| Direct geocoding | 0.20 RUB per address | verified |
| Reverse geocoding | Subscription address service | verified |
| SLA | Unknown in public docs reviewed | unknown |

## Commercial and Legal Notes

- Suggestions are intended for human-assisted entry; DaData documentation says they are not for automatic processing of address files or databases.
- Cleaning and direct geocoding use a secret key and must not be called from browser JavaScript.
- The provider reports that API-processed cleaning data is not stored, while file uploads are stored temporarily.
- Storage, caching, redistribution, resale and SaaS embedding must be confirmed against the exact contract.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Direct/reverse geocoding tied to Yandex maps and international map coverage | Not a normalization API; display/storage restrictions matter. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | Geocoding connected to the 2GIS map/catalog ecosystem | Organization search and suggestions are separate products; caching restrictions need review. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | Building a proprietary Russian address registry/search system | Requires ETL, indexing and quality logic; not a turnkey suggestions API. |

## Scenario-Based Recommendation

Choose DaData first for Russian address forms and for backend standardization when public pricing and fast onboarding matter. Test alternatives when map-display coupling, international geocoding, official-registry provenance or strict data-storage rights dominate the decision.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).
