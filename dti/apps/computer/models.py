from django.db import models


# Create your models here.

class TiComputer(models.Model):
    idcomputer = models.AutoField(primary_key=True)
    cp_name = models.CharField(max_length=45)
    cp_description = models.TextField()
    cp_licence_windows = models.CharField(max_length=50)
    cp_licence_office = models.CharField(max_length=50)
    id_computer_brand = models.ForeignKey('TiBrand', models.DO_NOTHING, db_column='id_computer_brand')
    id_tower = models.ForeignKey('TiTower', models.DO_NOTHING, db_column='id_tower')
    id_monitor = models.ForeignKey('TiMonitor', models.DO_NOTHING, db_column='id_monitor')
    id_keyboard = models.ForeignKey('TiKeyboard', models.DO_NOTHING, db_column='id_keyboard')
    id_mouse = models.ForeignKey('TiMouse', models.DO_NOTHING, db_column='id_mouse')
    id_operating_system = models.ForeignKey('TiOperatingSystem', models.DO_NOTHING, db_column='id_operating_system')
    id_office = models.ForeignKey('TiOffice', models.DO_NOTHING, db_column='id_office')
    cp_other_software = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_responsible = models.ForeignKey('TiResponsible', models.DO_NOTHING, db_column='id_responsible')

    class Meta:
        db_table = 'ti_computer'


class TiMonitor(models.Model):
    idmonitor = models.AutoField(primary_key=True)
    id_monitor_brand = models.ForeignKey('TiBrand', models.DO_NOTHING, db_column='id_monitor_brand')
    monitor_size = models.FloatField()
    monitor_reference = models.CharField(max_length=50)
    monitor_serial = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_monitor'


class TiKeyboard(models.Model):
    idkeyboard = models.AutoField(primary_key=True)
    id_kb_brand = models.ForeignKey('TiBrand', models.DO_NOTHING, db_column='id_kb_brand')
    kb_reference = models.CharField(max_length=50)
    kb_serial = models.CharField(max_length=50)

    class Meta:
        db_table = 'ti_keyboard'


class TiMouse(models.Model):
    idmouse = models.AutoField(primary_key=True)
    id_mouse_brand = models.ForeignKey('TiBrand', models.DO_NOTHING, db_column='id_mouse_brand')
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
    id_tower_brand = models.ForeignKey('TiBrand', models.DO_NOTHING, db_column='id_tower_brand')
    id_processor = models.IntegerField()
    id_hard_disk = models.IntegerField()
    id_ram = models.IntegerField(db_column='id_RAM')  # Field name made lowercase.
    id_cd_player = models.IntegerField(db_column='id_CD_player')  # Field name made lowercase.
    id_changer = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ti_tower'


class TiBrand(models.Model):
    idti_brand = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ti_brand'
