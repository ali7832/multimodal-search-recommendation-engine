from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class SearchSettings:
    environment: str = os.getenv('MMSEARCH_ENV', 'local')
    service_name: str = os.getenv('MMSEARCH_SERVICE_NAME', 'multimodal-search-recommendation-engine')
    ranking_version: str = os.getenv('MMSEARCH_RANKING_VERSION', 'tfidf-affinity-v1')
    default_top_k: int = int(os.getenv('MMSEARCH_DEFAULT_TOP_K', '3'))
    max_top_k: int = int(os.getenv('MMSEARCH_MAX_TOP_K', '20'))
    event_store_path: str = os.getenv('MMSEARCH_EVENT_STORE_PATH', 'search_events.jsonl')


settings = SearchSettings()
