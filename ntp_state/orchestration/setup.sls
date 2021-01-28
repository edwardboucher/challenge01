set_hostname:
  salt.function:
    - name: network.mod_hostname
    - tgt: 'salt'
    - arg:
      - salt
install_ntp_service:
   salt.state:
     - tgt: 'salt'
     - highstate: True
configure_ntp_service:
   salt.state:
     - tgt: 'salt'
     - sls:
       - ntp