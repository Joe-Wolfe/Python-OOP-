"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        '''
            Creates a new Serial Generator with an optional starting value, that defaults to 0
        '''
        self.start = start
        self.value = start

    def generate(self):
        self.value += 1
        return self.value-1

    def reset(self):
        self.value = self.start
