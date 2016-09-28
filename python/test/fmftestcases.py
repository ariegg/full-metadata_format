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
#   1.0    2016-09-23    Initial release.
#   1.1    2016-09-29    Added addDataSectionLineFromObject(...) and
#                        addDataSectionLinesFromObjectList(...).
#
#   This file contains a set of test cases for the FMF library.
#
#   This file is not needed at runtime.
#
#   Test cases are available for the basic functionality provided within
#   fmfbase.py as well as for the enhanced writing functionality provided
#   in fmfwriter.py (and which is the recommended way to use this library).
#
#   All test cases can also be used as examples how to use this library.
#


import fmfbase as fmf
import fmfwriter

#---------- Some test data and objects ----------

KEYVALUEREFERENCEITEMS = [('reference item 3' , 'Reference value 3'), ('reference item 4' , 'Reference value 4')]
DICTREFERENCEITEMS = {'reference item 7' : 'Reference value 7', 'reference item 8' : 'Reference value 8'}

ARBITRARYKEYVALUEITEMS = [('arbitrary item 1' , 'Arbitrary value 1'), ('arbitrary item 2' , 'Arbitrary value 2'), ('arbitrary item 3' , 'Arbitrary value 3')]
ARBITRARYDICTITEMS = {'arbitrary item 4' : 'Arbitrary value 4', 'arbitrary item 5' : 'Arbitrary value 5', 'arbitrary item 6' : 'Arbitrary value 6'}

DATAITEM = ('datakey 1' , 'C 1')
DATAITEMS = [('datakey 1' , 'C 1'), ('datakey 2' , 'C 2'), ('datakey 3' , 'C 3')]

KEYVALUETABLEITEMS = [('Table 1' , 'T1'), ('Table 2' , 'T2')]
DICTTABLEITEMS = {'Table 1' : 'T1', 'Table 2' : 'T2'}
DATAITEMS_T1 = [('datakey 1 (T1)' , 'C 1(T1)'), ('datakey 2 (T1)' , 'C 2(T1)'), ('datakey 3 (T1)' , 'C 3(T1)')]
DATAITEMS_T2 = [('datakey 1 (T2)' , 'C 1(T2)'), ('datakey 2 (T2)' , 'C 2(T2)')]

#---------- FMF base module settings section (fmfbase.py) ----------

def test_01():
    fmf.setCommentPrefix('#')
    print('Comment set to \'#\'')

def test_02():
    fmf.resetCommentPrefix()
    print('Comment reset to \';\'')


#---------- FMF_Serializer section (fmfbase.py) ----------

def test_10():
    fmfser = fmf.FMF_Serializer('Test Case 1.1, default fmf with minimum info and without tables.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))


def test_110():
    fmfser = fmf.FMF_10_Serializer('Test Case 1.1.0, explicit fmf v 1.0 and minimum info and without tables.',
                                   'Andreas Riegg',
                                   'Planet Earth')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))

def test_111():
    fmfser = fmf.FMF_11_Serializer('Test Case 1.1.1, explicit fmf v 1.1 and minimum info and without tables.',
                                   'Andreas Riegg',
                                   'Planet Earth')
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))

def test_12():
    fmfser = fmf.FMF_Serializer('Test Case 1.2, more info and without tables, positional arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_13():
    fmfser = fmf.FMF_Serializer('Test Case 1.3, more info and without tables, key value list arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                *KEYVALUEREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
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
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))

def test_15():
    fmfser = fmf.FMF_Serializer('Test Case 1.5, more info and without tables, dictionary arguments.',
                                'Andreas Riegg',
                                'Planet Earth',
                                **DICTREFERENCEITEMS)
    print(fmfser.header())
    print(fmfser.dataSection(None, *DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
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
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**4))


