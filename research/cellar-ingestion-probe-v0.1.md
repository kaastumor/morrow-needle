# Cellar ingestion probe v0.1

## Purpose

Test the P0 assumption that Cellar can serve as Needle's canonical large-scale ingestion backbone using official machine interfaces rather than presentation HTML.

## Official interface contract

The Publications Office documents:

- resource resolution by production-system identifier such as `/resource/celex/{CELEX}`;
- RDF/XML metadata notices;
- WEMI-style work/expression/manifestation structure;
- publication retrieval by language and MIME type;
- structured formats including FMX4.

Needle therefore tests the interface from the CELEX identifier outward rather than scraping EUR-Lex presentation pages.

## Controlled cases

### 32004R0794
A large, amendment-heavy 2004 implementing regulation.

EUR-Lex exposes:
- CELEX `32004R0794`;
- ELI `http://data.europa.eu/eli/reg/2004/794/oj`;
- Cellar work identifier `26f403d1-7656-4c91-9726-c08d466ff8bd` through its metadata-notice link;
- at least one direct Cellar content stream under that work.

### 31958R0001
Regulation No 1 determining the Community language regime.

EUR-Lex exposes:
- CELEX `31958R0001`;
- ELI `http://data.europa.eu/eli/reg/1958/1(1)/oj`;
- Cellar work identifier `115852e8-30ac-496e-8015-d580366ff059` through its metadata-notice link.

The awkward ELI suffix is another reason identifiers must be source-resolved rather than generated.

## Reproducible probe

`scripts/probe_cellar.py` requests for each CELEX work:

1. RDF tree metadata notice;
2. English XML branch notice;
3. English FMX4 content;
4. English XHTML content.

It records:
- HTTP status;
- content type;
- redirect chain;
- final resource URL;
- byte size;
- SHA-256;
- a small response prefix for diagnostics;
- observation timestamp.

The raw result is uploaded by GitHub Actions as `cellar-source-probe`.

## Why CI is part of the architecture

External source contracts can drift.

The source adapter therefore needs **contract tests against the live official source**, not just static parser unit tests. If Cellar changes MIME negotiation, redirects, or manifestation availability, Needle should detect that before silently ingesting the wrong representation.

## Provisional ingestion rule

```
CELEX
  ↓ official Cellar resolution
WORK
  ↓ metadata notice
EXPRESSIONS (language-scoped)
  ↓
MANIFESTATIONS (format-scoped)
  ↓
CONTENT STREAM(S)
  ↓ hash raw bytes
NORMALIZE
```

Presentation HTML is a fallback/debug surface, not a canonical ingestion dependency.

## Open questions the CI evidence should answer

- Does FMX4 resolve directly for both modern and early historical works?
- If not, which eras/forms require a different structured manifestation?
- Are notices stable enough to resolve language expressions deterministically?
- Are content streams single-file or multi-stream for complex acts?
- What metadata fields can be relied on for manifestation MIME/type selection?
