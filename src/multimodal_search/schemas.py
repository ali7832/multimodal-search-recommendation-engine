from __future__ import annotations

from pydantic import BaseModel


class CatalogItem(BaseModel):
    item_id: str
    title: str
    description: str
    category: str
    tags: list[str] = []
    image_url: str | None = None


class SearchRequest(BaseModel):
    query: str
    top_k: int = 3


class SearchResult(BaseModel):
    item_id: str
    title: str
    category: str
    score: float
    reason: str


class RecommendationRequest(BaseModel):
    liked_item_ids: list[str]
    top_k: int = 3
