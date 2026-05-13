from fastapi import FastAPI

from multimodal_search.schemas import (
    HealthResponse,
    RecommendationRequest,
    RecommendationResponse,
    SearchRequest,
    SearchResponse,
)
from multimodal_search.service import SearchRecommendationService

app = FastAPI(title='Multimodal Search Recommendation Engine', version='0.2.0')
_service = SearchRecommendationService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return _service.health()


@app.post('/search', response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return _service.search(request)


@app.post('/recommend', response_model=RecommendationResponse)
def recommend(request: RecommendationRequest) -> RecommendationResponse:
    return _service.recommend(request)
