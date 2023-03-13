from django.shortcuts import render
from dj_app.forms import *  # Импортируем все ФОРМЫ
from django.http import HttpResponse, HttpResponseRedirect
from class_files import File
from .models import *  # Импортируем все существующие модели
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


# Метод главной страница
def index(request):
    return render(request, "index.html")


# Класс содержащий методы для работы с ФОРМАМИ
class Forms:

    # FORM 1: Первая форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
    @staticmethod
    def one_get(request):
        my_form = UserForm()  # Создали объект формы
        context = {"form": my_form}
        return render(request, "form1.html", context=context)

    # FORM 2: Вторая форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
    @staticmethod
    def two_get(request):
        my_form = UserForm()  # Создали объект формы
        context = {"form": my_form}
        return render(request, "form2.html", context=context)

    # FORM 3: Третья форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице + ОБРАБОТКА)
    @staticmethod
    def three_get_post(request):
        if request.method == "GET":
            # Создание формы и передача ее в шаблон
            my_form = FloatingForm()
            context = {"form": my_form}
            return render(request, "form3.html", context=context)
        if request.method == "POST":
            # Получение данных из формы
            email = request.POST.get("email")
            password = request.POST.get("password")
            # На основе двух переменных создали словарь
            data = {"email": email, "password": password}  # Новые данные которые будем записывать
            # Запись данных в импровизированную БД (db.json)
            File.write_json(data=data, path="db.json", overwriting=False)
            # Прочитать БД в переменную table
            table = File.read_json("db.json")
            # Генерация ответа
            context = {"table": table}
            return render(request, "form3.html", context=context)

    # ОБРАБОТКА 1/2 форм (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + Показать ДАННЫЕ на странице)
    @staticmethod
    def processing(request):
        print(request.POST)  # Вывод словаря (содержащий все отправленные данные формы)

        # request.POST - это QueryDict
        # Чтобы из элемента QueryDict получить list а не str, нужно использовать метод .getlist("country")

        # Пример рабочего кода (где получаем список из MultipleChoiceField)
        x = request.POST.getlist("country")
        print(x, type(x))

        flag = True if request.POST.get("flag") == "on" else False  # Получаем отдельно из формы Флаг
        text = "<h2>Данные из формы:</h2>"  # Переменная содержащая финальный/возвращаемый html
        for key, value in request.POST.items():  # Цикл, который генерирует остальную часть "text"
            if not key == "csrfmiddlewaretoken" and not key == "flag":  # Исключение двух элементов словаря
                if key == "country":
                    # 1 способ (хуже)
                    # text += "<b>{}:</b> ".format(key[0].upper() + key[1:])  # Добавляем - Country:
                    # for i in request.POST.getlist("country"):
                    #     text += "{} ".format(i)  # # Добавляем - Англия Германия Испания
                    # text += "<br>"  # Добавляем - Переход на новую строку
                    # 2 способ (лучше)
                    country = ", ".join(request.POST.getlist("country"))  # строка со странами
                    text += "<b>{}:</b> {}<br>".format(key[0].upper() + key[1:], country)  # Добавляем - Country:
                else:
                    text += "<b>{}:</b> {}<br>".format(key[0].upper() + key[1:], value)
        text += "<b>{}:</b> {}<br>".format("Flag", flag)  # Исключение. Добавление отдельно Флага в финальный "text"
        return HttpResponse(text)


