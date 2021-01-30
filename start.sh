echo "Running tplc-reboot.sh on $(date)"
# DRIVER_LOCATION=$(dpkg -L firefox-geckodriver | sed '4q;d') in the webdriver
TPLC_MAC='98:da:c4:f6:03:fa'
TPLC_IP=$(/usr/sbin/arp -a | grep $TPLC_MAC | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}')
echo "TPLC IP found from arp: $TPLC_IP"
TPLC_IP=${TPLC_IP:-'192.168.0.93'}
echo "Using TPLC IP: $TPLC_IP"
MOZ_HEADLESS=1
python3 ~/workspace/tplc-reboot/tplc-reboot-webdriver.py $TPLC_IP
