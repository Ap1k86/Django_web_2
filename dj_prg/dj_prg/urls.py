from django.contrib import admin
from django.urls import path
from dj_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---- Обработка формы В ДВУХ МЕТОДАХ (GET / POST) ----
    # Маршрут №1 (ДЕЙСТВИЯ: Показать ФОРМУ на странице)
    path('form1', views.form1_get, name="form1_get"),
    # Маршрут №2: (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы + Показать ДАННЫЕ на странице)
    path('form2', views.form2_get, name="form1_get"),

    # ---- Обработка формы В ОДНОМ МЕТОДЕ ----
    path('form_processing', views.form_processing, name="form_processing"),

]