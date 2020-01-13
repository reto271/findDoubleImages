# findDoubleImages
Find copies of images on the disk/folders.

Start it on the the NAS:
1) ssh login, e.g. ssh -l root 192.168.1.100
2) cd /volume1/findDoubles
3) nohup ./findDoubles.sh

Wait for the script to terminate, e.g. monitor it by htop.

nohup
Runs a script without terminating if the ssh connection is closed.
