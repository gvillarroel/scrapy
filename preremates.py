from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
import unicodedata

class ElectronicsSpider(CrawlSpider):
    name = "pre-remates"
    allowed_domains = ["preremates.cl"]
    start_urls = [
        'http://preremates.cl/content/proximos-remates'
    ]

    def parse(self, response):
        for detalle in response.css(".row"):
            date = unicodedata.normalize('NFKD', u"\n".join(detalle.css("span.aviso-fecha::text").extract())).encode("iso-8859-15",'ignore')
            desc = unicodedata.normalize('NFKD', u"\n".join(detalle.css("div.aviso-texto::text").extract())).encode("iso-8859-15",'ignore')
            yield {"url":str(response.url), "desc": desc, "date":date}

        for link in response.css(".ktkPageLinks a::attr(href)"):
            l = str(link.extract())
            if l.startswith("/content/proximos-remates"):
                yield response.follow( l, self.parse )
