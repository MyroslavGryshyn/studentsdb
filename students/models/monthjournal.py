# -*- coding: utf-8 -*-
from django.db import models

class MonthJournal(models.Model):
    """Student monthly journal"""

    class Meta(object):
        verbose_name = u"Місячний журнал"
        verbose_name_plural = u"Місячний журнал"

    student = models.ForeignKey('Student',
        verbose_name=u"Студент",
        blank=False,
        unique_for_month='date')

    student = models.ForeignKey('Student',
        verbose_name=u'Студент',
        blank=False,
        unique_for_month='date')

    # we only need year and month, so always set day to first day of the month
    date = models.DateField(
        verbose_name=u'Дата',
        blank=False)

    # list of days, each says whether student was present or not
    present_day = [models.BooleanField(default=False) for x in range(31)]


    def __unicode__(self):
        return u'%s: %d, %d' % (self.student.last_name, self.date.month, \
                                self.date.year)
