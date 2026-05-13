from multimodal_search.index import SearchIndex
from multimodal_search.sample_data import sample_catalog


def test_search_returns_relevant_results():
    index = SearchIndex(sample_catalog())
    results = index.search('wireless headphones audio', top_k=2)

    assert results
    assert results[0].item_id == 'item-001'
    assert results[0].score >= 0