def test_21():
    fmfser = fmf.FMF_Serializer('Test Case 2.1, additional arbitrary section and without tables, key value list arguments.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", *ARBITRARYKEYVALUEITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_22():
    fmfser = fmf.FMF_Serializer('Test Case 2.2, additional arbitrary section and without tables, dictionary arguments.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", **ARBITRARYDICTITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_23():
    fmfser = fmf.FMF_Serializer('Test Case 2.3, additional arbitrary section and without tables, key value list and dictionary arguments.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.arbitrarySection("section", *ARBITRARYKEYVALUEITEMS, **ARBITRARYDICTITEMS))
    print(fmfser.dataSection(*DATAITEMS))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i/2,i/3))

def test_31():
    fmfser = fmf.FMF_Serializer('Test Case 3.1, minimum info with tables, key value lis arguments.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.tableSection(*KEYVALUETABLEITEMS))
    # Table T1
    print(fmfser.dataSection("T1", *DATAITEMS_T1))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2)))
    for i in range(10):
        print("{0:<15d}{1:<15d}".format(i,i**i))

def test_32():
    fmfser = fmf.FMF_Serializer('Test Case 3.2, minimum info with tables, dictionary arguments.',
                                'Andreas Riegg',
                                'Planet Earth')
    print(fmfser.header())
    print(fmfser.tableSection(**DICTTABLEITEMS))
    # Table T1
    print(fmfser.dataSection("T1", *DATAITEMS_T1))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2)))
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
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1)))
    for i in range(10):
        print("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))
    # Table T2
    print(fmfser.dataSection("T2", *DATAITEMS_T2))
    print(fmfser.comment("{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2)))
    for i in range(10):
        print("{0:<15d}{1:<15d}".format(i,i**i))


#---------- FMF_Text section (fmfwriter.py) ----------

def test_51():
    fmftextwriter = fmfwriter.FMF_Text('Test Case 5.1, create a basic default FMF text.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_510():
    fmftextwriter = fmfwriter.FMF_Text('Test Case 5.1.0, create a basic explicit FMF 1.0 text.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                fmf='1.0')

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_511():
    fmftextwriter = fmfwriter.FMF_Text('Test Case 5.1.1, create a basic explicit FMF 1.1 text.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                fmf='1.1')

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_512():
    fmftextwriter = fmfwriter.FMF_Text('Test Case 5.1.2, create a basic explicit FMF 1.2 text, resulting in falling back to FMF 1.1.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                fmf='1.2')

    print(fmftextwriter.text())
    fmftextwriter.finish()


def test_52():
    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.2, create a FMF text, use the spooled version.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_53():
    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.3, create a simple FMF text with one data section using data lines.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS)
    fmftextwriter.startDataSection(None, *DATAITEMS)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        fmftextwriter.addDataSectionLineFromText("{0:<10d}{1:<10d}{2:<10d}".format(i,i**2,i**3))

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_54():
    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.4, create a simple FMF text with one data section using data objects.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS)
    fmftextwriter.startDataSection(None, DATAITEM)
    fmftextwriter.addCommentLine("{0[1]:<9s}".format(DATAITEM))
    for i in range(10):
        fmftextwriter.addDataSectionLineFromObject("{0:<10d}", i**5)

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_55():
    dataList = []
    for i in range(10):
        dataList.append(i*1000)

    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.5, create a simple FMF text with one data section using a data object list.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS)
    fmftextwriter.startDataSection(None, DATAITEM)
    fmftextwriter.addCommentLine("{0[1]:<9s}".format(DATAITEM))
    fmftextwriter.addDataSectionLinesFromObjectList("{0:<10d}", dataList)

    print(fmftextwriter.text())
    fmftextwriter.finish()


def test_56():
    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.6, create a simple FMF text with one data section using data tuples.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS)
    fmftextwriter.startDataSection(None, *DATAITEMS)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    for i in range(10):
        # Show all possibilities
        fmftextwriter.addDataSectionLineFromTuple("{0:<10d}{1:<10d}{2:<10d}", tuple([i,i**2,i**3]))
        fmftextwriter.addDataSectionLineFromTuple("{0:<10d}{1:<10d}{2:<10d}", tuple((i,i**2,i**3)))
        fmftextwriter.addDataSectionLineFromTuple("{0:<10d}{1:<10d}{2:<10d}", (i,i**2,i**3))
        fmftextwriter.addDataSectionLineFromTuple("{0:<10d}{1:<10d}{2:<10d}", [i,i**2,i**3])

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_57():
    dataMatrix = []
    for i in range(10):
        dataMatrix.append(tuple([i,i**2,i**3]))

    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.7, create a simple FMF text with one data section using a data matrix.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'))
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS)
    fmftextwriter.startDataSection(None, *DATAITEMS)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS))
    fmftextwriter.addDataSectionLinesFromTupleMatrix("{0:<10d}{1:<10d}{2:<10d}", dataMatrix)

    print(fmftextwriter.text())
    fmftextwriter.finish()

