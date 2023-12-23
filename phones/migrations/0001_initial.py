# Generated by Django 4.2.5 on 2023-09-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='phones/')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]