# Full-Metadata Format
Dependency-free Python 2/3 support library for the Full-Metadata Format (FMF). The purpose of this library is to provide a very lightwheight possibility to generate/store FMF content on e.g. lightwheight IoT platforms that support Python 2/3 (e.g. Raspberry Pi). Explicit encoding support is not implemented at the moment, the library will just use the default encoding on the platform it runs on.

# Release
Current version is **1.1**.

Just writing of FMF is implemented. Reading FMF is not planned, please use the Pyphant libraries for that (https://github.com/SGWissInfo/pyphant1).

All Python code that is needed at **runtime** is located in **/python/dist**.

# Hints
To see **how the library can be used** look at the **/python/test** folder. Inside is one module with 
a lot of test cases that demonstrate the usage possibilities. In the file "fmf.txt" you have 
text that can be copied directly into a Python shell or IDLE to run the test cases.

The easiest way for testing and exploring the library is to copy all content from /python/dist 
and /python/test into one single folder and run the text cases from IDLE.

For usage within WebIOPi (http://webiopi.trouch.com/) the **/python/webiopi** folder has two example Python scripts and a config file that demonstrate how to use this library via custom scripts.

**WARNING:** This library makes intense usage of the Python **\*args** and **\*\*kwargs** features.
This makes the library very compact and highly flexible but may be hard to understand for Python beginners.
If you encounter problems when trying the library please look intensely at the test cases to see the 
correct usage of those features when using this library.

**INSTALLATION:** As the runtime part of this library just consists of 3 quite small Python files, no setup.py or other 
installation routine is provided. Just copy the 3 files to an appropriate location within your Python 
project and the library will be ready to use.

**Physical quantities:** This library does currently not have extended suport for generic creation of data (column) definitions. You have to create the values for the column definitions as strings by your own and obey the FMF rules so that standard FMF reading tolls can interpret the columns correct. However, in simple cases just a unique column name and a physical unit in square brackets is needed which not a big task to do.

