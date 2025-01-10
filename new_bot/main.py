import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import wikipedia
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import requests
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
TELEGRAM_TOKEN = os.getenv("7366704777:AAEOKF_WYmzWewcpqk6W0v3hYeKqGNiUGIs")
OPENWEATHER_API_KEY = "5512be61358ca16f9e773c17ac30504e"

wikipedia.set_lang('uz')

bot = Bot(token='7366704777:AAEOKF_WYmzWewcpqk6W0v3hYeKqGNiUGIs')
dp = Dispatcher()

# Start komandasi uchun handler
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Assalomu alaykum! Menga shahar nomini yozing, men sizga ob-havo haqida ma'lumot beraman. 🌍")



def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=uz"
    response = requests.get(url)
    print(response.status_code, response.text)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"🌤 {name} shahrida ob-havo:\n🌡 Harorat: {temp}°C\n📋 Tavsif: {description.capitalize()}"
    else:
        return "❌ Shahar nomi noto'g'ri yoki shahar nomi ingiliz tilida yozilmagan."


@dp.message()
async def send_weather(message: Message):
    city = message.text
    weather_info = get_weather(city)
    await message.answer(weather_info)




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())







