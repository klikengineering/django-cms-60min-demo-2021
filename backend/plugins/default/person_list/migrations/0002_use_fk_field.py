# Generated by Django 2.2.12 on 2020-05-02 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpluginmodel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_list.Person'),
        ),
    ]