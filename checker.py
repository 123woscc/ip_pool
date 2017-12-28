import asyncio
import aiohttp


class IPChecker():
    test_api = 'https://www.baidu.com'

    def __init__(self):
        self.raw_ips = None
        self.out_ips = None

    def set_raw_ips(self, raw_ips):
        self.raw_ips = raw_ips
        self._out_ips = []

    async def check_ip(self, ip_port):
        async with aiohttp.ClientSession() as sess:
            try:
                real_proxy = 'http://' + ip_port
                async with sess.get(self.test_api, proxy=real_proxy, timeout=15) as resp:
                    self._out_ips.append(ip_port)
            except Exception as e:
                print(e)

    def check_ips(self):
        print('Checking ip_port...')
        loop = asyncio.get_event_loop()
        tasks = [self.check_ip(ip) for ip in self.raw_ips]
        loop.run_until_complete(asyncio.wait(tasks, loop=loop))

    @property
    def usable_ips(self):
        return self._out_ips
