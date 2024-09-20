# Generated by Django 2.2 on 2019-05-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('slogan', models.CharField(max_length=50, verbose_name='简介')),
                ('sell', models.CharField(max_length=50, verbose_name='宣传')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('photo', models.CharField(max_length=50, verbose_name='相片')),
            ],
        ),
    ]
