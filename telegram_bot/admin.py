from django.contrib import admin

from .models import User, Product


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'telegram_id', 'username', 'first_name', 'last_name', 'is_registered')  # Какие поля отображать в списке
    search_fields = ('telegram_id', 'username', 'first_name', 'last_name')  # По каким полям можно искать
    list_filter = ('is_registered',)  # Фильтрация по полю is_registered
    ordering = ('telegram_id',)  # Сортировка по telegram_id


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'phone_number', 'prodOwner')  # Поля для отображения
    search_fields = ('title', 'description')  # Поля для поиска
    list_filter = ('price',)  # Поля для фильтрации
    ordering = ('title',)  # Сортировка по названию


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
