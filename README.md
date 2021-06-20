# tplc-reboot

My TP-Link TL-WPA4220 performs better when rebooted regularly. This script uses selenium to
navigate to its web portal and click the reboot button.

## Installation

To use this script, please clone the repo then install the necessary third-party libraries:
```
git clone https://github.com/lucasrijllart/tplc-reboot.git
pip3 install selenium
sudo apt install firefox-esr
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz
sudo tar -xzvf geckodriver-v0.23.0-arm7hf.tar.gz -C /usr/bin/; rm geckodriver-v0.23.0-arm7hf.tar.gz
# export PATH=$PATH:/usr/bin/geckodriver maybe not needed
```

You can test the script by running: `bash start.sh`

The script is called using cron as follows:
```
00 06 * * * bash ~/workspace/tplc-reboot/start.sh >> /tmp/tplc-reboot.log 2>&1
```

Tested with
```
selenium 3.141.0
firefox-esr 78.11.0esr-1~deb10u1+rpi1
```
