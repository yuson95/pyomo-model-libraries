# Pyomo Performance Tests Overview

Pyomo is a Python-based open-source software package that supports a diverse set of optimization capabilities for formulating and analyzing optimization models. Pyomo can be used to define symbolic problems, create concrete problem instances, and solve these instances with standard solvers.

This repository contains the reworked benchmark tests (aka, performance tests) to be run using `nose 1.3.7` for Pyomo, based on Bill Hart's original tests.

## Placement of Repository

In your local copy of the `Pyomo/pyomo-model-libraries` repository, clone `pyomo-performancetests` as below:
```
$ cd pyomo-model-libraries
$ git clone git@gitlab.sandia.gov:allevin/pyomo-performancetests.git 
```

## Running the Tests

### Manually
These tests can be invoked using the following command from the `pyomo-performancetests` directory:
```
$ nosetests performancetests/tests/<subset>
```

The available subsets are `longtests` and `shorttests`.

Also, both `longtests` and `shorttests` can be run together:
```
$ nosetests performancetests/tests
```
You can also use categories to initialize the tests:
```
$ nosetests "--eval-attr=short and (not nl)" performancetests/tests
```
### Console Script
These tests can also be invoked using the following console script command:
```
$ pyomo-performance [-h] [--version] [-c CATEGORY] [-l LOCATION] [-v]
```
The optional arguments are as follows:
```
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c CATEGORY, --cat CATEGORY
                        Specify the category(ies) of performance tests to run
                        in comma-separated list
  -l LOCATION, --location LOCATION
                        Specify location (including name of file, if desired)
                        of test(s)
  -v, --verbose         Verbose output

```
By default, the console script will run all tests in the `performancetests/tests` directory, but this can be filtered using categories like `short`, `long`, `nl`, `'not bar'`, etc.

## Output

Results from the test will print to the terminal in this fashion:
```
Performance Testing Report:
Pyomo Model bilinear1_100_100 (bar) - Total Runtime = 0.490000
Pyomo Model bilinear1_100_100 (gms) - Total Runtime = 0.470000
```

Output files in `.csv` format will be created in the `performancetests/output/runtime` directory for each successfully run test. Rundata as `.out` files will be created in the `performancetests/output/rundata` directory.