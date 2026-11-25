from aiogram import Router, F, types
from aiogram.filters import Command
from keyboards.menus import main_menu

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Приветствую вас в нашем магазине Velora!",
        reply_markup=main_menu()
    )


@router.message(F.text == "Главное меню")
async def back_to_main(message: types.Message):
    await message.answer(
        "Главное меню",
        reply_markup=main_menu()
    )


@router.message(F.text == "О нас")
async def about(message: types.Message):
    await message.answer(
        "Velora — магазин стильной повседневной одежды и обуви."
    )


@router.message(F.text == "Контакты")
async def contacts(message: types.Message):
    await message.answer(
        "По всем вопросам пишите администратору магазина."
    )