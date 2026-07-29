# Address and Geocoding API Selection Kit

[Русская версия](README.ru.md)

> Text-only procurement guidance for selecting address suggestions, cleaning, geocoding, place search and official registry integration.

## Purpose

Use this kit before buying or piloting an address/geocoding provider. It helps separate API capability, data rights, geography, quality, pricing and operational fit.

## Documents

| Document | Purpose |
|---|---|
| [`RFP.md`](RFP.md) | Questions to send to providers before commercial evaluation. |
| [`TEST_PROTOCOL.md`](TEST_PROTOCOL.md) | Reproducible benchmark protocol for address quality and geocoding tests. |
| [`SAMPLE_POLICY.md`](SAMPLE_POLICY.md) | Safe sample-data rules for testing without credentials, private addresses or personal data. |
| [`SCORING.md`](SCORING.md) | Scenario-weighted scorecard template; not a global Atlas Score. |
| [`NOMINATIM_SELF_HOSTING.md`](NOMINATIM_SELF_HOSTING.md) | Self-hosting operations checklist for Nominatim/OSM geocoding. |

## Provider-Specific Requests

Use these checklists after the general RFP when a provider reaches the shortlist. They are questions, not provider answers.

| Provider / scope | Checklist |
|---|---|
| DaData address suggestions, cleaning and geocoding | [`provider-request-dadata-address.md`](../../research/address-geocoding/provider-request-dadata-address.md) |
| Yandex Maps Geosuggest and Geocoder | [`provider-request-yandex-maps.md`](../../research/address-geocoding/provider-request-yandex-maps.md) |
| 2GIS Suggest, Places and Geocoder | [`provider-request-2gis-search.md`](../../research/address-geocoding/provider-request-2gis-search.md) |

## Related Atlas Materials

- Need route: [`Address Normalization, Address Registries and Geocoding`](../../needs/address-normalization-geocoding/README.md)
- Comparison: [`Address Normalization, Address Registries and Geocoding APIs`](../../comparisons/address-normalization-geocoding/README.md)
- Profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md), [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md), [`2GIS Places API`](../../apis/2gis-places-api/README.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md), [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md)

## Use Sequence

1. Pick the primary scenario from the need route.
2. Send the RFP questions to shortlisted providers.
3. Agree on a legal, reproducible test sample.
4. Run the test protocol with provider-approved credentials.
5. Fill the scorecard with evidence and unresolved risks.

No real benchmark results are included in this kit.
