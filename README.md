Цель проекта — создать парсер, который автоматически собирает информацию о событиях с сайта 98mag.kz из раздела «События».

Парсер должен:

извлекать заголовок события, ссылку и дату публикации;

переходить на страницу каждого события;

сохранять полученные данные в структурированном виде;

быть готовым к масштабированию (расширению на другие категории, сайты, типы данных).

Обоснование задачи:
Такой парсер может быть использован для мониторинга событий города, создания агрегаторов новостей, подписочных сервисов или последующей интеграции во внутренние системы аналитики.

Структура проекта и архитектура

Проект состоит из одного файла:

98mag.py          # Основной скрипт парсинга


Код структурирован таким образом, чтобы:

легко было выделить функции в дальнейшем;

заменить источник данных (другой сайт);

интегрировать парсер в класс или более крупную систему.

Используемые технологии

Проект использует:

Python 3.10+

requests — для загрузки HTML-страниц

lxml — для разбора HTML и поиска элементов

Инструкция по запуску
1. Клонировать репозиторий (если нужно)
git clone <ссылка-на-репозиторий>
cd Parser

2. Создать виртуальное окружение
python -m venv .venv

3. Активировать окружение

Windows:

.venv\Scripts\activate


macOS/Linux:

source .venv/bin/activate

4. Установить зависимости
pip install requests lxml cssselect



5. Запустить проект
python 1.py

Выходные данные

Сейчас результат выводится в консоль:

заголовок события

ссылка

дата

Пример результата работы парсера:

D:\PythonProject\Parser\.venv\Scripts\python.exe D:\PythonProject\Parser\98mag.py 
В Алматы пройдёт фестиваль альтернативных способов печати
https://www.98mag.kz/gorod/sobytiya/v-almaty-projdyot-festival-alternativnyh-sposobov-pechati/
25 ноября 2025

Almaty Museum of Arts представит инсталляцию Бахыт Бубикановой «Чудо»
https://www.98mag.kz/gorod/sobytiya/almaty-museum-of-arts-predstavit-installyacziyu-bahyt-bubikanovoj-chudo/
22 ноября 2025

Atelier Cauchemar запускает серию лимитированных коллекций
https://www.98mag.kz/gorod/cauchemar-edition-novyj-proekt-atelier-cauchemar/
19 ноября 2025

«Кайрат» перенёс два домашних матча Лиги чемпионов в Астану
https://www.98mag.kz/gorod/kajrat-perenyos-dva-domashnih-matcha-ligi-chempionov-na-astana-arenu/
19 ноября 2025

Aspan Gallery на ярмарке Abu Dhabi Art 2025
https://www.98mag.kz/gorod/aspan-gallery-na-yarmarke-abu-dhabi-art-2025/
15 ноября 2025

Чемпионы Formula-1 соберутся в Ташкенте на FIA Awards 2025
https://www.98mag.kz/gorod/chempiony-formula-1-soberutsya-v-tashkente-na-fia-awards-2025/
15 ноября 2025

Gorillaz выступят в Казахстане
https://www.98mag.kz/gorod/gorillaz-vystupyat-v-kazahstane/
14 ноября 2025

В Алматы пройдёт фестиваль подростковой рок-музыки
https://www.98mag.kz/gorod/v-almaty-projdet-festival-podrostkovoj-rok-muzyki/
13 ноября 2025

Алисса Сантос: танцовщица J-Hope и JENNIE в Казахстане
https://www.98mag.kz/gorod/alissa-santos-tanczovshhicza-j-hope-i-jennie-v-kazahstane/
12 ноября 2025

Искусство Алматы: что посмотреть в ноябре?
https://www.98mag.kz/gorod/iskusstvo-almaty-chto-posmotret-v-noyabre/
6 ноября 2025


with open("events.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
