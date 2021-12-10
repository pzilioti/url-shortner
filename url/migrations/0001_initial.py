# Generated by Django 4.0 on 2021-12-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=5)),
                ('long', models.CharField(max_length=100)),
                ('click_count', models.IntegerField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='url',
            constraint=models.UniqueConstraint(fields=('short',), name='unique_short_url'),
        ),
    ]