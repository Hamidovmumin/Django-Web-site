from django.contrib import admin
from .models import Contract,About,Service,Slider,Category,Blog,Setting,Comment
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia

class BaseAdmin(admin.ModelAdmin):
    # Add buttonu deaktiv etme
    def has_add_permission(self, request, obj=None):
        return False

    # delete buttonu deakriv etme
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone','email','message',)

@admin.register(About)
class AboutAdmin(TranslationAdmin, CommonMedia,BaseAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','image',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, CommonMedia):
    list_display = ('name',)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin, CommonMedia):
    list_display = ('title', 'category', 'views', 'created_at', 'updated_at')


@admin.register(Setting)
class SettingAdmin(TranslationAdmin, CommonMedia,BaseAdmin):
    list_display = ('title',)


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ('blog','author','content','created_at')








