import platform
import subprocess

try:
    import platform
    HAS_OS = True
except ImportError:
    HAS_OS = False

log = logging.getLogger(__name__)

__virtual_name__ = 'platform_module'

def __virtual__():
    '''
    Only load platform_module if os package is available
    '''
    if HAS_OS:
        return __virtual_name__
    else:
        return False, 'The platform_module module cannot be loaded: os package unavailable, check pip.'

def get():
    return_value = {}
    output = subprocess.check_output("platform.dist()",shell=True)
    return output

def _interrogate_service():
    output = subprocess.check_output("platform.dist()",shell=True)
    return output