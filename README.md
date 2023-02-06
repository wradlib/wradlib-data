# wradlib-data
wradlib example data

This repository contains example data used by notebooks/examples from [wradlib/wradlib](https://github.com/wradlib/wradlib/).

Installing
==========

We've moved the repository to use [pooch](https://www.fatiando.org/pooch/) for downloading and caching wradlib-data files locally. 
Please adapt your workflows.

- Ensure the `wradlib_data` package is installed in your environment

    ```bash
    $ python -m pip install wradlib-data
    
    # or
    
    $ python -m pip install git+https://github.com/wradlib/wradlib-data@pooch
    ```

- Import `DATASETS` and inspect the registry to find out which datasets are available

    ```python
    In [1]: from wradlib_data import DATASETS
    
    In [2]: DATASETS.registry_files
    Out[2]: 
    ['dx/raa00-dx_10908-0806021655-fbg---bin.gz',
    ...
    'trmm/2A-RW-BRS.TRMM.PR.2A25.20100206-S111422-E111519.069662.7.HDF']  
    ```

- To fetch a data file of interest, use the `.fetch` method and provide the filename of the data file. This will

  - download and cache the file if it doesn't exist already.
  - retrieve and return the local path.
      ```python
      In [1]: from wradlib_data import DATASETS
      
      In [2]: filepath = DATASETS.fetch("furuno/0080_20210730_160000_01_02.scn.gz")
      Out[2]: 
      Downloading file 'dx/raa00-dx_10908-0806021655-fbg---bin.gz' from 'https://github.com/wradlib/wradlib-data/raw/main/data/dx/raa00-dx_10908-0806021655-fbg---bin.gz' to '/user/kmuehlbauer/.cache/wradlib-data'.
      ```

- The datasets will be retrieved to your standard system cache-folder. To specify the location please set WRADLIB_DATA environment variable to the wanted path.
    - Linux:
        ```bash
        $ export WRADLIB_DATA=/path/to/wradlib-data
        ```
    - Windows:
        ```bash
        set WRADLIB_DATA C:\path\to\wradlib-data
        
        # or
        
        setx WRADLIB_DATA C:\path\to\wradlib-data
        ```

Usage
=====

The provided data is used in wradlib notebooks and examples. 
