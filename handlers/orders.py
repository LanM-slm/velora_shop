import logging
from collections import Counter

from aiogram import Router, F, types

from config import ADMIN_ID
from data.products import PRODUCTS
from data.cart_storage import user_carts

router = Router()


@router.callback_query(F.data == "checkout")
async def checkout(callback: types.CallbackQuery):
    cart = user_carts.get(callback.from_user.id, [])

    if not cart:
        await callback.answer("Корзина пуста!")
        return

    text = "📦 Ваш заказ:\n\n"
    total = 0

    for product_id, quantity in sorted(Counter(cart).items()):
        product = PRODUCTS[product_id]

        text += f"{product['name']} x {quantity}\n"
        total += product["price"] * quantity

    text += f"\nИтого: {total} $"

    kb = [
        [
            types.InlineKeyboardButton(
                text="Подтвердить заказ",
                callback_data="confirm_order"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Отмена",
                callback_data="cancel_order"
            )
        ],
    ]

    await callback.message.answer(
        text,
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=kb)
    )

    await callback.answer()


@router.callback_query(F.data == "confirm_order")
async def confirm_order(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    cart = user_carts.get(user_id, [])

    if not cart:
        await callback.answer("Корзина пуста!")
        return

    username = callback.from_user.username
    buyer = f"@{username}" if username else "Нет username"

    text = (
        f"🛍 Новый заказ!\n\n"
        f"Покупатель: {buyer}\n"
        f"Имя: {callback.from_user.full_name}\n"
        f"ID: {user_id}\n\n"
    )

    total = 0

    for product_id, quantity in sorted(Counter(cart).items()):
        product = PRODUCTS[product_id]
        text += f"{product['name']} x {quantity}\n"
        total += product["price"] * quantity

    text += f"\nИтого: {total} $"

    try:
        await callback.bot.send_message(ADMIN_ID, text)

    except Exception as e:
        logging.error("Ошибка отправки заказа: %s", e)
        await callback.answer(
            "Ошибка отправки заказа.",
            show_alert=True
        )
        return

    user_carts[user_id] = []

    await callback.message.edit_text(
        "✅ Ваш заказ принят! Администратор свяжется с вами."
    )

    await callback.answer()


@router.callback_query(F.data == "cancel_order")
async def cancel_order(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Оформление заказа отменено."
    )
    await callback.answer()