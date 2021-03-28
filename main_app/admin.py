from django.contrib import admin
from main_app import models

# defining a new class
class companyAdmin(admin.ModelAdmin):
    #list_display is used (naming the fields taken by item model)
    list_display = ('id', 'name', 'license_no', 'address', 'email', 'contact_no', 'description')
    list_per_page = 25
    # search_fields = ("name", "email")
    
    class Meta:
        ordering = ['id']
        

class medicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine_type', 'batch_no', 'shelf_no', 'in_stock_total', 'qty_in_strip' )
    
# Register your models here.
admin.site.site_header = 'Pharmacy Dashboard'
admin.site.index_title = 'Main Pharmacy DashBoard'

admin.site.register(models.Company, companyAdmin)
admin.site.register(models.Medicine, medicineAdmin)
admin.site.register(models.MedicalDetails)
admin.site.register(models.Employee)
admin.site.register(models.Customer)
admin.site.register(models.Bill)
admin.site.register(models.EmployeeSalary)
admin.site.register(models.BillDetails)
admin.site.register(models.CustomerRequest)
admin.site.register(models.CompanyAcconut)
admin.site.register(models.CompanyBank)
admin.site.register(models.EmployeeBank)


