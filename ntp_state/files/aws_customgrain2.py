#!/usr/bin/env python

import httplib2
import os

DEVICE_MAPPING_URI = 'http://169.254.169.254/latest/meta-data/block-device-mapping/'

def detect_devs():
    dev_list = [ x for x in os.listdir('/sys/block')
                 if x.startswith('xvd') or x.startswith('sd') ]
    return dev_list

def _metadata_call(url):
    try:
        #http = httplib2.Http()
        #conn = httplib2.request("169.254.169.254", 80, timeout=1)
        #conn.request('GET', url)
        h = httplib2.Http()
        out= h.request(url)
        response = (out[0])
        #response = conn.getresponse()
        if (out[0]).status != 200:
            return
        return out[1]
    except:
        return

def _get_block_devices():
    block_device_grain = { 'ephemeral': [], 'ebs': [] }
    detected_devs = detect_devs()
    for mapping in ((_metadata_call(DEVICE_MAPPING_URI)).decode("utf-8")).split('\n'):
        device = _metadata_call(DEVICE_MAPPING_URI + mapping)
        if mapping.startswith('ephemeral'):
            for dev in detected_devs:
                if dev[-1] == device[-1]:
                    block_device_grain['ephemeral'].append(dev)
        elif mapping.startswith('ebs'):
            for dev in detected_devs:
                if dev[-1] == device[-1]:
                    block_device_grain['ebs'].append(dev)
    return block_device_grain


def main():
    grains = {}
    grains['block_devices'] = _get_block_devices()
    return grains