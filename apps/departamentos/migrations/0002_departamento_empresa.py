# Generated by Django 4.1.6 on 2023-02-07 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa'),
            preserve_default=False,
        ),
    ]
