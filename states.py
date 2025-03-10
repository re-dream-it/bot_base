from aiogram.fsm.state import State, StatesGroup

# STATES FILE

# Get info input
class get_info(StatesGroup):
    enter_ebu = State()