# Project Atlas

Project Atlas is a research knowledge base about available datasets, data providers, access methods, catalogs, APIs, and practical ways to obtain information.

The project does not generate startup ideas or product concepts. Its purpose is to understand data first: what exists, who owns it, who collects it, who distributes it, how it can be accessed, what legal and technical limits apply, and whether the dataset is reliable enough for long-term use.

## Core Model

The main entity of Project Atlas is the Dataset.

An API is not the main entity. An API is only one possible access method for a Dataset.

The project now answers the question:

`What data exists?`

not only:

`What APIs exist?`

## Architectural Changes

Pass #1 organized the project around API cards. That was useful for discovery, but it made the API look more important than the data itself.

Pass #2 refactored the knowledge base around datasets:

- `datasets/` - primary cards for concrete datasets.
- `providers/` - organizations and systems as data providers, aggregators, owners, sellers, or distributors.
- `access_methods/` - ways to obtain each dataset, including REST API, Open Data, CSV, XML, FTP, Webhook, partnership, parsing, and other methods.
- `relationships/` - graphs connecting Dataset -> Provider -> Access Method -> Documentation -> Cost -> License -> Alternatives.

Legacy folders remain:

- `catalog/` - historical API-centric cards from Pass #1.
- `companies/` - historical company cards from Pass #1.

They are not deleted because they preserve provenance and source notes.

## Research Principles

- Use official sources first when available.
- Never invent missing facts.
- Mark every uncertain item as `не найдено`, `неизвестно`, or `требует проверки`.
- Separate confirmed facts from assumptions.
- Record ownership, collection, distribution, licensing, pricing, technical access, and data provenance for each dataset.
- Keep every file structured so a human researcher can continue the work.

## Project Structure

- `datasets/` - primary dataset cards.
- `providers/` - data provider cards.
- `access_methods/` - dataset access-method cards.
- `relationships/` - graph and relationship maps.
- `catalog/` - legacy API/source cards from Pass #1.
- `companies/` - legacy company cards from Pass #1.
- `industries/` - industry and category coverage maps.
- `research/` - focused investigations.
- `reports/` - report for each research run.
- `ratings/` - comparative scoring tables.
- `templates/` - reusable card templates.

## Initial Research Route

The first source is API Portal:

- https://apiportal.ru/catalog/

After API Portal coverage expands, the research should move dataset by dataset to official provider sites, official documentation, Swagger/OpenAPI specifications, GitHub organizations, government open data portals, primary registries, and other official data catalogs.
# project-Atlas
