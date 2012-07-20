# -*- coding: utf-8 -*-
from apps.issues.models import Issue
from misc.factories import xmlDoc_from_html
from misc.tasks import BasePeriodicTask
import requests
import config_lmv


class ReadIssuesPeriodicTask(BasePeriodicTask):
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

        dom = xmlDoc_from_html(r.text)
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
