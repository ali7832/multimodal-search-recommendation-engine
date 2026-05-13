# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn multimodal_search.api:app --reload
```

## CLI Demo

```bash
mmsearch demo
mmsearch search "wireless audio"
mmsearch recommend item-001
```

## Docker

```bash
docker build -t multimodal-search .
docker run -p 8000:8000 multimodal-search
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Search Endpoint

```bash
curl -X POST http://localhost:8000/search \
  -H 'Content-Type: application/json' \
  -d @sample_query.json
```

## Recommendation Endpoint

```bash
curl -X POST http://localhost:8000/recommend \
  -H 'Content-Type: application/json' \
  -d @sample_recommendation.json
```
