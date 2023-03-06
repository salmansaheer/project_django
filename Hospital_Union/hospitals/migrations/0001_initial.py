# Generated by Django 4.0.5 on 2023-02-23 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creator', '0002_remove_hospital_doctors_remove_hospital_staffs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffsAndDoctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, verbose_name='UserName')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('file', models.FileField(max_length=300, upload_to='Uploads', verbose_name='File')),
                ('check_up_doctor', models.CharField(max_length=50, verbose_name='Doctor Appointed')),
                ('check_up_date', models.DateField(verbose_name='checkup date')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='creator.hospital')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='creator.users')),
            ],
        ),
    ]
