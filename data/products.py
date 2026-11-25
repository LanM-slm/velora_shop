from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


PRODUCTS = {
    1: {
        "name": "Classic Hoodie",
        "category": "clothes",
        "price": 35,
        "description": "Удобное худи свободного кроя.",
        "photo": "photos/hoodies.jpg",
    },
    2: {
        "name": "Basic T-shirt",
        "category": "clothes",
        "price": 20,
        "description": "Базовая футболка на каждый день.",
        "photo": "photos/tshirt.jpg",
    },
    3: {
        "name": "Classic Sneakers",
        "category": "shoes",
        "price": 60,
        "description": "Удобные повседневные кроссовки.",
        "photo": "photos/sneakers.jpg",
    },
}

CATEGORIES = {
    "clothes": "Одежда",
    "shoes": "Обувь",
    "accessories": "Аксессуары",
}