from setuptools import setup, find_packages

setup(
    name="TrenchRipper",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    # python requirements
    install_requires=[
        "numpy",
        "pandas",
        "h5py",
        "scipy",
        "scikit-image",
        "matplotlib",
        "dask[distributed]",
        "dask-jobqueue",
        "tifffile",
        "ipywidgets",
        # "pytables", #derpcated package
        "scikit-learn",
        "seaborn",
        "line_profiler",
        "h5py_cache",
        "nd2reader",
        "nodejs",
        "widgetsnbextension",
    ],
)
