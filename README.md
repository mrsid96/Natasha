# Natasha
AI powered bot for smart home automation

###
NEW THINGS TO DO 
###


1. Expand File System


2. Enable SSH from the raspberry pi


2.5 Installing Necessary Packages


sudo apt-get install swig python-dev libpulse-dev


sudo apt-get install alsa-tools alsa-utils


sudo apt-get install gstreamer0.10-pulseaudio libao4 libasound2-plugins libgconfmm-2.6-1c2 libglademm-2.4-1c2a libpulse-dev libpulse-mainloop-glib0 libpulse-mainloop-glib0-dbg libpulse0 libpulse0-dbg libsox-fmt-pulse paman paprefs pavucontrol pavumeter pulseaudio pulseaudio-dbg pulseaudio-esound-compat pulseaudio-esound-compat-dbg pulseaudio-module-bluetooth pulseaudio-module-gconf pulseaudio-module-jack pulseaudio-module-lirc pulseaudio-module-lirc-dbg pulseaudio-module-x11 pulseaudio-module-zeroconf pulseaudio-module-zeroconf-dbg pulseaudio-utils oss-compat -y


3. Intall pyaudio
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install pyaudio


--- USB SOUND CARD --


sudo nano /usr/share/alsa/alsa.conf
Change bellow two lines:
defaults.ctl.card 0 -> 1
defaults.pcm.card 0 -> 1


sudo nano ~/.asoundrc


pcm.!default {
 type hw 
 card 1
}
ctl.!default {
 type hw 
 card 1
}


4. PocketSphinx


Download Git


sudo apt-get install git -y


Download and compile the PocketSphinx source code


git clone https://github.com/cmusphinx/sphinxbase.git


sudo apt-get install autoconf libtool automake bison-y


cd ~/sphinxbase


./autogen.sh 
./configure
make clean all
make check
sudo make install
Note: After compilation I observed sphinxbase failed 1 unit test. I ignored the unit test result and continued on.


git clone https://github.com/cmusphinx/pocketsphinx.git


cd ~/pocketsphinx


./autogen.sh 
./configure
make clean all
make check
sudo make install


Running the PocketSpinx Ruby gem
Before you can execute the pocketsphinx-ruby gem it is necessary to set the library paths e.g. :


LD_LIBRARY_PATH=/home/pi/sphinxbase/src/libsphinxbase/.libs/:/home/pi/sphinxbase/src/libsphinxad/.libs/:/home/pi/pocketsphinx/src/libpocketsphinx/.libs/
export LD_LIBRARY_PATH


5. LAMP
apache:
sudo apt-get install apache2 -y
php:
sudo apt-get install php5 libapache2-mod-php5 -y
mysql:
sudo apt-get install mysql-server php5-mysql -y
phpmyadmin:
sudo apt-get install phpmyadmin
edit : sudo nano /etc/apache2/apache2.conf then add at the end:
Include /etc/phpmyadmin/apache.conf


6.Pico TTS:
	sudo apt-get install libttspico-utils


7.Chatterbot:
	sudo pip install chatterbot


8.SimpleJSON:
	sudo pip install simplejson


9.Open Weather map:
	sudo pip install pyowm


10.Wikipedia:
	sudo pip install wikipedia


10.5 News:
  sudo apt-get install libxml2-dev libxslt1-dev python-dev
  sudo apt-get install python-lxml


11.MySQL python DB:
	sudo apt-get install python-mysqldb


12. Install OpneCV
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libatlas-base-dev gfortran
sudo pip install numpy
sudo apt-get install python-opencv




13. PulseAudio Erros 


from /usr/share/alsa/alsa.conf, remove:


pcm.rear cards.pcm.rear
pcm.center_lfe cards.pcm.center_lfe
pcm.side cards.pcm.side
pcm.hdmi cards.pcm.hdmi
pcm.modem cards.pcm.modem
pcm.phoneline cards.pcm.phoneline


14. Static IP


edit sudo nano /etc/dhcpcd.conf file and add the following : 


interface wlan0
static ip_address=192.168.0.143
static routers=192.168.0.125
static domain_name_servers=8.8.8.8


15.Connect pi to wifi:
	a. sudo nano /etc/network/interfaces
	b. copy the bellow in it:




auto lo


iface lo inet loopback
iface eth0 inet dhcp


auto wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf


	c. sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	d. copy the bellow to it


ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1


network={
        ssid="NETGEAR"
        psk="nist#nist"
        proto=WPA
        key_mgmt=WPA-PSK
        pairwise=TKIP
        group=TKIP
        id_str="YCollege Wifi"
}


network={
  ssid="ET701"
  psk="Sidharth12"
  proto=RSN
  key_mgmt=WPA-PSK
  pairwise=CCMP
  auth_alg=OPEN
}


	e. Reboot.


16. MAX7219 Library

https://pypi.python.org/pypi/max7219


17. Raspberry Pi GUI

sudo apt-get install --no-install-recommends xserver-xorg
sudo apt-get install --no-install-recommends xinit
sudo apt-get install raspberrypi-ui-mods
