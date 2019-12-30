from django.db import models


# Create your models here.

class TiComputer(models.Model):
    idcomputer = models.AutoField(primary_key=True)
    cp_name = models.CharField(max_length=45)
    cp_description = models.TextField()
    cp_licence_windows = models.CharField(max_length=30)
    cp_licence_office = models.CharField(max_length=30)
    id_tower = models.ForeignKey('TiTower', models.DO_NOTHING, db_column='id_tower')
    id_display = models.ForeignKey('TiDisplay', models.DO_NOTHING, db_column='id_display')
    id_keyboard = models.ForeignKey('TiKeyboard', models.DO_NOTHING, db_column='id_keyboard')
    id_mouse = models.ForeignKey('TiMouse', models.DO_NOTHING, db_column='id_mouse')
    id_operating_system = models.ForeignKey('TiOperatingSystem', models.DO_NOTHING, db_column='id_operating_system')
    id_office = models.ForeignKey('TiOffice', models.DO_NOTHING, db_column='id_office')
    cp_other_software = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_responsible = models.ForeignKey('TiResponsible', models.DO_NOTHING, db_column='id_responsible')

    class Meta:
        db_table = 'ti_computer'


class TiDisplay(models.Model):
    iddisplay = models.AutoField(primary_key=True)
    id_display_trademark = models.IntegerField()
    display_resolution = models.CharField(max_length=50)
    display_reference = models.CharField(max_length=50)
    display_serial = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_display'


class TiKeyboard(models.Model):
    idkeyboard = models.AutoField(primary_key=True)
    id_kb_trademark = models.IntegerField()
    kb_reference = models.CharField(max_length=50)
    kb_serial = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_keyboard'


class TiMouse(models.Model):
    idmouse = models.AutoField(primary_key=True)
    id_mouse_trademark = models.IntegerField()
    mouse_reference = models.CharField(max_length=50)
    mouse_serial = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_mouse'


class TiOffice(models.Model):
    idti_office = models.AutoField(primary_key=True)
    office_name = models.CharField(max_length=50)
    office_version = models.FloatField()
    office_reference = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_office'


class TiOperatingSystem(models.Model):
    idti_operating_system = models.AutoField(primary_key=True)
    os_name = models.CharField(max_length=50)
    os_version = models.FloatField()
    os_reference = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_operating_system'


class TiPosition(models.Model):
    idti_position = models.AutoField(primary_key=True)
    position_description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'ti_position'


class TiResponsible(models.Model):
    idti_responsible = models.AutoField(primary_key=True)
    rp_name = models.CharField(max_length=50)
    rp_dni = models.BigIntegerField()
    id_position = models.ForeignKey(TiPosition, models.DO_NOTHING, db_column='id_position')

    class Meta:
        db_table = 'ti_responsible'


class TiTower(models.Model):
    idti_tower = models.AutoField(primary_key=True)
    tower_description = models.TextField()
    tower_reference = models.CharField(max_length=50)
    tower_serial = models.CharField(max_length=50)
    id_type = models.IntegerField()
    id_tower_trademark = models.IntegerField()
    id_processor = models.IntegerField()
    id_hard_disk = models.IntegerField()
    id_ram = models.IntegerField(db_column='id_RAM')  # Field name made lowercase.
    id_cd_player = models.IntegerField(db_column='id_CD_player')  # Field name made lowercase.
    id_changer = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ti_tower'
