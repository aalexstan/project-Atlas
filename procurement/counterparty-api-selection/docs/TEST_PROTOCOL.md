# Comparative Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

## Goal

Evaluate providers on one frozen sample, under identical rules and mandatory-field requirements.

## Preparation

1. Complete **Test Cases**.
2. Confirm lawful use of identifiers.
3. Freeze the sample before testing.
4. Record plan, API version, and date.
5. Synchronize system clocks.
6. Stay within authorized limits.

## Execution

Run every test at least three times:

- cold single request;
- repeated request;
- request inside a controlled series.

For batch operations test:

- fully valid batch;
- one invalid identifier;
- mixed batch;
- exact retry of the batch.

## Measurements

Record:

- complete HTTP or delivery status;
- end-to-end latency;
- result count;
- mandatory-field completion;
- match accuracy;
- freshness;
- error quality;
- observed cost;
- raw evidence link.

## Scoring Rules

### Required Fields %

Completed mandatory fields divided by applicable mandatory fields.

`null`, missing, and explicit “not found” must remain distinct.

### Match Accuracy 0–5

- 0 — wrong entity;
- 1 — mostly incorrect;
- 2 — material errors;
- 3 — usable with manual review;
- 4 — correct with minor caveats;
- 5 — correct and unambiguous.

### Freshness 0–5

Score only against a fact verifiable from a primary source on the test date.

## Prohibited

- changing the sample after seeing early results;
- treating missing fields as zero;
- comparing different plans without disclosure;
- hiding errors;
- using confidential data;
- exceeding authorized load.
