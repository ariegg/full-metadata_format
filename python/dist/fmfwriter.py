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
#   This is the comfort class that does FMF rendering to files and text objects.
#   Only the concrete classes
#   - FMF_Text (temporary file getting deleted after some time)
#   - FMF_SpooledText (temporary file kept in main memory until a certain size)
#   - FMF_File (persistent file)
#   should be used for FMF rendering.
#
#   This class makes use of the extended print() function that allows a
#   redirection of the printed output to arbitrary "file" objects.
#
#   This class has some helper methods that allow to create data lines
#   from tuples and sequences of tuples(=matrix) and by using the full
#   advanced output formatting capability of the str.format() feature.
#
#   As this implementation uses (temporary) files it is necessary to call
#   finish() at the end to close the files and ensure file housekeeping.
#

from __future__ import print_function
import tempfile
import fmfbase as fmf

class FMF_Creator():
    def __init__(self, outfile, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        if 'fmf' in additionalDictItems:
            if additionalDictItems['fmf'] == '1.0':
                constructor = fmf.FMF_10_Serializer
            elif additionalDictItems['fmf'] == '1.1':
                constructor = fmf.FMF_11_Serializer
            else:
                constructor = fmf.FMF_Serializer
            del additionalDictItems['fmf']
            self._serializer = constructor(title, creator, place, *additionalKeyValueItems, **additionalDictItems)
        else:
            self._serializer = fmf.FMF_Serializer(title, creator, place, *additionalKeyValueItems, **additionalDictItems)
        self._file = outfile
        print(self._serializer.header(), file=self._file)

    def addCommentLine(self, text):
        print(self._serializer.comment(text), file=self._file)

    def addSection(self, title, *arbitraryKeyValueItems, **arbitraryDictItems):
        print(self._serializer.arbitrarySection(title, *arbitraryKeyValueItems, **arbitraryDictItems), file=self._file)

    def addTables(self, *tableKeyValueDefinitions, **tableDictDefinitions):
        print(self._serializer.tableSection(*tableKeyValueDefinitions, **tableDictDefinitions), file=self._file)

    def startDataSection(self, name, *dataDefinitions):
        print(self._serializer.dataSection(name, *dataDefinitions), file=self._file)

    def addDataSectionLineFromText(self, text):
        print(text, file=self._file)

    def addDataSectionLineFromObject(self, formatString, data):
        self.addDataSectionLineFromText(formatString.format(data))

    def addDataSectionLinesFromObjectList(self, formatString, dataList):
        for data in dataList:
            self.addDataSectionLineFromObject(formatString, data)

    def addDataSectionLineFromTuple(self, formatString, dataTuple):
        self.addDataSectionLineFromText(formatString.format(*dataTuple))

    def addDataSectionLinesFromTupleMatrix(self, formatString, dataMatrix):
        for dataTuple in dataMatrix:
            self.addDataSectionLineFromTuple(formatString, dataTuple)

    def finish(self):
        self._file.close()


class FMF_Text(FMF_Creator):
    def __init__(self, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        FMF_Creator.__init__(self, tempfile.TemporaryFile(), title, creator, place, *additionalKeyValueItems, **additionalDictItems)

    def text(self):
        self._file.seek(0)
        text = self._file.read()
        return text


class FMF_SpooledText(FMF_Text):
    def __init__(self, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        FMF_Creator.__init__(self, tempfile.SpooledTemporaryFile(), title, creator, place, *additionalKeyValueItems, **additionalDictItems)


class FMF_File(FMF_Creator):
    def __init__(self, filename, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        outfile = open(filename, 'w')
        FMF_Creator.__init__(self, outfile, title, creator, place, *additionalKeyValueItems, **additionalDictItems)

