# Generated by Django 2.0.2 on 2019-11-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('number', models.IntegerField(null=True, verbose_name='数字')),
                ('info', models.IntegerField(default=0, null=True, verbose_name='信息')),
            ],
        ),
    ]
