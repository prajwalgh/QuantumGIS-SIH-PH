# Generated by Django 4.1 on 2022-08-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0008_merge_20220819_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='FRV_Assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FRV_Type', models.CharField(max_length=20)),
                ('Driver_Name', models.CharField(max_length=100)),
                ('lat', models.CharField(default='', max_length=50)),
                ('lng', models.CharField(default='', max_length=50)),
                ('case_id', models.CharField(max_length=50)),
                ('end_lat', models.CharField(default='', max_length=50)),
                ('end_lng', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='frv',
            name='end_lat',
        ),
        migrations.RemoveField(
            model_name='frv',
            name='end_lng',
        ),
        migrations.AlterField(
            model_name='form1detail',
            name='lat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='form1detail',
            name='lng',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='frv',
            name='lat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='frv',
            name='lng',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='history',
            name='lat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='history',
            name='lng',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operations',
            name='lat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operations',
            name='lng',
            field=models.CharField(default='', max_length=50),
        ),
    ]
