from schedule import ProxyCountCheckProcess, ExpireCheckProcess
from config import VALID_CHECK_CYCLE, POOL_LEN_CHECK_CYCLE


def main():
    p1 = ProxyCountCheckProcess(POOL_LEN_CHECK_CYCLE)
    p2 = ExpireCheckProcess(VALID_CHECK_CYCLE)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
