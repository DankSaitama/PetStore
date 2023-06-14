from django.contrib import admin
from .models import login_form,Product_details,Birds_details


# Register your models here.
admin.site.register(login_form)
admin.site.register(Product_details)
admin.site.register(Birds_details)
# admin.site.register(Staff)
# admin.site.register(Layoff)
# admin.site.register(Author)
# admin.site.register(Book)
admin.site.site_title="Pet Store"
admin.site.site_header="Pet Store"
