from users.models import FirebaseUsers
from django.contrib import admin
from .user.delete import delete_user
from .user.update import update_user_info


# Register your models here.
class FirebaseUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'name', 'email',
                    'provider', 'verified', 'last_sign_in',)
    list_display_links = ('id', 'uid', 'name', 'email',
                          'provider', 'verified')
    search_fields = ('uid', 'name', 'email',
                     'provider', 'verified', 'disabled')
    list_per_page = 10
    readonly_fields = ('provider', 'uid', 'last_sign_in', 'create_at')
    fieldsets = (
        (
            None, {
                'fields': ['uid', 'email', 'password']
            }
        ),
        (
            "Personal Information", {
                'fields': ['name', 'phone', 'user_image', 'provider']
            }
        ),
        (
            "Permissions", {
                'fields': ['verified', 'disabled']
            }
        ),
        (
            "Important dates", {
                'fields': ['last_sign_in', 'create_at']
            }
        ),
    )
    save_on_top = True

    list_filter = (
        ('provider', admin.AllValuesFieldListFilter),
        'verified',
        'disabled',
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('password', 'phone')
        return self.readonly_fields

    def delete_model(self, request, obj):
        delete_user(obj)

    def save_model(self, request, obj, form, change):
        print("88888888888888888888888888")
        update_user_info(obj=obj)

    def get_actions(self, request):
        pass


admin.site.register(FirebaseUsers, FirebaseUserAdmin)
