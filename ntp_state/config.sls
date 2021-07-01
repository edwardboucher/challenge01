include:
  - ntp.restart
ntp_service_config:
  file.replace:
  - name: /etc/ntp.conf
  - pattern:  |
      ^(.*)(server)(\s+)(.*)
  - repl: 'server 0.centos.pool.ntp.org iburst\n'
  - backup: true
  - append_if_not_found: true
  - not_found_content: 'server 0.centos.pool.ntp.org iburst'
  - require:
    - pkg: ntp

#update_ntp_conf:
#  file.append:
#    - name: /etc/ntp.conf
{#    - text: server {{ pillar['ntp']['server'] }} #}