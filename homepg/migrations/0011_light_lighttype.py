# Generated by Django 3.2 on 2021-04-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepg', '0010_auto_20210424_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='lightType',
            field=models.CharField(choices=[('floor lamp', 'floor lamp'), ('table lamp', 'table lamp'), ('ceiling light', 'ceiling light')], default='', max_length=20),
        ),
    ]
