from django.contrib import admin
from django.http import QueryDict

from penduduk.models import Warga
from itertools import chain


# Register your models here.
@admin.register(Warga)
class PendudukAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    using = 'db_us'
    def save_model(self, request, obj, form, change):
        if obj.country == 'US':
            obj.save(using=self.using)
            return super().save_model(request, obj, form, change)
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        # return list(chain(Warga.objects.using('db_us'), Warga.objects.all()))
        return super().get_queryset(request)
        # return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)