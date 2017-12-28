from db import RedisPool
from worker import PoolAdder
from multiprocessing import Process
import time
from checker import IPChecker
from config import IP_MIN


class ExpireCheckProcess(Process):
    def __init__(self, cycle):
        super().__init__()
        self._cycle = cycle
        self._checker = IPChecker()

    def run(self):
        pool = RedisPool()
        print('Expire Check Process is working..')
        while True:
            time.sleep(self._cycle)
            total = int(0.25 * pool.size)
            if total < 4:
                continue
            raw_ips = pool.gets(total)
            self._checker.set_raw_ips(raw_ips)
            self._checker.check_ips()
            ips = self._checker.usable_ips
            if len(ips) != 0:
                pool.puts(ips)


class ProxyCountCheckProcess(Process):
    print('Proxy Count Check Process is working..')

    def __init__(self, cycle):
        super().__init__()
        self._ip_min = IP_MIN
        self._cycle = cycle

    def run(self):
        worker = PoolAdder()
        pool = RedisPool()
        while True:
            if pool.size < self._ip_min:
                worker.add_to_pool()
            time.sleep(self._cycle)
