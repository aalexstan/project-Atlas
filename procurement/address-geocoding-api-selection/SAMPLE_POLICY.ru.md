# Политика тестовой выборки адресов

[English version](SAMPLE_POLICY.md)

## Разрешённые источники

Используйте только:

- synthetic addresses, созданные для тестирования;
- public government или open-data examples, которые законно использовать;
- provider-approved sample rows;
- internal customer data только после legal approval, DPA coverage и documented deletion rules.

## Запрещённые данные

Не включайте:

- домашние адреса, связанные с identifiable individuals;
- customer addresses из production systems без approval;
- credentials, cookies или access tokens;
- payment, passport, phone или email data;
- данные, license которых запрещает testing или publication.

## Правила публикации

- Публикуйте только aggregate benchmark metrics, если каждая raw row не разрешена к публикации.
- Храните raw provider responses приватно, если contract не разрешает publication.
- Маскируйте или удаляйте coordinates, если они раскрывают sensitive places.
- Записывайте sample origin, license, date и transformation steps.

## Минимальные metadata sample

| Поле | Значение |
|---|---|
| `sample_id` | Stable internal row identifier. |
| `source_type` | `synthetic`, `public`, `provider_sample` или `internal_approved`. |
| `country` | Country code. |
| `region` | Region or subject. |
| `scenario` | Suggestions, cleaning, direct geocoding, reverse geocoding, batch. |
| `expected_level` | House, street, locality или unknown. |
| `allowed_to_publish` | Boolean with evidence. |

## Retention

Удаляйте provider responses и temporary files по самому строгому применимому provider contract, DPA и internal policy.
