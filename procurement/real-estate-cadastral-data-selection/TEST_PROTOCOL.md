# Real-estate and Cadastral Data Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

## Sample

Use legally obtained public or owned test objects. Include land plots, buildings, premises, recently changed addresses, ambiguous addresses, missing cadastral identifiers and objects from several regions. Do not include restricted owner data unless the test has a documented legal basis.

## Measure

- identifier match and false-match rate;
- field completeness by object type;
- geometry availability and coordinate reference system;
- update delay against dated official evidence;
- partial, missing and contradictory responses;
- latency percentiles, timeout and retry behavior;
- cost per successful legally usable result;
- reproducibility and schema stability.

Record provider, method, timestamp, request class, response status and evidence reference. A map screenshot is not a substitute for an extract or structured response.

No Atlas benchmark result is claimed by this protocol.
