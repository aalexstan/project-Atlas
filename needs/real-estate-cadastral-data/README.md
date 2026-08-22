# Choosing a Real-estate or Cadastral Data Source

[Русская версия](README.ru.md)

## Start With the Output

| Your task | Start with | Do not confuse it with |
|---|---|---|
| Prove official registry facts | EGRN extract | Cadastral map or enrichment response |
| Request many official extracts | FGIS EGRN package access | Undocumented scraping |
| Explore boundaries and spatial context | NSPD | Legally significant extract |
| Normalize an address and obtain cadastral enrichment | DaData Address API | Property-right verification |
| Build an internal Russian address base | FIAS/GAR | EGRN ownership/encumbrance data |

## Questions Before Implementation

1. Must the output be legally significant?
2. Do you need an address, cadastral identifier, geometry, characteristics, ownership or encumbrance information?
3. Are you requesting one object, a recurring portfolio or a bulk dataset?
4. Can the result be stored and shown to customers?
5. Is automated decision-making involved?
6. What happens when an official source is delayed or unavailable?

## Current Limits

Atlas has not confirmed a public unattended Rosreestr REST API, current package pricing, quotas, SLA or commercial reuse rights. No live request or paid extract was performed.

## Next Step

Read the [scenario comparison](../../comparisons/real-estate-cadastral-data/README.md), choose the required legal output, then use the [procurement checklist](../../procurement/real-estate-cadastral-data-selection/README.md).
