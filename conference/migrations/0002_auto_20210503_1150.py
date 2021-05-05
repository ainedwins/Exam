# Generated by Django 3.1.7 on 2021-05-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newslettersubcriber',
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='City',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Email',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Firstname',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Lastname',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='Phone',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='program',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]