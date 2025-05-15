# Sprint_6
Проектная работа 6-го спринта
Автотесты для сервиса аренды самокатов

Проект автоматизированного тестирования веб-приложения аренды самокатов с использованием Python, Selenium, Pytest и Allure

## 🛠 Технологии
- **Python 3.9+**
- **Selenium 4**
- **Pytest**
- **Allure Framework**
- **Page Object Model**
- **Git**

## ✅ Тестируемые функциональности
1. Переходы по логотипам:
   - Логотип Самоката → Главная страница
   - Логотип Яндекса → Дзен в новой вкладке

2. Оформление заказа:
   - Через верхнюю и нижнюю кнопки "Заказать"
   - Валидация форм:
     - "Для кого самокат" (личные данные)
     - "Про аренду" (детали заказа)
   - Подтверждение заказа

3. FAQ-раздел:
   - Проверка раскрытия ответов
   - Валидация текста ответов

## ⚙ Требования
1. Установленный [Python 3.9+](https://www.python.org/)
2. Браузер [Mozilla Firefox](https://www.mozilla.org/)
3. [Geckodriver](https://github.com/mozilla/geckodriver) (автоматическая установка через webdriver-manager)

## 📥 Установка
1. Клонировать репозиторий:
```bash
git clone https://github.com/your-username/scooter-autotests.git
cd scooter-autotests
Установить зависимости:

bash
pip install -r requirements.txt
🚀 Запуск тестов
Все тесты:

bash
pytest tests/ --alluredir=allure-results
Отдельные тесты:

bash
# Тесты заказа
pytest tests/test_order.py

# Тесты логотипов
pytest tests/test_logos.py

# Тесты FAQ
pytest tests/test_faq.py
📊 Отчеты Allure
Генерация отчета:

bash
allure serve allure-results
Пример отчета:
Allure Report

📁 Структура проекта
scooter-autotests/
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/
│   ├── test_faq.py
│   ├── test_logos.py
│   └── test_order.py
├── locators/
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── data/
│   └── test_data.py
├── allure-results/
├── requirements.txt
└── README.md
