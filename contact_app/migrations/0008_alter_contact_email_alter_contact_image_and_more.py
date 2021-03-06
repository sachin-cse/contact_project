# Generated by Django 4.0.4 on 2022-05-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0007_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
