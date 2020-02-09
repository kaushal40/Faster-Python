"""Example on profiling memory"""

from datetime import datetime
from collections import namedtuple
from itertools import cycle, islice

Event = namedtuple('Event', ['type', 'time', 'user', 'url', 'site'])


class EncodeError(Exception):
    pass


class Encoder:
    """Event encoder"""
    def __init__(self, stream):
        self.stream = stream
        self._fields = {
            'click': ['time', 'user'],
            'view': ['time', 'user', 'url'],
            'enter': ['user', 'url', 'site'],
        }

    def encode(self, event):
        """Encode event to stream"""
        fields = self._fields.get(event.type)
        if not fields:
            raise EncodeError('unknown event type: {}'.format(event.type))

        self.stream.write('{}'.format(len(fields)))
        for field in fields:
            value = getattr(event, field)
            if isinstance(value, datetime):
                value = value.isoformat()
            self.stream.write('|{}={}'.format(field, value))
        stream.write('\n')


def encode_event(event, stream):
    """Encode event to stream"""
    enc = Encoder(stream)
    # we call the encode  method 
    return enc.encode(event)


if __name__ == '__main__':
    import tracemalloc
    from tempfile import NamedTemporaryFile

    # Generate test cases
    # we are crating sample test cases to test out code KP 
    events = []
    for typ in ('click', 'view', 'enter'):
        events.append(
            Event(typ, datetime.now(), 'bugs', '/buy/carrot', 'acme.com'))

    events = islice(cycle(events), 1000)
    stream = NamedTemporaryFile(mode='wt', delete=False)
    print('encoding to {}'.format(stream.name))

    # started tracing the memory allocation
    tracemalloc.start()

    for event in events:
        encode_event(event, stream)

    # this is to print the statistic KP 
    snapshot = tracemalloc.take_snapshot()
    for stat in snapshot.statistics('lineno')[:10]:
        print(stat)

# python enc.py