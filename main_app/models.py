from django.db import models

# stock database
class Company(models.Model):#Company Contacts
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    license_no = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.CharField(max_length=200)
    added_no = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() # can be accessed later

    def __str__(self):
        return self.name
    class Meta:
        managed = True
        verbose_name =  'Company'
        verbose_name_plural =  'Companys'

class Medicine(models.Model): #new medicine
    id = models.AutoField(primary_key=True)
    medicine_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    buy_price = models.CharField(max_length=255)
    sell_price = models.CharField(max_length=255)
    c_gst = models.CharField(max_length=255)#can be deleted
    s_gst = models.CharField(max_length=255)#can be deleted
    batch_no = models.CharField(max_length=255)
    shelf_no = models.CharField(max_length=255)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    in_stock_total = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Medicine'
        verbose_name_plural =  'Medicine'

    def __str__(self):
        return self.medicine_type

class MedicalDetails(models.Model):#
    id = models.AutoField(primary_key=True)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=200)#can be deleted
    salt_qty = models.CharField(max_length=200)#can be deleted
    salt_qty_type = models.CharField(max_length=200)#can be deleted
    added_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.medicine_id

    class Meta:
        managed = True
        verbose_name =  'Medicine Detail'
        verbose_name_plural =  'Medicine Details'

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    joining_date = models.DateField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name =  'Employee'
        verbose_name_plural =  'Employees'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name + self.contact

    class Meta:
        managed = True
        verbose_name =  'Customer'
        verbose_name_plural =  'Customers'

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.customer_id

    class Meta:
        managed = True
        verbose_name =  'Bill'
        verbose_name_plural =  'Bills'

class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.employee_id

    class Meta:
        managed = True
        verbose_name =  'Employee Salary'
        verbose_name_plural =  'Employee Salaries'

class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Billing Details'
        verbose_name_plural =  'Billing Details'

class CustomerRequest(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    medicine_details = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Customer Request'
        verbose_name_plural =  'Customer Request'

class CompanyAcconut(models.Model):
    choices = ((1, "Debit"), (2, "Credit"))

    id =models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    transcation_type = models.CharField(choices=choices, max_length=200)
    transcation_amt = models.CharField(max_length=200)
    transcation_date = models.DateField()
    payment_mode = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Company Account'
        verbose_name_plural =  'Company Account'

class CompanyBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Company Bank'
        verbose_name_plural =  'Company Bank'

class EmployeeBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account_no = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=200)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        managed = True
        verbose_name =  'Employee Bank'
        verbose_name_plural =  'Employee Bank'


