# Generated by Django 2.2.11 on 2020-03-27 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionWithImageBackgroundPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='section_with_image_background_sectionwithimagebackgroundpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(help_text='For displaying in the plugin tree', max_length=512)),
                ('height', models.IntegerField(default=350, help_text='In pixels')),
                ('background_image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]