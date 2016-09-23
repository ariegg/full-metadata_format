# Full-Metadata Format
Dependency-free Python 2/3 support library for the Full-Metadata Format (FMF)

Version 1.0; for now, just writing of FMF is implemented.

All Python code that is needed at **runtime** is located in **/python/dist**.

To see **how the library can be used** look at the **/python/test** folder. Inside is one module with 
a lot of test cases that demonstrate the usage possibilities. In the file "fmf.txt" you have 
text that can be copied directly into a Python shell to run the test cases.

The easiest way for testing and exploring the library is to copy all content from /python/dist 
and /python/test into one single folder and run the text cases from IDLE.

**WARNING:** This library makes intense usage of the Python **\*args** and **\*\*kwargs** features.
This makes the library very compact and highly flexible but may be hard to understand for Python beginners.
If you encounter problems when trying the library please lokk intensely at the test cases to see the 
correct usage of those features when using this library.

**INSTALLATION:** As the runtime part of this library just consists of 3 quite small Python files, not setup.py or other 
installation routine is provided. Just copy the 3 files to an appropriate location within your Python 
project and the library will be ready to use.