# Класс содержащий методы для работы с МОДЕЛЯМИ
class Models:

    # Метод маршрута /operation (открывает страницу с функционалом + обработка формы)
    @staticmethod
    def operation(request):
        if request.method == "GET":
            form = OperationForm()  # Создаю форму
            data = DataBase.read(model=Person)  # Читаю таблицу
            context = {"data": data, "form": form}
            return render(request, "operation.html", context=context)
        if request.method == "POST":
            name = request.POST.get("name")  # Получили из формы Имя
            age = request.POST.get("age")  # Получили из формы Возраст
            if len(age):
                # Сохраняем только если поля не пустые
                if len(name) and len(age):
                    kwargs = {"name": name, "age": age}  # Передаваемые аргументы
                    DataBase.write(model=Person, **kwargs)  # Пишет в БД
                else:
                    raise "Не ввели возраст!!"
                form = OperationForm()  # Создаю форму
                data = DataBase.read(model=Person)  # Читаю таблицу
                context = {"data": data, "form": form}
                return render(request, "operation.html", context=context)
            else:
                return render(request, "age_not_specified.html")

    # Метод маршрута /edit
    @staticmethod
    def edit(request, user_id):
        # Отобразить форму изменения данных
        if request.method == "GET":
            form = OperationForm()  # Создаю форму
            data = DataBase.read(model=Person)  # Читаю таблицу
            context = {"data": data, "form": form, "user_id": int(user_id)}
            return render(request, "operation.html", context=context)
        # Обработать форму изменения данных
        if request.method == "POST":
            name = request.POST.get("name")  # Получили из формы Имя
            age = request.POST.get("age")  # Получили из формы Возраст
            kwargs = {"name": name, "age": age}
            DataBase.update(model=Person, elm_id=user_id, **kwargs)  # Обновили

            form = OperationForm()  # Создаю форму
            data = DataBase.read(model=Person)  # Читаю таблицу
            context = {"data": data, "form": form}
            return render(request, "operation.html", context=context)

    # Метод маршрута /delete (удаляет объект из БД и перезагружает страницу)
    @staticmethod
    def delete(request, user_id):
        kwargs = {"id": user_id}  # Передаваемые аргументы
        DataBase.delete(model=Person, **kwargs)  # Удаляю элемент с таблицы
        return HttpResponseRedirect("/operation")

    # Метод маршрута /create_user (создает нового пользователя со статичными данными)
    @staticmethod
    def create_user(request):
        DataBase.create_user("moderator", "12345", "moderator@gmail.com")
        print("Пользователь создан!")
        return HttpResponseRedirect("/operation")


# Класс содержащий ВНУТРЕННЮЮ работу с БД
class DataBase:
    @staticmethod
    # Чтение из таблицы "model" элементов удовлетворяющих тому что передаем в {} через "kwargs"
    def read(model, mode="all", **kwargs):
        # .count() - метод возвращающий количество
        if mode == "all":  # Получить данные для [всех объектов]
            result = model.objects.all()
            return list(result.values())
        if mode == "filter":  # Получить данные [все которые = фильтр]
            result = model.objects.filter(**kwargs)
            return list(result.values())
        if mode == "exclude":  # Получить данные [все которые = не фильтр]
            result = model.objects.exclude(**kwargs)
            return list(result.values())
        if mode == "get":  # Получить данные для [одного объекта]
            result = model.objects.get(**kwargs)  # id/pk одно и тоже
            print(result, type(result))
            return [result]

    @staticmethod
    # Запись в таблицу "model" элемента с полями которые передаем в {} через "kwargs"
    def write(model, **kwargs):
        model(**kwargs).save()  # или Person.objects.create(**kwargs)

    @staticmethod
    # Обновление объекта с "elm_id" в таблице "model", а именно перезапись полей на те, которые в {} через "kwargs"
    def update(model, elm_id, **kwargs):
        model.objects.filter(id=elm_id).update(**kwargs)

    @staticmethod
    # Удаление из таблицы "model" записи, удовлетворяющей фильтру переданному в {} через "kwargs"
    def delete(model, **kwargs):
        model.objects.filter(**kwargs).delete()

    @staticmethod
    # Создание нового пользователя с "login" "password" "email" (все параметры обязательны)
    def create_user(login, password, email):
        try:
            User.objects.create_user(login, email, password).save()
        except IntegrityError:
            pass
