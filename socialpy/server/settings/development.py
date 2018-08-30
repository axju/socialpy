from .base import *

DEBUG = True

MIDDLEWARE += ['socialpy.server.utils.AutomaticLoginUserMiddleware', ]
