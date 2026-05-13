from multimodal_search.schemas import CatalogItem


def sample_catalog() -> list[CatalogItem]:
    return [
        CatalogItem(
            item_id='item-001',
            title='Wireless Noise Cancelling Headphones',
            description='Premium headphones with active noise cancellation and long battery life.',
            category='electronics',
            tags=['audio', 'wireless', 'travel'],
            image_url='https://example.com/headphones.jpg',
        ),
        CatalogItem(
            item_id='item-002',
            title='Running Shoes',
            description='Lightweight athletic shoes designed for road running and daily training.',
            category='sports',
            tags=['fitness', 'running', 'shoes'],
            image_url='https://example.com/shoes.jpg',
        ),
        CatalogItem(
            item_id='item-003',
            title='Smart Home Security Camera',
            description='WiFi camera with night vision, motion alerts, and cloud recording.',
            category='electronics',
            tags=['security', 'camera', 'smart-home'],
            image_url='https://example.com/camera.jpg',
        ),
        CatalogItem(
            item_id='item-004',
            title='Minimalist Office Chair',
            description='Ergonomic chair for home office comfort and productivity.',
            category='furniture',
            tags=['office', 'ergonomic', 'home'],
            image_url='https://example.com/chair.jpg',
        ),
    ]
