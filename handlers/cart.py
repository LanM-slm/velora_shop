from collections import Counter

from aiogram import Router, F, types

from data.products import PRODUCTS
from data.cart_storage import user_carts

router = Router()


def build_cart(user_id: int):
    cart = user_carts.get(user_id, [])

    if not cart:
        return None

    text = "🛍 Ваша корзина:\n\n"
    kb = []
    total = 0

    for product_id, quantity in sorted(Counter(cart).items()):
        product = PRODUCTS[product_id]

        text += (
            f"{product['name']}\n"
            f"Количество: {quantity}\n"
            f"Цена: {product['price']} $\n\n"
        )

        total += product["price"] * quantity

        kb.append([
            types.InlineKeyboardButton(
                text=f"Удалить {product['name']}",
                callback_data=f"remove_{product_id}"
            )
        ])

    text += f"Итого: {total} $"

    kb.append([
        types.InlineKeyboardButton(
            text="Очистить корзину",
            callback_data="clear_cart"
        )
    ])

    kb.append([
        types.InlineKeyboardButton(
            text="Оформить заказ",
            callback_data="checkout"
        )
    ])

    return text, types.InlineKeyboardMarkup(inline_keyboard=kb)


@router.callback_query(F.data.startswith("add_"))
async def add_to_cart(callback: types.CallbackQuery):
    product_id = int(callback.data.split("_")[1])

    if product_id not in PRODUCTS:
        await callback.answer("Товар не найден")
        return

    user_carts.setdefault(
        callback.from_user.id, []
    ).append(product_id)

    await callback.answer("Товар добавлен в корзину!")


@router.message(F.text == "Корзина")
async def show_cart(message: types.Message):
    result = build_cart(message.from_user.id)

    if result is None:
        await message.answer("🛒 Ваша корзина пока пуста.")
        return

    text, keyboard = result
    await message.answer(text, reply_markup=keyboard)


@router.callback_query(F.data.startswith("remove_"))
async def remove_from_cart(callback: types.CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    cart = user_carts.get(callback.from_user.id, [])

    if product_id in cart:
        cart.remove(product_id)

    result = build_cart(callback.from_user.id)

    if result is None:
        await callback.message.edit_text("🛒 Ваша корзина пуста.")
    else:
        text, keyboard = result
        await callback.message.edit_text(
            text,
            reply_markup=keyboard
        )

    await callback.answer("Товар удалён из корзины.")


@router.callback_query(F.data == "clear_cart")
async def clear_cart(callback: types.CallbackQuery):
    user_carts[callback.from_user.id] = []

    await callback.message.edit_text("🛒 Корзина очищена.")
    await callback.answer()