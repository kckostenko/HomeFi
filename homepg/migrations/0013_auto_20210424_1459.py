# Generated by Django 3.2 on 2021-04-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepg', '0012_alter_light_lighttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='light',
            name='roomLoc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepg.room'),
        ),
        migrations.AddField(
            model_name='lock',
            name='roomLoc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepg.room'),
        ),
    ]