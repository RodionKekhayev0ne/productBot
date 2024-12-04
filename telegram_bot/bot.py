# telegram_bot/bot.py
import random

from asgiref.sync import sync_to_async
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from django.conf import settings
from .models import User, Product


def get_random_product():
    """Получает случайный товар из базы данных"""
    count = Product.objects.count()
    return count
    # if count == 0:
    #     return None  # Если товаров нет
    # random_index = random.randint(0, count - 1)
    # return Product.objects.all()[random_index]


async def start(update, context):
    telegram_id = update.effective_user.id

    # Выполняем синхронный запрос к базе через sync_to_async
    user, created = await sync_to_async(User.objects.get_or_create)(telegram_id=telegram_id)
    keyboard = [
        ['Смотреть товары']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    if created:
        await update.message.reply_text("Вы зарегистрированы!", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Добро пожаловать обратно!", reply_markup=reply_markup)


# Функция для обработки нажатий на кнопки
async def handle_message(update: Update, context):
    text = update.message.text
    if text == 'Смотреть товары':
        # Оборачиваем вызов ORM в sync_to_async
        product_count = await sync_to_async(Product.objects.count)()
        if product_count > 0:
            # Получаем случайный товар
            random_product = await sync_to_async(lambda: Product.objects.order_by("?").first())()
            response = (
                f"Название: {random_product.title}\n"
                f"Описание: {random_product.description}\n"
                f"Номер для покупки: {random_product.phone_number}\n"
                f"Цена: {random_product.price}тг"
            )

            # Отправка изображения и текста
            if random_product.image:  # Если товар имеет изображение
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,  # ID чата
                    photo=random_product.image,  # URL или путь к изображению
                    caption=response  # Текст, который будет добавлен к изображению
                )
    elif text == 'Помощь':
        await update.message.reply_text("Чем я могу помочь?")
    else:
        await update.message.reply_text("Я не понимаю эту команду. Попробуйте ещё раз.")
# Настроим запуск бота
def main():
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Добавим обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("products", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    # Запуск бота
    application.run_polling()
