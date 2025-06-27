from django.db import models
from django.utils.translation import gettext_lazy as _


class Example(models.Model):
    """Example"""

    name = models.CharField(
        max_length=100,
        db_index=True,
        default='',
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
