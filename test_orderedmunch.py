from munch import OrderedMunch
from munch._compat import OrderedDict


def test_orderedmunch():
    b = OrderedMunch([
        ('foo', OrderedMunch([('lol', True)])),
        ('hello', 42),
        ('ponies', 'are pretty')
    ])
    b.bar = 'baz'
    assert tuple(b.keys()) == ('foo', 'hello', 'ponies', 'bar')
    assert tuple(b.values()) == (
        OrderedMunch([('lol', True)]),
        42,
        'are pretty',
        'baz',
    )

    munched = OrderedMunch.munchify([
        OrderedDict([
            ('foo', OrderedDict([('lol', True)])),
            ('hello', 42),
            ('ponies', 'are pretty'),
            ('bar', 'baz')
        ])
    ])
    assert munched == [b]

    assert list(OrderedMunch.unmunchify(b).items()) == [('foo', OrderedDict([('lol', True)])), ('hello', 42), ('ponies', 'are pretty'), ('bar', 'baz')]
