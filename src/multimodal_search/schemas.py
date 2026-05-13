from __future__ import annotations

from pydantic import BaseModel, Field


class CatalogItem(BaseModel):
    item_id: str
    title: str
    description: str
    category: str
    tags: list[str] = []
    image_url: str | None = None
    tenant_id: str = 'default'
    active: bool = True


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=3, ge=1, le=20)
    user_id: str | None = None
    session_id: str | None = None
    tenant_id: str = 'default'


class SearchResult(BaseModel):
    item_id: str
    title: str
    category: str
    score: float
    reason: str
    rank: int | None = None


class RecommendationRequest(BaseModel):
    liked_item_ids: list[str]
    top_k: int = Field(default=3, ge=1, le=20)
    user_id: str | None = None
    session_id: str | None = None
    tenant_id: str = 'default'


class SearchResponse(BaseModel):
    request_id: str
    query: str
    results: list[SearchResult]
    ranking_version: str
    latency_ms: float


class RecommendationResponse(BaseModel):
    request_id: str
    liked_item_ids: list[str]
    results: list[SearchResult]
    ranking_version: str
    latency_ms: float


class HealthResponse(BaseModel):
    status: str
    service_name: str
    environment: str
    ranking_version: str
    catalog_size: int
