#! /bin/bash
sudo chmod +x remove.sh score.py
sudo mkdir /opt/cricinfoscore
sudo cp remove.sh score.py gui.py /opt/cricinfoscore
sudo ln -s /opt/cricinfoscore/score.py /usr/bin/cricinfoscore
sudo ln -s /opt/cricinfoscore/remove.sh /usr/bin/cricinfoscore-uninstall
