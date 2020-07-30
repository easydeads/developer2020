from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

"""
То, как я импортирую класс Config, может показаться запутанным сначала, но если вы посмотрите, как класс Flask (в верхнем регистре «F») импортируется из flask пакета (нижний регистр «f»), вы заметите, что я делаю то же самое с конфигурацией. Строковый «config» — это имя модуля python config.py, и, очевидно, тот, который имеет верхний регистр «C», является фактическим классом.
"""
""" Сценарий выше создает объект приложения как экземпляр класса Flask, Переменная __name__, переданная в класс Flask является переопределенной переменной пайтон которая задается именем модуля в котором она используется. Flask использует расположение модуля, переданного здесь как отправную точку, когда ему необходимо загрузить связанные ресурсы такие как файлы шаблонов... """
