# Address Test Sample Policy

[Русская версия](SAMPLE_POLICY.ru.md)

## Allowed Sources

Use only:

- synthetic addresses created for testing;
- public government or open-data examples that are lawful to reuse;
- provider-approved sample rows;
- internal customer data only after legal approval, DPA coverage and documented deletion rules.

## Prohibited Data

Do not include:

- personal home addresses connected to identifiable individuals;
- customer addresses from production systems without approval;
- credentials, cookies or access tokens;
- payment, passport, phone or email data;
- any data whose license prohibits testing or publication.

## Publication Rules

- Publish only aggregate benchmark metrics unless every raw row is cleared for publication.
- Keep raw provider responses private unless the contract allows publication.
- Mask or remove coordinates if they reveal sensitive places.
- Record sample origin, license, date and transformation steps.

## Minimum Sample Metadata

| Field | Meaning |
|---|---|
| `sample_id` | Stable internal row identifier. |
| `source_type` | `synthetic`, `public`, `provider_sample`, or `internal_approved`. |
| `country` | Country code. |
| `region` | Region or subject. |
| `scenario` | Suggestions, cleaning, direct geocoding, reverse geocoding, batch. |
| `expected_level` | House, street, locality, or unknown. |
| `allowed_to_publish` | Boolean with evidence. |

## Retention

Delete provider responses and temporary files according to the strictest applicable provider contract, DPA and internal policy.
