# Multimodal Search Recommendation Engine

Deployable product discovery service for catalog search and recommendations. It returns ranked results with request IDs, ranking version metadata, latency measurements, and event traces for search quality review.

## Core Capabilities

- Catalog item schema with text, tags, category, image metadata, tenant, and active status
- TF-IDF text and metadata search baseline
- Tag/category affinity recommendation baseline
- Search request IDs for traceability
- Recommendation request IDs for traceability
- Ranking version metadata in every response
- Latency measurement for search and recommendation calls
- Result ranking, scores, and explanation reasons
- JSONL event stream for local search/recommendation analytics
- FastAPI `/search` and `/recommend` APIs
- CLI workflows for demo, search, and recommendation
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
mmsearch demo
uvicorn multimodal_search.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/search \
  -H 'Content-Type: application/json' \
  -d @sample_query.json
curl -X POST http://localhost:8000/recommend \
  -H 'Content-Type: application/json' \
  -d @sample_recommendation.json
```

## Docker

```bash
docker-compose up --build
```

## Runtime Configuration

See `.env.example` for environment, ranking version, result limits, and event stream path.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-search-recommendation-service.md`
- `sample_query.json`
- `sample_recommendation.json`

## Production Roadmap

- Database-backed catalog ingestion
- Vector database support
- Image embeddings with multimodal encoders
- Personalized user profiles
- Clickstream feedback loops
- A/B testing for ranking strategies
- Search quality and conversion dashboards
