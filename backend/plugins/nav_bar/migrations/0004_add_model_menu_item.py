# Generated by Django 2.2.14 on 2020-07-18 20:04

from django.db import migrations, models
import django.db.models.deletion
import linkit.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('nav_bar', '0003_add_field_is_use_default_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItemModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='nav_bar_menuitemmodel', serialize=False, to='cms.CMSPlugin')),
                ('link', linkit.model_fields.LinkField(allow_label=True, allow_no_follow=True, allow_target=True, name='link', types=['djangocms_blog', 'page', 'file', 'input'])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='navbarpluginmodel',
            name='is_full_width',
            field=models.BooleanField(default=False, verbose_name='Enable full-width mode'),
        ),
    ]
