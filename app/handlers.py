from aiogram import types,F,Router
from aiogram.filters import *
import asyncio
import app.keyboard
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
router = Router()
class Registr(StatesGroup):
    name = State()
@router.message(Command('help'))
async def help_msg(message : types.Message):
    await message.answer("Help Command",reply_markup=await app.keyboard.carss())
@router.message(CommandStart())
async def stcmd(message : types.Message, state:FSMContext):
    await state.set_state(Registr.name)
    await message.answer("Name")
@router.message(Registr.name,F.text)
async def ongetname(message : types.Message, state:FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(str(data['name']))
