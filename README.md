# Multimodal Search Recommendation Engine

Deployable product discovery service for catalog search and recommendations. It returns ranked results with request IDs, ranking version metadata, latency measurements, event traces for search quality review, and a premium React discovery operations dashboard.

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
- Multi-page React/Vite multimodal discovery frontend

## Quickstart

```bash
pip install .[dev]
mmsearch demo
uvicorn multimodal_search.api:app --reload
pytest -q
```

## Frontend DiscoveryAI Dashboard

The `frontend/` directory contains a premium React/Vite command center for multimodal search, personalized recommendations, ranking quality, and discovery analytics.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

Frontend pages:

- Overview: search KPIs, CTR/latency trends, and query modality mix
- Search Studio: interactive text/hybrid catalog search with ranked results
- Recommendations: personalized recommendation context and ranked carousel-style results
- Embedding Explorer: visual similarity-space explorer for catalog items
- Ranking Controls: ranking weights, metadata filters, and business guardrails
- Personalization: user affinity profiles and next-best recommendation examples
- Analytics: CTR lift, conversion insights, and latency performance
- Evaluation: ranking experiment table with NDCG, recall, CTR lift, and winner flags

The UI attempts to call `/search` and `/recommend` and falls back to demo discovery intelligence when the backend is offline.

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
