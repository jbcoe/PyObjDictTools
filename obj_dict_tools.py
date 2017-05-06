def to_dict(obj):
    if hasattr(obj, '_to_dict'):
        return obj._to_dict()
    if isinstance(obj, tuple):
        return [to_dict(x) for x in obj]
    if isinstance(obj, list):
        return [to_dict(x) for x in obj]
    if isinstance(obj, dict):
        return {to_dict(k):to_dict(v) for k,v in obj.items()}
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return obj
    if isinstance(obj, float):
        return obj
    raise Exception('unhandled type \'{}\''.format(type(obj).__name__))


def from_dict(var, m=globals()):
    if isinstance(var, dict) and '__class__' in var:
        cls = m[var['__class__']]
        if cls:
            return cls._from_dict({k: from_dict(v, m) 
                                   for k, v in var.items() 
                                   if not k.startswith('_')})
    if isinstance(var, dict):
        return {from_dict(k):from_dict(v) for k,v in var.items()}
    if isinstance(var, list):
        return [from_dict(x, m) for x in var]
    return var


def dict_fields(attributes):
    def wrapper(klass):
        for a in attributes:
            assert not a.startswith('_')

        def _from_dict(cls, d):
            return cls(**d)

        def _to_dict(self):
            d = {'__class__': self.__class__.__name__}
            for a in attributes:
                v = getattr(self, a)
                if not v is None:
                    d[a] = to_dict(getattr(self, a))
            return d

        klass._from_dict = classmethod(_from_dict)
        klass._to_dict = _to_dict
        return klass

    return wrapper
