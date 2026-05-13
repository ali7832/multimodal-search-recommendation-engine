# Operations Runbook

## Purpose

This service powers catalog search and recommendations for product discovery workflows. It returns ranked results with request IDs, ranking version, latency, and explanation metadata.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `MMSEARCH_ENV`: deployment environment.
- `MMSEARCH_SERVICE_NAME`: service identifier.
- `MMSEARCH_RANKING_VERSION`: ranking strategy version.
- `MMSEARCH_DEFAULT_TOP_K`: default result count.
- `MMSEARCH_MAX_TOP_K`: maximum result count.
- `MMSEARCH_EVENT_STORE_PATH`: JSONL search/recommendation event path.

## Search Lifecycle

1. Client submits a query to `/search`.
2. Service creates a request ID.
3. Catalog index ranks items by text and metadata similarity.
4. Results are returned with rank, score, reason, and ranking version.
5. Search event is written to JSONL storage.

## Recommendation Lifecycle

1. Client submits liked item IDs to `/recommend`.
2. Service infers tag and category affinity.
3. Ranked recommendations are returned with score and reason.
4. Recommendation event is written to JSONL storage.

## Demo Readiness

Expose `/health`, `/search`, and `/recommend`. Health returns service name, environment, ranking version, and catalog size.

## Production Roadmap

- Replace static sample catalog with database-backed ingestion.
- Add vector database support.
- Add image embeddings through multimodal encoders.
- Add personalized user profiles.
- Add clickstream feedback loops.
- Add A/B testing for ranking strategies.
- Add dashboards for search quality and conversion metrics.
