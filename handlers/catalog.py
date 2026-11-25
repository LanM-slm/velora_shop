import os

from aiogram import Router, F, types
from keyboards.menus import catalog_menu
from keyboards.catalog import categories_keyboard, products_keyboard
from data.products import PRODUCTS, BASE_DIR

router = Router()


@router.message(F.text == "Каталог")
async def katalog(message: types.Message):
    await message.answer(
        "Наш каталог",
        reply_markup=catalog_menu()
    )


@router.message(F.text == "Категории товаров.")
async def categories(message: types.Message):
    await message.answer(
        "Выберите категорию товаров:",
        reply_markup=categories_keyboard()
    )


@router.callback_query(F.data.startswith("cat_"))
async def show_category(callback: types.CallbackQuery):
    category = callback.data.split("_", 1)[1]

    filtered = {
        pid: product
        for pid, product in PRODUCTS.items()
        if product["category"] == category
    }

    if not filtered:
        await callback.message.answer(
            "В этой категории пока нет товаров."
        )
    else:
        await callback.message.answer(
            "Выберите товар:",
            reply_markup=products_keyboard(filtered)
        )

    await callback.answer()


@router.message(F.text == "Список товаров.")
async def product_list(message: types.Message):
    await message.answer(
        "Выберите товар:",
        reply_markup=products_keyboard(PRODUCTS)
    )


@router.callback_query(F.data.startswith("product_"))
async def show_product(callback: types.CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    product = PRODUCTS.get(product_id)

    if product is None:
        await callback.answer("Товар не найден")
        return

    caption = (
        f"✨ {product['name']}\n\n"
        f"{product['description']}\n\n"
        f"Цена: {product['price']} $"
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[[
            types.InlineKeyboardButton(
                text="Добавить в корзину",
                callback_data=f"add_{product_id}"
            )
        ]]
    )

    photo_path = BASE_DIR / product["photo"]

    if photo_path.exists():
        await callback.message.answer_photo(
            photo=types.FSInputFile(str(photo_path)),
            caption=caption,
            reply_markup=keyboard
        )
    else:
        await callback.message.answer(
            caption,
            reply_markup=keyboard
        )

    await callback.answer()