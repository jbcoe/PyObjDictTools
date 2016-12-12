from obj_dict_tools import *


@dict_fields(['name', 'size'])
class Simple:

    def __init__(self, name=None, size=None):
        self.name = name
        self.size = size


@dict_fields(['first', 'second'])
class Pair:

    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second


def test_simple_class_to_dict():
    s = Simple('foo', 100)
    d = to_dict(s)

    assert d['__class__'] == 'Simple'
    assert d['name'] == 'foo'
    assert d['size'] == 100


def test_null_fields_to_dict():
    p = Pair()
    d = to_dict(p)

    assert d['__class__'] == 'Pair'
    assert not 'first' in d
    assert not 'second' in d


def test_list_to_dict():
    ss = [Simple('foo', 100), Simple('bar', 200)]
    d = to_dict(ss)

    assert len(d) == 2

    assert d[0]['__class__'] == 'Simple'
    assert d[0]['name'] == 'foo'
    assert d[0]['size'] == 100

    assert d[1]['__class__'] == 'Simple'
    assert d[1]['name'] == 'bar'
    assert d[1]['size'] == 200


def test_list_field_to_dict():
    p = Pair([1, 2, 3, 4, 5], Simple('b', 200))
    d = to_dict(p)

    assert d['__class__'] == 'Pair'
    assert len(d['first']) == 5
    assert d['second']['__class__'] == 'Simple'
    assert d['second']['name'] == 'b'
    assert d['second']['size'] == 200

