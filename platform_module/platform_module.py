import platform
import subprocess

try:
    import platform
    HAS_OS = True
except ImportError:
    HAS_OS = False

log = logging.getLogger(__name__)

__virtual_name__ = 'platform_module'


def get():
    return_value = {}
    output = subprocess.check_output("platform.dist()",shell=True)
    return output

def _interrogate_service():
    output = subprocess.check_output("platform.dist()",shell=True)
    return output