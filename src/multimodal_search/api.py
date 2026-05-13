from fastapi import FastAPI

from multimodal_search.index import SearchIndex
from multimodal_search.recommender import Recommender
from multimodal_search.sample_data import sample_catalog
from multimodal_search.schemas import RecommendationRequest, SearchRequest, SearchResult

app = FastAPI(title='Multimodal Search Recommendation Engine')
_items = sample_catalog()
_index = SearchIndex(_items)
_recommender = Recommender(_items)


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/search', response_model=list[SearchResult])
def search(request: SearchRequest) -> list[SearchResult]:
    return _index.search(request.query, top_k=request.top_k)


@app.post('/recommend', response_model=list[SearchResult])
def recommend(request: RecommendationRequest) -> list[SearchResult]:
    return _recommender.recommend(request.liked_item_ids, top_k=request.top_k)
