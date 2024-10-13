SimplHDL-gowin
---------------------------

SimplHDL-gowin is a backend flow for the SimplHDL framework.
From the SimplHDL project model, it generates a GOWIN IDE project, which you can either
open in the GUI or run directly through SimplHDL.


## Installation
Simply clone the repository to a location of your choice, and install the plugin with pip:
```
$ pip install -e <path-to-your-local-clone>
```


## Use
The plugin makes a new flow, `gowin`, available in SimplHDL. This flow simply outputs the generated VHDL_LS configuration
to `stdout`. To run it, simply type:
```
$ simpl gowin [--gui] [--step syn|pnr|all]
```

GOWIN part numbers must be specified in your project spec as follows:
```
<part_no>__<device_version>
```
