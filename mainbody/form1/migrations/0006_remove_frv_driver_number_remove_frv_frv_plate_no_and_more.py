# Generated by Django 4.1 on 2022-08-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0005_frv_lat_frv_lng_alter_form1detail_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frv',
            name='Driver_Number',
        ),
        migrations.RemoveField(
            model_name='frv',
            name='FRV_Plate_No',
        ),
        migrations.AddField(
            model_name='frv',
            name='end_lat',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frv',
            name='end_lng',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
