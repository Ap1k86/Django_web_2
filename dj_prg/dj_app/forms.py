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


# Создание формы №1 (Основные поля)
class UserForm(forms.Form):
    # 1. Поле [str, int, bool]
    name = forms.CharField(label="Имя1", required=False, max_length=5, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Возраст", required=False, max_value=99, widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}))
    flag = forms.BooleanField(label="Флаг", initial=False, required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'form-check-input'}))
    comment = forms.CharField(label="Комментарий", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    # 2. Поле [Выбор ОДНОГО строкового элемента из списка]
    choices = (("Английский", "Английский"), ("Немецкий", "Немецкий"), ("Данные", "Название"))
    ling = forms.ChoiceField(label="Выберите язык", choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))

    # 3. Поле [Выбор МНОЖЕСТВА строковых элементов из списка]
    choices = (("Англия", "Англия"), ("Германия", "Германия"), ("Испания", "Испания"))
    country = forms.MultipleChoiceField(label="Выберите страны", choices=choices, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    # 4. Поле [Выбор файла (ИМЯ) из ОС]
    file1 = forms.FileField(label="Файл", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    # 5. Поле [Выбор файла (ПУТЬ) из ОС]
    file2 = forms.FilePathField(label="Файл", required=False, path=r"C:\Users\st\PycharmProjects\django_web_2\dj_prg", recursive=True, match=".py", allow_folders=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))


# Создание формы №2 (Поля входа)
class FloatingForm(forms.Form):

    email = forms.EmailField(label="Email", required=True, widget=forms.widgets.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com'}))
    password = forms.CharField(label="Password", required=True, widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}))


# Создание формы №3 (Для операций с БД)
class OperationForm(forms.Form):
    name = forms.CharField(label="Введите имя", required=False, max_length=20, widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Введите возраст", required=False, max_value=99, widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}))
