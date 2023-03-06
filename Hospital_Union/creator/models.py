from django.db import models

# Create your models here.
class GeneralDetails(models.Model):
    general_details_id = models.AutoField(
        primary_key=True
    )

    username = models.CharField(
        verbose_name ="UserName",
        max_length=50,
        unique=True)

    email = models.EmailField(
        verbose_name="Email",
        null=True)

    password = models.CharField(
        verbose_name="Password",
        max_length=20
    )

    role = models.CharField(
        verbose_name="role",
        max_length=50,
        # default='user'
    )

class Users(models.Model):
    GENDER=(
        ('male',"Male"),
         ("female","Female"),
    )
    MARITAL=(
        ('Single','Single'),
        ('Married','Married')
    )

    BLOODGROUP=(
        ('O positive','O positive'),
        ('A positive','A positive'),
        ('B positive','B positive'),
        ('AB positive','AB positive'),
        ('O negative','O negative'),
        ('A negative','A negative'),
        ('B negative','B negative'),
        ('AB negative','AB negative')
    )

    firstname = models.CharField(
        verbose_name ="First Name",
        max_length=50,)

    lastname = models.CharField(
        verbose_name ="Last Name",
        max_length=50,)

    dob = models.DateField(
        verbose_name='Date of Birth'
    )

    address = models.TextField(
        verbose_name= "Address",
        max_length=500)

    marital = models.CharField(
        verbose_name='Marital Status',
        choices=MARITAL,
        max_length=50)

    gender = models.CharField(
        verbose_name = 'Gender',
        max_length=50,
        choices=GENDER)
    
    religion= models.CharField(
        verbose_name='Religion',
        max_length=25
    )

    caste = models.CharField(
        verbose_name= "Caste",
        max_length=50,)

    phone= models.BigIntegerField(
        verbose_name="Phone number"
    )

    bloodgroup=models.CharField(
        verbose_name='Blood Group',
        max_length=50,
        choices=BLOODGROUP
    )

    image = models.FileField(
        verbose_name='Photo',
        upload_to='User_Photo',
        max_length=300) 

    general_details = models.ForeignKey(
        to=GeneralDetails,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(
        verbose_name ="Hospital Name",
        max_length=50,)

    # image = models.FileField(verbose_name='images',upload_to='hospital_images',null=True)

    phone= models.BigIntegerField(
        verbose_name="Phone number"
    )

    general_details = models.ForeignKey(
        to=GeneralDetails,
        on_delete=models.CASCADE)