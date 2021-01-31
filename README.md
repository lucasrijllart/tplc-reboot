# tplc-reboot

My TP-Link TL-WPA4220 performs better when rebooted regularly. This script uses selenium to
navigate to its web portal and click the reboot button.

The script is called using cron as follows:
```
00 06 * * * bash ~/workspace/tplc-reboot/start.sh >> /tmp/tplc-reboot.log 2>&1
```
