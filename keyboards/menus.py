from aiogram import types

def main_menu():
    kb = [
        [types.KeyboardButton(text="Каталог")],
        [types.KeyboardButton(text="Корзина")],
        [types.KeyboardButton(text="О нас")],
        [types.KeyboardButton(text="Контакты")],
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )


def catalog_menu():
    kb = [
        [
            types.KeyboardButton(text="Категории товаров."),
            types.KeyboardButton(text="Список товаров."),
        ],
        [types.KeyboardButton(text="Главное меню")],
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

def main_menu():
    kb = [
        [types.KeyboardButton(text="Каталог")],
        [types.KeyboardButton(text="Корзина")],
        [types.KeyboardButton(text="О нас")],
        [types.KeyboardButton(text="Контакты")],
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )


def catalog_menu():
    kb = [
        [
            types.KeyboardButton(text="Категории товаров."),
            types.KeyboardButton(text="Список товаров."),
        ],
        [types.KeyboardButton(text="Главное меню")],
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )