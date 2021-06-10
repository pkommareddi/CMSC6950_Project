# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Prudhvi Kommareddi

## Software setup

Create a python environment for the project
```
conda create -n pymagicc pip
conda activate pymagicc
```

Install Wine to run the Fortran based Windows binary
```
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install wine32
```

Install the python wrapper and its supporting libraries
```
pip install pymagicc matplotlib seaborn notebook
```

