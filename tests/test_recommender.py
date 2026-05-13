from multimodal_search.recommender import Recommender
from multimodal_search.sample_data import sample_catalog


def test_recommender_returns_related_items():
    recommender = Recommender(sample_catalog())
    results = recommender.recommend(['item-001'], top_k=3)

    assert results
    assert all(item.item_id != 'item-001' for item in results)
