# MTUCI

## [Calculater](https://github.com/rinalenskay/mtuci/raw/master/Calculater)

![Image](https://github.com/rinalenskay/mtuci/raw/master/Reports/Screenshots/Calculater.png)

The calculator is written in Python using `PyQt5` library. The calculator performs simple mathematical operations on numbers:
- multiplication; 
- division; 
- addition; 
- subtraction.

The first time you run it, you need to install all of the project's dependencies:
- `pipenv install`

To run the application:
- `pipenv shell`
- `python3 calculator.py`

## [MyWebApp](https://github.com/rinalenskay/mtuci/raw/master/MyWebApp)

![Image](https://github.com/rinalenskay/mtuci/raw/master/Reports/Screenshots/MyWebApp.png)

A small simple blog based on Flask. The application supports:
- Registration users. When a user registers, their login and password are stored in a database;
- Login users. When a user logs in to the blog, their entered data is checked against the database, if the login is successful, the user is welcomed with a message that says: "Hello,*Full Name*!" and prints user's login and password.

This application uses the following libraries:
- `flask`;
- `requests`;
- `psycopg2`.

The first time you run it, you need to install all of the project's dependencies:
- `pipenv install`

To run the application:
- `source venv/bin/activate`
- `pip install -r req.txt`
- `flask run`

## [Simple-bot](https://github.com/rinalenskay/mtuci/raw/master/Simple-bot)

![Image](https://github.com/rinalenskay/mtuci/raw/master/Reports/Screenshots/Simple-Bot.png)

Simple Python Telegram bot, which takes 5 different commands from the user, depending on the command the bot gives a text response.

List of bot commands:
- `/start` - the command to start the bot. The bot welcomes you with a message: "Привет! Хочешь узнать свежую инфорацию о МТУСИ?" (translate: Hello! Do you want to get the lastest news about university MTUCI?). To continue interacting with the bot, you need to write `Хочу` (translate: "Want") in the chat;
- `/help`- the command to show all the commands in a list;
- `/LMS` - the command gives a link to the e-university MTUCI;
- `/ADR` - the command gives the address of university MTUCI;
- `/DEP` - the command gives a link with all departments of university MTUCI.

This application uses the following libraries:
- `pyTelegramBotAPI`;
- `requests`.

## [Tg-bot-Schedule](https://github.com/rinalenskay/mtuci/raw/master/Tg-bot-Schedule)

![Image](https://github.com/rinalenskay/mtuci/raw/master/Reports/Screenshots/Tg-bot-Schedule.png)

Python Telegram bot on Python that responds the BFI2102 schedule. The program automatically determines the type of the current week using the "datetime" library.

The bot supports the following commands:

- "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" - sends the schedule for the specified day.
- `Расписание на текущую неделю` - gives the schedule for the current week.
- `Расписание на следующую неделю` - gives the schedule for the next week.
- `/week` - specifies the type of the current week.
- `/help` - gives a list of bot commands.
- `/mtuci` - gives a link to the official MTUCI website.

The bot displays an error message if the entered message does not belong to the list of commands.

This application uses the following libraries:

- `psycopg2`
- `pyTelegramBotAPI`
- `datetime`

## [UI-Schedule](https://github.com/rinalenskay/mtuci/raw/master/UI-Schedule)

![Image](https://github.com/rinalenskay/mtuci/raw/master/Reports/Screenshots/UI-Schedule.png)

Information of database visualization using PostgreSQL and the PyQt5 module. It displays the database in the form as a tabbed table and allows you to edit its rows as well as add and remove database content.

This application uses the following libraries:
- `psycopg2`
- `datetime`
