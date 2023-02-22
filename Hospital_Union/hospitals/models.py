from django.db import models
from creator.models import *

# Create your models here.
class MedicalHistory(models.Model):
    # person=models.ForeignKey(
    #     to=Users,)

    # hospital = models.ForeignKey(
    #     to= Hospital,)

    medical_data = models.TextField(
        verbose_name="Medical Data")

    check_up_doctor = models.CharField(
        verbose_name="Doctor Appointed",
        max_length=50)

    date_of_checkup = models.DateField()

class MedicalHistory(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)

    file = models.FileField(
        verbose_name='File',
        upload_to='Uploads',
        max_length=300,
    )

    check_up_doctor = models.CharField(
        verbose_name="Doctor Appointed",
        max_length=50)

    check_up_date = models.DateField(
        verbose_name='checkup date',
    )

     # person=models.ForeignKey(
    #     to=Users,)

    # hospital = models.ForeignKey(
    #     to= Hospital,)


    def __str__(self):
        return self.title
    
    
class StaffsAndDoctors(models.Model):
    # hospital = models.ForeignKey(
    #     to= Hospital,)

    uname = models.CharField(
        verbose_name="UserName",
        max_length=50
        )

    name =models.CharField(
        verbose_name="Name",
        max_length=50
    )

    position = models.CharField(
        verbose_name="Position",
        max_length=50
        )
    
    role = models.CharField(
        verbose_name="Role",
        max_length=50,
        )
    
    password = models.CharField(
        verbose_name="Password",
        max_length=20
    )