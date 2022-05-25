from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['user', 'timestamp', 'updated']

admin.site.register(Recipe, RecipeAdmin)
