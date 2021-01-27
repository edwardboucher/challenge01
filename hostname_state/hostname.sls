set_hostname:
  network.system:
    - enabled: True
    - hostname: minion1
    - apply_hostname: True
    - retain_settings: True