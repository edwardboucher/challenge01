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
        h = httplib2.Http()
        out= h.request(url)
        response = (out[0])
        if (out[0]).status != 200:
            return
        return out[1]
    except:
        return

def _get_block_devices():
    block_device_grain = { 'ephemeral': [], 'ebs': [], 'ami': [], 'root': []  }
    detected_devs = detect_devs()
    devices_map=((_metadata_call(DEVICE_MAPPING_URI)).decode("utf-8")).split('\n')
    for mapping in devices_map:
        device = _metadata_call(DEVICE_MAPPING_URI + mapping).decode("utf-8")
        if mapping.startswith('ephemeral'):
            print(dev)
            for dev in detected_devs:
                print(dev)
                if dev[-1] == device[-1]:
                    block_device_grain['ephemeral'].append(device)
        if mapping.startswith('ebs'):
            for dev in detected_devs:
                print(dev)
                if dev[-1] == device[-1]:
                    block_device_grain['ebs'].append(device)
        if mapping.startswith('ami'):
            for dev in detected_devs:
                print(dev)
                block_device_grain['ami'].append(device)
        if mapping.startswith('root'):
            for dev in detected_devs:
                print(dev)
                block_device_grain['root'].append(device)
        return block_device_grain


def main():
    grains = {}
    grains['block_devices'] = _get_block_devices()
    return grains