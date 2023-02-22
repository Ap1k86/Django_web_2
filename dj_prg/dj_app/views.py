import json

from django.shortcuts import render
from dj_app.forms import *  # Импортируем все ФОРМЫ
from django.http import HttpResponse


# Метод главной страницы.
def index(request):
    return render(request, 'index.html')


# FORM 1: Первая форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
def form1_get(request):
    my_form = UserForm()  # Создали объект формы
    context = {"form": my_form}
    return render(request, "form1.html", context=context)


# FORM 2: Вторая форма (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
def form2_get(request):
    my_form = UserForm()  # Создали объект формы
    context = {"form": my_form}
    return render(request, "form2.html", context=context)


def form3_get_post(request):
    if request.method == "GET":
        my_form = FloatingForm()
        return render(request, 'form3.html', {'form': my_form})
    if request.method == "POST":
        request.POST.get("email")
        request.POST.get("password")

        dct = {}

        for key, value in request.POST.items():
            if not key == "csrfmiddlewaretoken":
                dct = {key: value}

                with open("dj_prg/data.json", mode="a+") as f:
                    json.dump(dct, f)


# ОБРАБОТКА 1/2 форм (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + показать ДАННЫЕ на странице)

def form_processing(request):
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
