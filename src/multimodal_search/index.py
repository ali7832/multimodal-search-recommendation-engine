from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from multimodal_search.schemas import CatalogItem, SearchResult


def item_text(item: CatalogItem) -> str:
    return ' '.join([item.title, item.description, item.category, ' '.join(item.tags)])


class SearchIndex:
    def __init__(self, items: list[CatalogItem]) -> None:
        self.items = items
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.matrix = self.vectorizer.fit_transform([item_text(item) for item in items]) if items else None

    def search(self, query: str, top_k: int = 3) -> list[SearchResult]:
        if not self.items or self.matrix is None:
            return []
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix)[0]
        ranked = sorted(enumerate(scores), key=lambda row: row[1], reverse=True)[:top_k]
        return [
            SearchResult(
                item_id=self.items[index].item_id,
                title=self.items[index].title,
                category=self.items[index].category,
                score=round(float(score), 4),
                reason='text and metadata similarity',
            )
            for index, score in ranked
        ]
