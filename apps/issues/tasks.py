# -*- coding: utf-8 -*-
from apps.issues.models import Issue
from lxml import etree
from misc.tasks import TaskLockedMixin
from celery.task.base import PeriodicTask
import requests
import config_lmv


class ReadIssuesPeriodicTask(PeriodicTask, TaskLockedMixin):
    """
    Comprueba si hay ediciones nuevas de la revista para ser descargadas
    """
    name = "ReadIssuesPeriodicTask"
    run_every = config_lmv.LMV_TASK_CHECK_ISSUES

    def _do_task(self, *args, **kwargs):
        r = requests.get(config_lmv.LMV_URL_ISSUES)
        if r.status_code != 200:
            self.logger.error(u"No se ha podido leer '%s'" % config_lmv.LMV_URL_ISSUES)

        i = Issue()
        print i

        dom = etree.parse(r.text)
        for link in enumerate(dom.xpath('//a[contains(@href, "/issue/")]')):
            print link


    # def parse(self, response):
    #     dom = HtmlXPathSelector(response)

    #     numeros = []
    #     for index, link in enumerate(dom.select('//a[contains(@href, "/issue/")]')):
    #         href = link.select('@href').extract()[0]
    #         text = link.extract()

    #         item = LinkMagazineItem()
    #         item['number'] = int(href.split('/')[2])
    #         item['title'] = text
    #         item['link'] = 'http://www.linux-magazine.es' + href

    #         numeros.append(item)

    #     return numeros
