# Generated by Django 3.0.1 on 2019-12-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0004_tikeyboard_timouse_tioffice_tioperatingsystem_tiposition_tiresponsible_titower'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiComputer',
            fields=[
                ('idcomputer', models.AutoField(primary_key=True, serialize=False)),
                ('cp_name', models.CharField(max_length=45)),
                ('cp_description', models.TextField()),
                ('cp_licence_windows', models.CharField(max_length=30)),
                ('cp_licence_office', models.CharField(max_length=30)),
                ('cp_other_software', models.TextField(blank=True, null=True)),
                ('id_display', models.ForeignKey(db_column='id_display', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiDisplay')),
                ('id_keyboard', models.ForeignKey(db_column='id_keyboard', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiKeyboard')),
                ('id_mouse', models.ForeignKey(db_column='id_mouse', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiMouse')),
                ('id_office', models.ForeignKey(db_column='id_office', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiOffice')),
                ('id_operating_system', models.ForeignKey(db_column='id_operating_system', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiOperatingSystem')),
                ('id_responsible', models.ForeignKey(db_column='id_responsible', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiResponsible')),
                ('id_tower', models.ForeignKey(db_column='id_tower', on_delete=django.db.models.deletion.DO_NOTHING, to='computer.TiTower')),
            ],
            options={
                'db_table': 'ti_computer',
            },
        ),
    ]
