# Generated by Django 3.0.1 on 2019-12-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiDisplay',
            fields=[
                ('iddisplay', models.AutoField(primary_key=True, serialize=False)),
                ('id_display_trademark', models.IntegerField()),
                ('display_resolution', models.CharField(max_length=50)),
                ('display_reference', models.CharField(max_length=50)),
                ('display_serial', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='TiComputer',
        ),
    ]