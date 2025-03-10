from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup

# KEYBOARDS FILE

async def main_menu_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Поиск ЭБУ", callback_data=f"find_ebu")],
        [InlineKeyboardButton(text="Поиск авто", callback_data=f"find_car")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard