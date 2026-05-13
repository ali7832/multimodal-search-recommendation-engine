import typer
from rich.console import Console

from multimodal_search.index import SearchIndex
from multimodal_search.recommender import Recommender
from multimodal_search.sample_data import sample_catalog

app = typer.Typer(help='Multimodal search and recommendation CLI')
console = Console()


@app.command()
def search(query: str = 'wireless audio for travel') -> None:
    index = SearchIndex(sample_catalog())
    results = index.search(query)
    console.print_json(data=[item.model_dump() for item in results])


@app.command()
def recommend(item_id: str = 'item-001') -> None:
    recommender = Recommender(sample_catalog())
    results = recommender.recommend([item_id])
    console.print_json(data=[item.model_dump() for item in results])


@app.command()
def demo() -> None:
    search()
