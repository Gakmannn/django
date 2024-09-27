1 Клонировать проект

2 Поднять виртуальное окружение

```
python -m venv .venv
```

3 Активировать вертуальное окружение

cmd
```
.venv\Scripts\activate.bat
```

power shell
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

4 Установить Django

```
python -m pip install Django
```

5 Перейти в папку с проектом

```
cd имя-папки-проекта
```

6 Запустить сервер

```
python manage.py runserver
```
