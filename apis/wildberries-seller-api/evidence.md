# Evidence: Wildberries Seller API

[Русская версия](evidence.ru.md)

## Confirmed from official documentation

- Wildberries documents a seller API for integrating seller operations with external business systems.
- The API is exposed through REST/HTTP service categories and the official documentation is available in Swagger/OpenAPI format.
- Seller access requires an account and an API token; token categories and permissions control access to service groups.
- An official test environment is documented for supported scopes and uses generated test data rather than real seller data.
- The official documentation gives method-level limit examples, including `ping` and seller information. These examples do not establish a universal quota for every method.

## Not confirmed

- API-specific price, SLA and support commitments.
- Complete method and field coverage for a particular seller account.
- Storage, SaaS, redistribution and customer-facing display rights.
- Live request success: no credentials were used.

## Sources

- [Official API information](https://dev.wildberries.ru/en/docs/openapi/api-information)
- [Official Russian API information](https://dev.wildberries.ru/docs/openapi/api-information)
- [Official token connection guidance](https://dev.wildberries.ru/knowledge-base/articles/019d49a0-f9f7-79a4-b5ee-df5dabe9cff4)
- [Official sandbox documentation](https://dev.wildberries.ru/en/openapi-other/sandbox-environment)
