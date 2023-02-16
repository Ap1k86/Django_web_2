from django.contrib import admin
from django.urls import path
from dj_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---- Обработка формы В ДВУХ МЕТОДАХ (GET / POST) ----
    # Маршрут №1 (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
    path('form1', views.form1_get, name="form1_get"),
    # Маршрут №2: (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + Показать ДАННЫЕ на странице)
    path('form1_post', views.form1_post, name="form1_post"),

    # ---- Обработка формы В ОДНОМ МЕТОДЕ ----
    path('', views.form2, name="form2"),

]