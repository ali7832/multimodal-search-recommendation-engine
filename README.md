# Multimodal Search Recommendation Engine

Production-ready search and recommendation platform for catalog items with text metadata, image metadata, tagging, similarity search, and personalized recommendations.

## Features

- Catalog item schema with text, tags, category, and image metadata
- TF-IDF text indexing baseline
- Similarity search
- Tag/category-aware recommendations
- FastAPI search and recommendation API
- CLI workflows for demo, search, and recommendation
- JSON search and recommendation examples
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite
- Architecture and deployment documentation

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

## Docs

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `sample_query.json`
- `sample_recommendation.json`

## Portfolio Highlights

- Demonstrates retrieval, recommendation systems, APIs, and production engineering
- Useful for ecommerce, media search, product discovery, and personalized content systems
- Strong foundation for vector databases, embeddings, multimodal encoders, ranking models, personalization, and A/B testing
