from __future__ import annotations

import time
from uuid import uuid4

from multimodal_search.config import settings
from multimodal_search.events import append_search_event
from multimodal_search.index import SearchIndex
from multimodal_search.recommender import Recommender
from multimodal_search.sample_data import sample_catalog
from multimodal_search.schemas import (
    HealthResponse,
    RecommendationRequest,
    RecommendationResponse,
    SearchRequest,
    SearchResponse,
    SearchResult,
)


class SearchRecommendationService:
    def __init__(self) -> None:
        self.items = sample_catalog()
        self.index = SearchIndex(self.items)
        self.recommender = Recommender(self.items)

    def health(self) -> HealthResponse:
        return HealthResponse(
            status='ok',
            service_name=settings.service_name,
            environment=settings.environment,
            ranking_version=settings.ranking_version,
            catalog_size=len(self.items),
        )

    def search(self, request: SearchRequest) -> SearchResponse:
        started = time.perf_counter()
        request_id = str(uuid4())
        top_k = min(request.top_k, settings.max_top_k)
        results = self._ranked(self.index.search(request.query, top_k=top_k))
        latency_ms = round((time.perf_counter() - started) * 1000, 2)
        response = SearchResponse(
            request_id=request_id,
            query=request.query,
            results=results,
            ranking_version=settings.ranking_version,
            latency_ms=latency_ms,
        )
        self._record_event('search_completed', request_id, request.model_dump(), response.model_dump())
        return response

    def recommend(self, request: RecommendationRequest) -> RecommendationResponse:
        started = time.perf_counter()
        request_id = str(uuid4())
        top_k = min(request.top_k, settings.max_top_k)
        results = self._ranked(self.recommender.recommend(request.liked_item_ids, top_k=top_k))
        latency_ms = round((time.perf_counter() - started) * 1000, 2)
        response = RecommendationResponse(
            request_id=request_id,
            liked_item_ids=request.liked_item_ids,
            results=results,
            ranking_version=settings.ranking_version,
            latency_ms=latency_ms,
        )
        self._record_event('recommendation_completed', request_id, request.model_dump(), response.model_dump())
        return response

    @staticmethod
    def _ranked(results: list[SearchResult]) -> list[SearchResult]:
        ranked = []
        for index, result in enumerate(results, start=1):
            ranked.append(result.model_copy(update={'rank': index}))
        return ranked

    @staticmethod
    def _record_event(event_type: str, request_id: str, request: dict, response: dict) -> None:
        append_search_event(
            {
                'event_type': event_type,
                'request_id': request_id,
                'request': request,
                'response': response,
            },
            settings.event_store_path,
        )
