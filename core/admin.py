from django.contrib import admin
from .models import Major, Profile, ProfileDocument, CompetencePassport, Module

admin.site.site_header = "Панель управление аккредитацией"       
admin.site.site_title = "админ панель"       
admin.site.index_title = "Аккредитация"       

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0
    fields = ("name", "full_time", "part_time")
    show_change_link = True


class ProfileDocumentInline(admin.TabularInline):
    model = ProfileDocument
    extra = 0
    fields = ("title", "file")
    readonly_fields = ()
    show_change_link = False


class CompetencePassportInline(admin.TabularInline):
    model = CompetencePassport
    extra = 0
    fields = ("title", "file")
    show_change_link = False


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0
    fields = ("name", "annotation", "syllabus", "assessment_fund")
    show_change_link = False


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "level")
    search_fields = ("name", "code", "level")
    ordering = ("name",)
    inlines = [ProfileInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "full_time", "part_time")
    list_filter = ("major", "full_time", "part_time")
    search_fields = ("name", "major__name", "major__code")
    inlines = [ProfileDocumentInline, CompetencePassportInline, ModuleInline]
    autocomplete_fields = ("major",)


@admin.register(ProfileDocument)
class ProfileDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "profile", "file")
    search_fields = ("title", "profile__name")
    list_select_related = ("profile",)


@admin.register(CompetencePassport)
class CompetencePassportAdmin(admin.ModelAdmin):
    list_display = ("title", "profile")
    search_fields = ("title", "profile__name")
    list_select_related = ("profile",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "profile")
    search_fields = ("name", "profile__name")
    list_select_related = ("profile",)
