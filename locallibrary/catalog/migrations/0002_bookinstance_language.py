# Generated by Django 5.0.3 on 2024-04-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.CharField(blank=True, choices=[('e', 'English'), ('s', 'Spanish'), ('f', 'French'), ('a', 'Arabic')], default='e', help_text='Book language', max_length=100),
        ),
    ]
