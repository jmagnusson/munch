try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict  # noqa
    except ImportError:
        class OrderedDict(dict):
            def __init__(self, *args, **kwargs):
                raise Exception('OrderedDict not available')
