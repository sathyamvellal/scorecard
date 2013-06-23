#! /bin/bash
sudo apt-get install python
sudo apt-get install pyqt4-dev-tools
sudo chmod +x remove.sh score.py gui.py
sudo cp remove.sh score.py gui.py /opt/
sudo ln -s /opt/score.py /usr/bin/score
sudo ln -s /opt/gui.py /usr/bin/gui
sudo ln -s /opt/remove.sh /usr/bin/remove
