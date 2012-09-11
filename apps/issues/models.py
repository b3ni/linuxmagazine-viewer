# -*- coding: utf-8 -*-
from django.db import models
from config_lmv import LMV_URL_BASE


class Issue(models.Model):
    cover_title = models.CharField(u"cover title", max_length=50)
    number = models.IntegerField()

    class Crawler:
        url = LMV_URL_BASE + 'issue/{number}'

        def cover_title_crawl(self, page):
            pass

        def number_crawl(self, page):
            pass
