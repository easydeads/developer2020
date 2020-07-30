Все сделано по циклу статей https://habr.com/ru/post/346306/

1. Перейти в microblog дирректорию
2. Создать виртуальное окружение python -m venv venv
3. Установить pip install -r requirements
4. Для запуска сервера необходимо добавить в переменные окружения находясь в дирректории с файлом microblog.py - export FLASK_APP=microblog.py
5. Для запуска сервера flask run
https://habr.com/ru/post/346340/ часть2
https://habr.com/ru/post/346342/ часть3
6. При установке flask-migrate возникла ошибка 
"error: invalid command 'bdist_wheel'
  
  ----------------------------------------
  Failed building wheel for alembic
"
Лечил предварительной установкой
pip install wheel (https://github.com/palantir/python-language-server/issues/524)

https://habr.com/ru/post/346344/ часть4
