from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) #max length = required
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField(blank = True, null = False)
    featured = models.BooleanField() #null=True, default = True ou pode esperar dar error ao dar comando python manage.py makemigrations
                                     # e usar a opção 1 para criar um valor default para os valores que já estão no banco de dados.
    #python manage.py makemigrations
    #It is impossible to add a non-nullable field 'featured' to product without specifying a default. This is because the database needs something to populate existing rows.
    #Please select a fix:
        #1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        #2) Quit and manually define a default value in models.py.
    #Select an option: 1
    #Please enter the default value as valid Python.
    #The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
    #Type 'exit' to exit this prompt
    #>>> True
    #Migrations for 'trydjango':
    #  trydjango\migrations\0002_product_featured_alter_product_summary.py
    #    + Add field featured to product
    #    ~ Alter field summary on product