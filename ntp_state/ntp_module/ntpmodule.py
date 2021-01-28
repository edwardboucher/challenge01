import logging
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
def _make_request():
    service = "ntpd"
    p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    output_str=output.encode('ascii','ignore')
    try:
        output_str.index('active')
    except ValueError:
        my_grain = {'ntp_initialized': 'False'}
    else:
        my_grain = {'ntp_initialized': 'True'}
    return my_grain