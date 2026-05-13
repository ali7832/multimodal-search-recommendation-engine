from __future__ import annotations

from collections import Counter

from multimodal_search.schemas import CatalogItem, SearchResult


class Recommender:
    def __init__(self, items: list[CatalogItem]) -> None:
        self.items = items
        self.by_id = {item.item_id: item for item in items}

    def recommend(self, liked_item_ids: list[str], top_k: int = 3) -> list[SearchResult]:
        liked = [self.by_id[item_id] for item_id in liked_item_ids if item_id in self.by_id]
        if not liked:
            return []

        tag_counts = Counter(tag for item in liked for tag in item.tags)
        category_counts = Counter(item.category for item in liked)
        liked_ids = {item.item_id for item in liked}
        scored = []

        for item in self.items:
            if item.item_id in liked_ids:
                continue
            score = sum(tag_counts[tag] for tag in item.tags) + category_counts[item.category]
            scored.append((item, score))

        ranked = sorted(scored, key=lambda row: row[1], reverse=True)[:top_k]
        return [
            SearchResult(
                item_id=item.item_id,
                title=item.title,
                category=item.category,
                score=round(float(score), 4),
                reason='shared category and tag affinity',
            )
            for item, score in ranked
            if score > 0
        ]
