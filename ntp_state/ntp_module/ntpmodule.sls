#do nodes have PIP installed?
python3-pip:
  pkg.installed

requests:
  pip.installed:
    - require:
      - pkg: python3-pip