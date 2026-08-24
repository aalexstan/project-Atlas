# Доказательства Open-Meteo

[English version](evidence.md)

| Утверждение | Источник | Статус |
|---|---|---|
| Free tier некоммерческий и ограничен | https://open-meteo.com/en/pricing | verified |
| Commercial customer endpoint документирован | https://open-meteo.com/en/pricing | verified |
| Weather data CC BY 4.0 и server code AGPLv3 | https://open-meteo.com/en/pricing | provider_reported |

В [записи публичного live test](../../research/open-meteo-api/live-test-2026-08-24.ru.md) сохранены сырые payload, latency, коды статусов и findings. Тест подтвердил протестированные формы forecast, archive и geocoding, а также JSON-ошибку для некорректного ввода. Дневная квота и коммерческие права не измерялись.
