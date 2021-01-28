#do nodes have PIP installed?
python-pip:
  pkg.installed

requests:
  pip.installed:
    - require:
      - pkg: python-pip