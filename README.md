# findDoubleImages
Find copies of images on the disk/folders.

## Usage
### Data Acquisition
1. git clone to some location 'git clone https://github.com/reto271/findDoubleImages'
1. Run 'nohup ./findDoublesAdv.sh'
1. Wait for the script to terminate, e.g. monitor it by htop.


**Comments:**
* If you would like to register different image properties for logging, modify the 'logger.registerTag' list at the bottom of the Python script 'findDoublesAdv.py'.
* 'nohup' runs a script without terminating if the ssh connection is closed/aborted.

### Data Analysis
There are several possibilities to analyze the output data (out_dir)

_Eventually copy the out_dir to a location where more computation power is available than on a NAS._

* Run the 'analyzeFiles.sh'. Make sure the out_dir is next to the script. **(Currently not update)**
* Analyze 'out_dir/fileData.csv' manually by using Excel, Libre Office, ...
