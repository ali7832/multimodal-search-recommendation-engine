# ADR-001: Search Recommendation Service Layer

## Status

Accepted

## Context

Search and recommendation systems need operational metadata beyond ranked items. Product teams need request IDs, ranking strategy versions, latency, catalog health, and event traces to debug relevance and compare ranking changes.

## Decision

Introduce a `SearchRecommendationService` that owns catalog loading, indexing, recommendation execution, response envelopes, ranking metadata, latency measurement, health metadata, and event persistence.

## Consequences

Benefits:

- API routes remain thin and deployable.
- Every search and recommendation request can be traced by request ID.
- Ranking version metadata supports A/B testing and rollout reviews.
- JSONL events support local demo analytics and debugging.

Tradeoffs:

- TF-IDF and tag affinity are lightweight baselines.
- Production deployments should add embeddings, vector search, clickstream feedback, and learning-to-rank models.
