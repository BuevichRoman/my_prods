from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode
import asyncio
import logging
import config
from bs4 import BeautifulSoup
from urllib.request import urlopen



# создание диспетчера
dp = Dispatcher()

# функиця команды старт
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text=f"hello {markdown.hbold(message.from_user.full_name)}",
        parse_mode=ParseMode.HTML)

# функиця команды хелп
@dp.message(Command("help"))
async def help(message: types.Message):
    text = "i'm an echo bot, send me any message"
    await message.answer(text=text)

#функия команды доллар
@dp.message(Command("usd"))
async def dollar(message: types.Message):
    html = urlopen("https://finance.rambler.ru/currencies/USD/").read().decode('utf-8')
    s = str(html)
    soup = BeautifulSoup(s, 'html.parser')
    dol = soup.find("div", class_="finance-currency-plate__col finance-currency-plate__col--value-tomorrow")
    dollar = dol.find("div", class_="finance-currency-plate__currency")
    await message.answer(text=dollar.text)

@dp.message(Command("eur"))
async def euro(message: types.Message):
    html = urlopen("https://finance.rambler.ru/currencies/EUR/").read().decode('utf-8')
    s = str(html)
    soup = BeautifulSoup(s, 'html.parser')
    ev= soup.find("div", class_="finance-currency-plate__col finance-currency-plate__col--value-tomorrow")
    euro = ev.find("div", class_="finance-currency-plate__currency")
    await message.answer(text=euro.text)


# функция - отвечает вашим же сообщением
@dp.message()
async def echo(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.reply(text="это я еще не умею обрабатывать,"
        "потому что Рома еще слишком тупой и не знает как это реализовать, если что пиште ему, пусть сделает https://t.me/BUEVICHjr ")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())