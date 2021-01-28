#!/usr/bin/env python
def my_custom_ntp_grain():
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
def main():
    # initialize a grains dictionary
    grains = {}
    grains['my_grains'] = my_custom_ntp_grain()
    return grains