include:
  - ntp.restart
ntp_service_config:
  file.managed:
    - name: /etc/ntp.conf
    - source: salt://ntp/files/ntp.conf
    - require:
      - pkg: ntp