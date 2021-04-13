# Generated by Django 3.2 on 2021-04-08 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=250)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='crudapp.brand')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Brands', to='crudapp.category')),
            ],
        ),
    ]