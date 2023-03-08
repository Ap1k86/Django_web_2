from django.contrib import admin
from django.urls import path
from dj_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршрут главной страницы.
    path('', views.index, name='Main page'),

    # Маршрут №1 БЕЗ BOOTSTRAP (ДЕЙСТВИЯ: Показать ФОРМУ №1 на странице)
    path('form1', views.Forms.one_get, name="form1_get"),

    # Маршрут №2 С BOOTSTRAP (ДЕЙСТВИЯ: Показать ФОРМУ №2 на странице)
    path('form2', views.Forms.two_get, name="form2_get"),

    # Маршрут №3 С BOOTSTRAP (ДЕЙСТВИЯ: Показать ФОРМУ №3 на странице)
    path('form3', views.Forms.three_get_post, name="form3_get"),

    # Маршрут №4
    path('operation', views.Models.operation, name="operation"),

    # Маршрут №5: (ДЕЙСТВИЯ: Принимает ДАННЫЕ из формы 1/2 + Показать ДАННЫЕ на странице)
    path('form_processing', views.Forms.processing, name="form_processing"),

    # Маршрут №6 Действия: (Работа с бд)
    path('edit/<int:user_id>', views.Models.edit, name='edit'),
    path('delete/<int:user_id>/', views.Models.delete, name='delete'),
    path('create', views.Models.create_user, name='create_user')
]
