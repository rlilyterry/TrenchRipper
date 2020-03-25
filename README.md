# Setup using Anaconda on MacOS

These commands download this file from internet and then open it.
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.pkg
open Anaconda3-2020.02-MacOSX-x86_64.pkg
```

## Install anaconda packages after Anaconda installation is complete
```
conda install -y -c conda-forge widgetsnbextension ipympl
conda install nodejs

# jupyter labextension install @jupyterlab/toc @jupyter-widgets/jupyterlab-manager jupyterlab-matplotlib

conda install -y -c conda-forge numpy pandas h5py scipy scikit-image jupyterlab matplotlib dask distributed dask-jobqueue tifffile ipywidgets
conda install -y -c pytorch torchvision
conda install -y -c anaconda pytables scikit-learn seaborn line_profiler
pip install h5py_cache nd2reader
pip install qgrid
```

## Install `trenchripper`

In the package directory run
```
python setup.py install
```

## Start Jupyter Server

```
jupyter notebook
```

# General Terminal Guide

```
# open directory
cd DirectoryName/XXX/YYY

# go one level up
cd ..

# go to the home folder
cd ~

# list files in directory
ls -l

# present working directory
pwd
```

# [Alternate] Setup using Native Python

Run this command in shell to install required packages.
```
pip3 install -r requirements.txt
```
