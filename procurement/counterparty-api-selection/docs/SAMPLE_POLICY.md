# Evaluation-Sample Policy

[Русская версия](SAMPLE_POLICY.ru.md)

## Goal

The sample should reveal provider differences rather than confirm a preferred conclusion.

## Composition

Recommended cases:

- active large legal entity;
- branch;
- sole proprietor;
- liquidation;
- reorganization;
- bankruptcy;
- recent address change;
- missing financial statements;
- court and enforcement history;
- procurement and unreliable-supplier registry;
- CIS or another target market;
- ambiguous name search;
- invalid identifier;
- batch with partial failure.

## Safety

Allowed:

- public organization identifiers;
- identifiers from official documentation;
- synthetic invalid values.

Do not include without a separate lawful basis:

- customer databases;
- personal identifiers;
- confidential investigations;
- NDA-protected data.

## Freeze Rule

Before the first comparative run:

1. complete mandatory rows;
2. record the date;
3. define expected checks;
4. prohibit replacing inconvenient cases after results arrive.
