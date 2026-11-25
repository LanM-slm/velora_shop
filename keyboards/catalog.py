from aiogram import types
from data.products import PRODUCTS, CATEGORIES


def categories_keyboard():
    kb = [
        [
            types.InlineKeyboardButton(
                text=name,
                callback_data=f"cat_{key}"
            )
        ]
        for key, name in CATEGORIES.items()
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def products_keyboard(products):
    kb = [
        [
            types.InlineKeyboardButton(
                text=product["name"],
                callback_data=f"product_{pid}"
            )
        ]
        for pid, product in products.items()
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)