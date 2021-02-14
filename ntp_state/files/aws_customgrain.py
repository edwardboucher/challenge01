#!/usr/bin/env python
import requests
def my_custom_aws_grain(aws_key = "instance-id"):
    metaurl = 'http://169.254.169.254/1.0/meta-data/'
    url = metaurl+aws_key
    r = requests.get(url)
    out = r.text
    my_grain = {'aws_'+aws_key: out}
    return my_grain
def main():
    # initialize a grains dictionary
    grains = {}
    grains['my_grains'] = my_custom_aws_grain()
    return grains