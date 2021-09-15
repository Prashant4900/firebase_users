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
    list_per_page = 50
    readonly_fields = ('provider', 'uid', 'phone', 'image_preview', 'last_sign_in', 'create_at')
    fieldsets = (
        (
            None, {
                'fields': ['uid', 'email', 'password']
            }
        ),
        (
            "Personal Information", {
                'fields': ['name', 'phone', 'user_image', 'image_preview', 'provider']
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
        ("phone", admin.EmptyFieldListFilter),
        ("user_image", admin.EmptyFieldListFilter),
        'create_at',
        'last_sign_in',
    )

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return self.readonly_fields + ('user_image', 'phone')
        return self.readonly_fields + ('password',)

    def delete_model(self, request, obj):
        delete_user(obj)

    def save_model(self, request, obj, form, change):
        update_user_info(obj=obj)

    def get_actions(self, request):
        pass

    def add_view(self, request, form_url='', extra_context=None):
        return self.changeform_view(request, None, form_url, extra_context)


admin.site.register(FirebaseUsers, FirebaseUserAdmin)
