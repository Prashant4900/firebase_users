from django.contrib import admin
from .models import DummyModel
from .operations.update_data import update_data
from .operations.dalete_data import delete_data


# Register your models here.
@admin.register(DummyModel)
class DummyAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'update_at', 'create_at')
    list_display_links = ('id', 'uid', 'name', 'update_at', 'create_at')
    readonly_fields = ('uid', 'create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('create_at', 'update_at')
    list_per_page = 50
    save_on_top = True

    def get_actions(self, request):
        pass

    def save_model(self, request, obj, form, change):
        update_data(obj)

    def delete_model(self, request, obj):
        delete_data(obj)
