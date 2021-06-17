# CMSC6950_Project - Pymagicc
Course project for CMSC6950 Spring 2021

Prudhvi Kommareddi

## Introduction
[Pymagicc](https://github.com/openscm/pymagicc) is a Python wrapper around the reduced complexity climate model [MAGICC6](http://magicc.org/). It wraps the CC-BY-NC-SA licensed MAGICC6 binary. Pymagicc itself is AGPL licensed.

This project utilises the Pymagicc module to achieve a couple of computational tasks and visualizations.

## Software setup

Assuming conda package manager is already installed,

Create a python environment for the project.
```
conda create -n pymagicc pip
conda activate pymagicc
```

Install Wine to run the Fortran based Windows binary.
```
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install wine32
```

Install the python wrapper and its supporting libraries.
```
pip install pymagicc matplotlib seaborn
```

## Basic Usage
Clone the repo and the change the directory to the project
```
git clone https://github.com/pkommareddi/CMSC6950_Project.git
cd CMSC6950_Project
```

Run the below command to generate the repot
```
make
```

Finally, either of the below commands to clean the intermediate files
```
make clean
make deepclean
```