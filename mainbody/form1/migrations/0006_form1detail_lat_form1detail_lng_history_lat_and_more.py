# Generated by Django 4.1 on 2022-08-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0005_frv_lat_frv_lng_alter_form1detail_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1detail',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='form1detail',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='operations',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='operations',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='frv',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='frv',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
