from django.contrib import admin

from .models import BooleanAttribute, TimeAttribute, IntegerAttribute, FloatAttribute, \
    TravelAttribute, StringAttribute, AttributeModule


class BaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration')
    search_fields = ('name',)


@admin.register(BooleanAttribute)
class BooleanAttributeAdmin(BaseAdmin):
    pass


@admin.register(TimeAttribute)
class TimeAttributeAdmin(BaseAdmin):
    pass


@admin.register(IntegerAttribute)
class IntegerAttributeAdmin(BaseAdmin):
    pass


@admin.register(FloatAttribute)
class FloatAttributeAdmin(BaseAdmin):
    pass


@admin.register(TravelAttribute)
class TravelAttributeAdmin(BaseAdmin):
    pass


@admin.register(StringAttribute)
class StringAttributeAdmin(BaseAdmin):
    pass


@admin.register(AttributeModule)
class AttributeEventModuleMapperAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'standard', 'event_module', 'field_type')
    search_fields = ('event_module',)
