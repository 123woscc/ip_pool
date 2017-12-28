class SpiderError(Exception):
    def __init__(self, cls_name):
        self.cls_name = cls_name
        super().__init__()

    def __str__(self):
        return repr(f'The spider `{self.cls_name}` does not has func `gets`.')


class IPEmptyError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return repr('There are not more ips can use')
