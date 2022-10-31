from pyexpat import model
from django.db import models
from django.utils.translation import gettext as _


COUNTRY = [
    ('IN', 'Indonesia'),
    ('US', 'Unitid State')
]

AGES = [
    ('Male','Male'),
    ('Fimale', 'Fimale')
]

# Create your models here.
class Warga(models.Model):
    country = models.CharField(_("Negara Asal"), choices=COUNTRY, max_length=10)
    name = models.CharField(_('Nama'), max_length=255)
    gender = models.CharField(_('Jenis Kelamin'), choices=AGES, max_length=10)
    age = models.IntegerField(_('Usia'))
    address = models.CharField(_('Alamat'), max_length=255)
    
    class Meta:
        verbose_name = _("Warga Negara")
        