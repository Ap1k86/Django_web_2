from django.shortcuts import render
from dj_app.forms import *  # Импортируем все ФОРМЫ
from django.http import HttpResponse


# FORM 1: Вторая страница (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + Показать ДАННЫЕ на странице)
def form1_post(request):
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


# FORM 1: Первая страница (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
def form1_get(request):
    my_form = UserForm()  # Создали объект формы
    context = {"form": my_form}
    return render(request, "form1.html", context=context)


# FORM 2: Главная страница
def form2(request):
    my_form = UserForm()  # Создали объект формы
    context = {"form": my_form}
    return render(request, "form2.html", context=context)


