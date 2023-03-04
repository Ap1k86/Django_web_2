import json
# Класс по работе с файлами json.
from class_files import File
from json.decoder import JSONDecodeError

from django.shortcuts import render
# from dj_app.forms import *  # Импортируем все ФОРМЫ
from django.http import *
from .forms import *
from .models import *


# Метод главной страницы.
def index(request):
    return render(request, 'index.html')


# Класс содержащий методы для работы с моделями.
class Models:
    @staticmethod
    def operation(request):
        if request.method == "GET":
            form = OperationForm()

            data = DataBase.read(Person, mode="filter")
            return render(request, 'operation.html', {"data": data, "form": form})

        if request.method == "POST":
            form = OperationForm()

            name = request.POST.get("name")
            age = request.POST.get("age")

            if len(name) and len(age):
                kwargs = {"name": name, "age": age}
                DataBase.write(Person, **kwargs)

            data = DataBase.read(Person, "all")
            return render(request, 'operation.html', {"data": data, "form": form, "name": name})


# Удаление данных из базы данных.
# Класс содержащий ВНУТРЕННЮЮ работу с бд.
class DataBase:

    @staticmethod
    def read(model, mode="all"):

        if mode == "all":
            return model.objects.all()

        if mode == "filter":
            return model.objects.filter(age=99)

        if mode == "exclude":
            return model.objects.filter(exclude=16)

        if mode == "get":
            return model.objects.get(id=id)

    @staticmethod
    def write(model, **kwargs):
        model(**kwargs).save()

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    # Создание нового юзера.
    @staticmethod
    def create_used(login, password, email):
        try:
            from django.contrib.auth.models import User
            from django.db.utils import IntegrityError
            User.objects.create_user(login, password, email)
        except IntegrityError:
            pass


# Класс работы с формой.
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

    # FORM 3: Третья форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
    @staticmethod
    def three_get_post(request):
        if request.method == "GET":
            my_form = FloatingForm
            return render(request, 'form3.html', {'form': my_form})
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            data = {"email": email, "password": password}

            File.write_json(data=data, path="db.json", overwriting=False)

        x = File.read_json(path="db.json")

        context = {"x": x}
        return render(request, 'form3.html', context=context)

    # ОБРАБОТКА 1/2 форм (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + показать ДАННЫЕ на странице)
    @staticmethod
    def processing(request):

        # Записываем в базу данных.
        person = Person.objects.all()
        human = Person()
        human.name = request.POST.get("name")
        human.age = request.POST.get("age")
        human.save()
        print(request.POST)  # Вывод словаря (содержащий все отправленные данные формы)

        # request.POST - это QueryDict
        # Чтобы из элемента QueryDict получить list а не str, нужно использовать метод .getlist("country")

        # Пример рабочего кода (где получаем список из MultipleChoiceField)
        x = request.POST.getlist("country")
        print(x, type(x))

        flag = True if request.POST.get("flag") == "on" else False  # Получаем отдельно из формы Флаг
        text = "<h2>Данные из формы:</h2>"  # Переменная содержащая финальный/возвращаемый html
        for key, value in request.POST.items():  # Цикл, который генерирует остальную часть "text"
            if value:
                if not key == "csrfmiddlewaretoken" and not key == "flag":  # Исключение двух элементов словаря
                    if key == "country":
                        # 1 способ (хуже)
                        # text += "<b>{}:</b> ".format(key[0].upper() + key[1:])  # Добавляем - Country:
                        # for i in request.POST.getlist("country"):
                        #     text += "{} ".format(i)  # # Добавляем - Англия Германия Испания
                        # text += "<br>"  # Добавляем - Переход на новую строку
                        # 2 способ (лучше)
                        country = ", ".join(request.POST.getlist("country"))  # строка со странами
                        text += f"<b>{key}:</b> {country}<br>"  # Добавляем - Country:
                    else:
                        text += "<b>{}:</b> {}<br>".format(key[0].upper() + key[1:], value)
        text += "<b>{}:</b> {}<br>".format("Flag", flag)  # Исключение. Добавление отдельно Флага в финальный "text"
        return HttpResponse(text)
