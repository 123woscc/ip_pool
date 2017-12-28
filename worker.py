from db import RedisPool
from spider import SpiderMeta
from concurrent import futures
from checker import IPChecker
from errors import IPEmptyError
from config import IP_MAX


class PoolAdder():
    def __init__(self):
        self._pool = RedisPool()
        self._checker = IPChecker()
        self._ip_max = IP_MAX

    def is_over(self):
        return True if self._pool.size >= self._ip_max else False

    def add_to_pool(self):
        flag = 0
        print('PoolAdder is working')
        spiders = [cls() for cls in SpiderMeta.spiders]
        while not self.is_over():
            flag += 1
            raw_ips = []
            with futures.ThreadPoolExecutor(max_workers=len(spiders)) as executor:
                future_to_down = {executor.submit(spiders[i].gets): i for i in range(len(spiders))}
                for future in futures.as_completed(future_to_down):
                    raw_ips.extend(future.result())
            print(raw_ips)
            self._checker.set_raw_ips(raw_ips)
            self._checker.check_ips()
            ips = self._checker.usable_ips
            if len(ips) != 0:
                self._pool.puts(ips)
            if self.is_over():
                break
            if flag >= 10:
                raise IPEmptyError
