from django.contrib import admin
from .models import DummyModel
from .operations.update import update
from .operations.delete import delete


# Register your models here.
@admin.register(DummyModel)
class DummyAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'user')
    list_display_links = ('id', 'uuid', 'name')
    readonly_fields = ('uuid',)
    search_fields = ('name', 'user')
    list_per_page = 50
    save_on_top = True

    def get_actions(self, request):
        pass

    def save_model(self, request, obj, form, change):
        update(obj)

    def delete_model(self, request, obj):
        delete(obj)
