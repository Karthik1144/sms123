from django.db import models
class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key=True)
    comments = models.TextField(max_length=255)
    # phone = models.CharField(max_length=10, default='')

    class Meta:
        db_table = "contactus"

# Create your models here.
