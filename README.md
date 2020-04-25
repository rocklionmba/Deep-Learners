# Deep-Learners

## How to run:
1. Install Anaconda and download and unzip “Deep-Learners”.

2. Open the anaconda prompt and create the conda3 environment using
the following commands:
```batch
conda create -n yolo python=3.6
activate yolo
cd /path/to/folder/Deep-Learners/Deep-Learners
```
3. Install the modules from the requirements.txt file using the commands
```batch
pip install -r Machine_Learning/requirements.txt
pip install -e Machine_Learning/
```
4. Once all the modules are installed, run the command below:
```batch
python UI/MainWindow.py
```
  NOTE! If you have more than one python interpreter, you MUST run the anaconda one.
To find the path, follow the commands below:
```batch
where python
C:\path\to\anaconda\yolo\python.exe UI/MainWindow.py
```