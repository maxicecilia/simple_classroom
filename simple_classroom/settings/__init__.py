""" Specify the other settings files to load. """

try:
    from .base import *
except ImportError:
    pass

# local overrides go last so they have top priority
try:
    from .local import *
except ImportError, e:
    # print 'Unable to load local.py:', e
    pass
