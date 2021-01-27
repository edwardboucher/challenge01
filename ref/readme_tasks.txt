1. Create an ntp state which installs the ntp package.
2. Add the ntp service to your ntp state and make sure it is running and enabled.
3. Create a state which runs ntpdate 0.centos.pool.ntp.org to force a time sync
4. Put your ntp states into a formula
5. Add an ntp configuration file with ntp servers set by a variable
6. Use pillar for all variables in your ntp states
7. Create an orchestration file that installs ntp, initializes using ntpdate, then starts the ntp service
8. Have your state from #3 also set a custom grain called ntp_initalized to True
9. Create a custom execution module to list the currently configured ntp servers