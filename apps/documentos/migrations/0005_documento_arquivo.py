# Generated by Django 4.1.6 on 2023-02-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_alter_documento_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]