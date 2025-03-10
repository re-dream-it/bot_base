from loader import dp, bot, db
from aiogram import types, F
from filters import admin_filter
from aiogram.fsm.context import FSMContext
import keyboards

# BOT HANDLERS

# start
@dp.message(F.text == ('/start'), admin_filter)
async def execute_command(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, f"*Пример обработки /start!*", parse_mode='markdown', reply_markup=await keyboards.main_menu_keyboard())