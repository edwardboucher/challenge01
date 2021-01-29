import logging
import subprocess
try:
    import os
    HAS_OS = True
except ImportError:
    HAS_OS = False

log = logging.getLogger(__name__)

__virtual_name__ = 'ntpmodule'

def __virtual__():
    '''
    Only load ntpmodule if os package is available
    '''
    if HAS_OS:
        return __virtual_name__
    else:
        return False, 'The ntpmodule module cannot be loaded: os package unavailable, check pip.'

def get():
    return_value = {}
    output = subprocess.check_output("sudo service ntpd status | grep Active",shell=True)
    return output

def _interrogate_service():
    output = subprocess.check_output("sudo service ntpd status | grep Active",shell=True)
    return output