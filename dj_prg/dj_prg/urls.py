from django.contrib import admin
from django.urls import path
from dj_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршрут №1 БЕЗ BOOTSTRAP (ДЕЙСТВИЯ: Показать ФОРМУ №1 на странице)
    path('form1', views.form1_get, name="form1_get"),

    # Маршрут №2 С BOOTSTRAP (ДЕЙСТВИЯ: Показать ФОРМУ №2 на странице)
    path('form2', views.form2_get, name="form2_get"),

    # Маршрут №3: (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы 1/2 + Показать ДАННЫЕ на странице)
    path('form_processing', views.form_processing, name="form_processing"),
]
