#   Copyright 2016 Andreas Riegg - t-h-i-n-x.net
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Changelog
#
#   1.0    2014-09-02    Initial release.

import fmf

KEYVALUEREFERENCEITEMS = [('reference item 3' , 'Reference value 3'), ('reference item 4' , 'Reference value 4')]
DICTREFERENCEITEMS = {'reference item 7' : 'Reference value 7', 'reference item 8' : 'Reference value 8'}

ARBITRARYKEYVALUEITEMS = [('arbitrary item 1' , 'Arbitrary value 1'), ('arbitrary item 2' , 'Arbitrary value 2'), ('arbitrary item 3' , 'Arbitrary value 3')]
ARBITRARYDICTITEMS = {'arbitrary item 4' : 'Arbitrary value 4', 'arbitrary item 5' : 'Arbitrary value 5', 'arbitrary item 6' : 'Arbitrary value 6'}

DATAITEMS = [('datakey 1' , 'C 1'), ('datakey 2' , 'C 2'), ('datakey 3' , 'C 3')]

KEYVALUETABLEITEMS = [('Table 1' , 'T1'), ('Table 2' , 'T2')]
DICTTABLEITEMS = {'Table 1' : 'T1', 'Table 2' : 'T2'}
DATAITEMS_T1 = [('datakey 1 (T1)' , 'C 1(T1)'), ('datakey 2 (T1)' , 'C 2(T1)'), ('datakey 3 (T1)' , 'C 3(T1)')]
DATAITEMS_T2 = [('datakey 1 (T2)' , 'C 1(T2)'), ('datakey 2 (T2)' , 'C 2(T2)')]

def test_11():
    fmfser = fmf.FMF_Serializer('Test Case 1.1, minimum info and without tables.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))


def test_111():
    fmfser = fmf.FMF_11_Serializer('Test Case 1.1.1, fmf v 1.1 and minimum info and without tables.',
                                   'Andreas Riegg',
                                   'Planet Earth')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))

def test_12():
    fmfser = fmf.FMF_Serializer('Test Case 1.2, more info and without tables, positional arguments.',
                                'Andreas Riegg', 'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_13():
    fmfser = fmf.FMF_Serializer('Test Case 1.3, more info and without tables, key value list arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                *KEYVALUEREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_14():
    fmfser = fmf.FMF_Serializer('Test Case 1.4, more info and without tables, keyword arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                referenceitem5='Reference value 5',
                                referenceitem6='Reference value 6')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_15():
    fmfser = fmf.FMF_Serializer('Test Case 1.5, more info and without tables, dictionary arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                **DICTREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_16():
    fmfser = fmf.FMF_Serializer('Test Case 1.6, more info, mixed arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                *KEYVALUEREFERENCEITEMS,
                                referenceitem5='Reference value 5',
                                referenceitem6='Reference value 6',
                                **DICTREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))


def test_21():
    fmfser = fmf.FMF_Serializer('Test Case 2.1, additional arbitrary section and without tables, key value list arguments.', 'Andreas Riegg', 'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", *ARBITRARYKEYVALUEITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_22():
    fmfser = fmf.FMF_Serializer('Test Case 2.2, additional arbitrary section and without tables, dictionary arguments.', 'Andreas Riegg', 'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", **ARBITRARYDICTITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_23():
    fmfser = fmf.FMF_Serializer('Test Case 2.3, additional arbitrary section and without tables, key value list and dictionary arguments.', 'Andreas Riegg', 'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", *ARBITRARYKEYVALUEITEMS, **ARBITRARYDICTITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_31():
    fmfser = fmf.FMF_Serializer('Test Case 3.1, minimum info with tables, key value lis arguments.', 'Andreas Riegg', 'Planet Earth')
    print(fmfser.header())
    print(fmfser.tableSection(*KEYVALUETABLEITEMS))
    # Table T1    
    print(fmfser.dataSection("T1", *DATAITEMS_T1))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2        
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2))
    for i in range(10):
        print("{0:<15d}{1:<15d}".format(i,i**i))

def test_32():
    fmfser = fmf.FMF_Serializer('Test Case 3.2, minimum info with tables, dictionary arguments.', 'Andreas Riegg', 'Planet Earth')
    print(fmfser.header())
    print(fmfser.tableSection(**DICTTABLEITEMS))
    # Table T1
    print(fmfser.dataSection("T1", *DATAITEMS_T1))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2        
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2))
    for i in range(10):
        print("{0:<15d}{1:<15d}".format(i,i**i))
    
def test_41():
    fmfser = fmf.FMF_Serializer('Test Case 4.1, all options.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                *KEYVALUEREFERENCEITEMS,
                                referenceitem5='Reference value 5',
                                referenceitem6='Reference value 6',
                                **DICTREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", *ARBITRARYKEYVALUEITEMS))
    print(fmfser.tableSection(*KEYVALUETABLEITEMS))
    # Table T1   
    print(fmfser.dataSection("T1", *DATAITEMS_T1))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2        
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(";{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2))
    for i in range(10):
        print("{0:<15d}{1:<15d}".format(i,i**i))
  
