# Generated by Django 3.0.5 on 2020-04-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/filesharing/%Y/%m/%d/')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_delete', models.DateTimeField()),
                ('password_for_delete', models.CharField(blank=True, max_length=40, null=True)),
                ('password_for_download', models.CharField(blank=True, max_length=40, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('creator_ip', models.CharField(max_length=15)),
            ],
        ),
    ]
