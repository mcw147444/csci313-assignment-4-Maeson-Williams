# Generated by Django 5.0.3 on 2024-04-03 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_language_remove_bookinstance_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.language'),
        ),
    ]
