from multimodal_search.schemas import RecommendationRequest, SearchRequest
from multimodal_search.service import SearchRecommendationService


def test_search_service_returns_request_metadata():
    service = SearchRecommendationService()
    response = service.search(SearchRequest(query='wireless headphones audio', user_id='user_001'))

    assert response.request_id
    assert response.ranking_version
    assert response.latency_ms >= 0
    assert response.results
    assert response.results[0].rank == 1


def test_recommendation_service_returns_ranked_results():
    service = SearchRecommendationService()
    response = service.recommend(RecommendationRequest(liked_item_ids=['item-001'], user_id='user_001'))

    assert response.request_id
    assert response.ranking_version
    assert response.latency_ms >= 0
    assert response.results
    assert response.results[0].rank == 1


def test_search_service_health_metadata():
    health = SearchRecommendationService().health()

    assert health.status == 'ok'
    assert health.catalog_size > 0
    assert health.ranking_version
