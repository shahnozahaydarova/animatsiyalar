# Generated by Django 4.1.4 on 2023-01-12 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_maishiytehnikalar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barchatoifalar',
            options={'verbose_name': 'Barcha Mahsulot turlari'},
        ),
        migrations.AlterModelOptions(
            name='maishiytehnikalar',
            options={'verbose_name': 'Maishiy Tehnika', 'verbose_name_plural': 'Maishiy Tehnikalar'},
        ),
        migrations.AlterModelOptions(
            name='maishiytehnikalarsoni',
            options={'verbose_name': 'Maishiy Tehnikalar soni', 'verbose_name_plural': 'Maishiy Tehnikalar soni'},
        ),
        migrations.AlterModelOptions(
            name='mebellar',
            options={'verbose_name': 'Mebel', 'verbose_name_plural': 'Mebellar'},
        ),
        migrations.AlterModelOptions(
            name='mebellarsoni',
            options={'verbose_name': 'Mebellar soni', 'verbose_name_plural': 'Mebellar soni'},
        ),
    ]
