from jsonmodels.collections import ModelCollection
from jsonmodels.fields import ListField

from funcy import iterable, suppress

class LazyModelCollection(ModelCollection):

    def _repr(self):
        return super(LazyModelCollection, self).__repr__()

    def __repr__(self):
        # TODO if self is empty, then change repr
        n = len(self)
        s = 's' if n != 1 else ''

        items_types = '(' + ', '.join(t.__name__ for t in self.field.items_types) + ')'
        msg = '[...lazy list of types {items_types}...]'
        return msg.format(n=n, s=s, items_types=items_types)

    def __getitem__(self, key):
        lazy_item = super(LazyModelCollection, self).__getitem__(key)
        with suppress(Exception):
            lazy_item.get()
        return lazy_item


class LazyListField(ListField):

    #def __get__(self, instance, owner):
    #    if

    def get_default_value(self):
        return LazyModelCollection(self)

    def parse_value(self, values):
        """Cast value to proper collection."""
        collection = self.get_default_value()

        if not iterable(values):
            values = [values]
        for value in values:
            collection.append(self._cast_value(value))

        return collection
