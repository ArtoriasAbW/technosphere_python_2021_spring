class CustomMeta(type):

    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items()
                 if not name.startswith('__'))
        magic_attrs = dict(((name, value) for name, value in dct.items()
                            if name.startswith('__')))
        custom_attrs = dict(("custom_" + name, value) for name, value in attrs)
        custom_attrs.update(magic_attrs)
        return type.__new__(cls, name, bases, custom_attrs)
