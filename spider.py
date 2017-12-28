from utils import get_doc
from errors import SpiderError


class SpiderMeta(type):
    spiders = []

    def __new__(meta, name, bases, class_dict):
        if 'gets' not in class_dict:
            raise SpiderError(name)
        cls = type.__new__(meta, name, bases, class_dict)
        SpiderMeta.spiders.append(cls)
        return cls


class XiciSpider(metaclass=SpiderMeta):
    def gets(self):
        urls = ['http://www.xicidaili.com/nn/{}'.format(i) for i in range(1, 2)]
        ips = []
        for url in urls:
            doc = get_doc(url)
            trs = doc('#ip_list tr')
            for tr in trs.items():
                ip = tr.find('td:nth-child(2)').text()
                port = tr.find('td:nth-child(3)').text()
                if ip and port:
                    ip_port = '{}:{}'.format(ip, port)
                    ips.append(ip_port)
        return ips


class KuaidailiSpider(metaclass=SpiderMeta):
    def gets(self):
        urls = ['http://www.66ip.cn/{}.html'.format(i) for i in range(1, 2)]
        ips = []
        for url in urls:
            doc = get_doc(url)
            trs = doc('#main table tr:not(:first-child)')
            for tr in trs.items():
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                if ip and port:
                    ip_port = '{}:{}'.format(ip, port)
                    ips.append(ip_port)
        return ips
