from django import forms

# --- [1] Основные ПАРАМЕТРЫ при создании ПОЛЕЙ ---
# label - Название поля (пишется слева)
# help_text - Подсказка поля (пишется снизу)
# initial - Начальное значение поля (пишется внутри)
# required - False (необязательное к заполнению)
# ТЕКСТ: min_length и max_length - Количество символов ОТ..ДО которое можно ввести
# ЧИСЛО: min_value и max_value - Число ОТ..ДО которое можно ввести
# widget - Объект HTML на основе которого будет построено поле: forms.Textarea() или forms.widgets.DateInput()
# recursive - Рассматривает файлы в подпайках
# match - Регулярное выражение имен (например отбор по расширению .html)
# allow_folders - Рассматривает папки (для выбора)


# Создание формы №1
class UserForm(forms.Form):
    # 1. Поле [str, int, bool]
    name = forms.CharField(label="Имя", required=False, max_length=5, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Возраст", required=False, max_value=99)
    flag = forms.BooleanField(label="Флаг", initial=False, required=False)
    comment = forms.CharField(label="Комментарий", required=False, widget=forms.Textarea())

    # 2. Поле [Выбор ОДНОГО строкового элемента из списка]
    choices = (("Английский", "Английский"), ("Немецкий", "Немецкий"), ("Данные", "Название"))
    ling = forms.ChoiceField(label="Выберите язык", choices=choices)

    # 3. Поле [Выбор МНОЖЕСТВА строковых элементов из списка]
    choices = (("Англия", "Англия"), ("Германия", "Германия"), ("Испания", "Испания"))
    country = forms.MultipleChoiceField(label="Выберите страны", choices=choices)

    # 4. Поле [Выбор файла (ИМЯ) из ОС]
    file1 = forms.FileField(label="Файл", required=False)

    # 5. Поле [Выбор файла (ПУТЬ) из ОС]
    file2 = forms.FilePathField(label="Файл", required=False, path=r"C:\Users\st\PycharmProjects\django_web_2\dj_prg", recursive=True, match=".py", allow_folders=True)























# --- 2-ой способ применения CSS (через виджеты) ---
# У поля можно указать Виджет (widget) на основе которого и будет создано HTML разметка поля.
# А к виджету "Textarea" можно прикрепить класс "mybold". Пример: Textarea(attrs={"class": "mybold"})
# И этот класс описать в CSS (в шаблоне)