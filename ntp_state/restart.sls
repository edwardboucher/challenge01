ntp_restart:
   module.wait:
     - name: service.restart
     - m_name: ntp
     - onchanges:
       - ntp_service_config