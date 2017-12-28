import requests
from pyquery import PyQuery as pq
import telnetlib


def get_doc(url, headers=None):
    if headers:
        headers = headers
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }
    html = requests.get(url, headers=headers)
    doc = pq(html.text)
    return doc


def check_ip(ip_port, timeout=3):
    ip = ip_port.split(':')[0]
    port = ip_port.split(':')[-1]
    try:
        telnetlib.Telnet(ip, port, timeout)
        return False
    except:
        return True