def test_58():
    dataMatrixT1 = []
    for i in range(10):
        dataMatrixT1.append(tuple([i,i**2,i**3]))
    dataMatrixT2 = []
    for i in range(10):
        dataMatrixT2.append(tuple([i,i**i]))

    fmftextwriter = fmfwriter.FMF_SpooledText('Test Case 5.8, create all options FMF text having tables using a data matrix.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                *KEYVALUEREFERENCEITEMS,
                                referenceitem5='Reference value 5',
                                referenceitem6='Reference value 6',
                                **DICTREFERENCEITEMS)
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS, **ARBITRARYDICTITEMS)
    fmftextwriter.addTables(*KEYVALUETABLEITEMS)
    # Table T1
    fmftextwriter.startDataSection("T1", *DATAITEMS_T1)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1))
    fmftextwriter.addDataSectionLinesFromTupleMatrix("{0:<10d}{1:<10d}{2:<10d}", dataMatrixT1)
    # Table T2
    fmftextwriter.startDataSection("T2", *DATAITEMS_T2)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2))
    fmftextwriter.addDataSectionLinesFromTupleMatrix("{0:<15d}{1:<15d}", dataMatrixT2)

    print(fmftextwriter.text())
    fmftextwriter.finish()


#---------- FMF_File section (fmfwriter.py) ----------

def test_61(filename):
    fmffilewriter = fmfwriter.FMF_File(filename, 'Test Case 6.1, create a minimal FMF file, use the provided filename.',
                                'Andreas Riegg',
                                'Planet Earth')
    fmffilewriter.finish()

def test_610(filename):
    fmffilewriter = fmfwriter.FMF_File(filename, 'Test Case 6.1.0, create a minimal FMF 1.0 file, use the provided filename.',
                                'Andreas Riegg',
                                'Planet Earth',
                                fmf='1.0')
    fmffilewriter.finish()

def test_62(filename):
    dataMatrixT1 = []
    for i in range(200):
        dataMatrixT1.append(tuple([i,i**2,i**3]))
    dataMatrixT2 = []
    for i in range(500):
        dataMatrixT2.append(tuple([i,i**4]))

    fmftextwriter = fmfwriter.FMF_File(filename, 'Test Case 6.2, create all options FMF file having tables using a data matrix.',
                                'Andreas Riegg',
                                'Planet Earth',
                                ('reference item 1', 'Reference value 1'),
                                ('reference item 2', 'Reference value 2'),
                                *KEYVALUEREFERENCEITEMS,
                                referenceitem5='Reference value 5',
                                referenceitem6='Reference value 6',
                                **DICTREFERENCEITEMS)
    fmftextwriter.addSection("section", *ARBITRARYKEYVALUEITEMS, **ARBITRARYDICTITEMS)
    fmftextwriter.addTables(*KEYVALUETABLEITEMS)
    # Table T1
    fmftextwriter.startDataSection("T1", *DATAITEMS_T1)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}{0[2][1]:<10s}".format(DATAITEMS_T1))
    fmftextwriter.addDataSectionLinesFromTupleMatrix("{0:<10d}{1:<10d}{2:<10d}", dataMatrixT1)
    # Table T2
    fmftextwriter.startDataSection("T2", *DATAITEMS_T2)
    fmftextwriter.addCommentLine("{0[0][1]:<9s}{0[1][1]:<10s}".format(DATAITEMS_T2))
    fmftextwriter.addDataSectionLinesFromTupleMatrix("{0:<15d}{1:<15d}", dataMatrixT2)
    fmftextwriter.finish()
