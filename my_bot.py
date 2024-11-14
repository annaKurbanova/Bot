from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Тексты для кнопок
button_texts = {
    "О нас": (
        "ООО <BTL> – это динамично развивающаяся логистическая компания, которая предлагает комплексные услуги "
        "в области международной торговли и логистики. Мы специализируемся на оптимизации цепочки поставок от поиска "
        "поставщиков до доставки товаров в Российскую Федерацию.\n\n"
        "🆒 выкуп от 0%\n👍 доставка от 0,5 доллара\n👍 поиск товара от 3000 р\n🤬 перевод в Китай 1%\n\n"
        "[Наш сайт](http://9339-logistics.ru/)"
    ),
    "Услуги": (
        "Наши Услуги:\n\n"
        "1️⃣ Поиск поставщиков: Мы помогаем нашим клиентам находить надежных поставщиков за рубежом, проводим анализ "
        "рынка и оценку потенциальных партнеров.\n"
        "2️⃣ Закуп товаров: Мы организуем процесс закупок от переговоров о ценах до оформления.\n"
        "3️⃣ Денежные переводы: Быстрые и безопасные международные транзакции.\n"
        "4️⃣ Таможенные оформления: Помощь в прохождении всех таможенных процедур.\n"
        "5️⃣ Логистические перевозки в РФ: Полный контроль доставки товаров, включая морские, воздушные и авто перевозки.\n\n"
        "КАРГО🇷🇺 BTL-logistics 🇨🇳 Доставка из Китая\n"
        "🔥 Выкуп от 0%\n🔥 Доставка от 0,5 доллара\n🔥 Поиск товара от 3000 руб\n🔥 Перевод в Китай 1%\n\n"
        "Сроки доставки до Москвы (Гуанчжоу - Россия):\n"
        "✈️ Обычная авиа: 9-12 дней\n🛻 Экспресс авто: 13-15 дней\n🛻 Обычное авто: 18-25 дней"
    ),
    "Отзывы": "Отзывы можно прочитать здесь: [VK](https://vk.com/topic-228005427_53134904)",
    "Контакты": (
        "Для получения дополнительной информации о наших услугах или для начала сотрудничества, пожалуйста, свяжитесь с нами:\n\n"
        "📱 [Сайт](http://9339-logistics.ru/)\n"
        "📱 [VK](https://vk.com/cargo9339)\n"
        "📱 [WhatsApp](https://wa.me/+8615545033334)\n"
        "📱 [Instagram](http://instagram.com/9339-cargo)"
    )
}

# Обработчик команды /start для показа начальных кнопок
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[key for key in button_texts]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Добро пожаловать! Выберите нужный раздел:", reply_markup=reply_markup)

# Обработчик для команды /edit_text <название> <новый текст>
async def edit_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Используйте: /edit_text <название> <новый текст>")
        return
    
    button_name = args[0]
    new_text = ' '.join(args[1:])
    
    if button_name in button_texts:
        button_texts[button_name] = new_text
        await update.message.reply_text(f"Текст кнопки '{button_name}' обновлен.")
    else:
        await update.message.reply_text("Такой кнопки не существует.")

# Обработчик для нажатия кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text in button_texts:
        await update.message.reply_text(button_texts[text], parse_mode="Markdown")

# Запуск бота
def main() -> None:
    application = Application.builder().token("токен_бота").build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('edit_text', edit_text))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
