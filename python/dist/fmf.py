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

from datetime import datetime

NL = '\n'

class FMF_Serializer():
    def __init__(self, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        self._title = title
        self._creator = creator
        self._place = place
        self._additionalKeyValueItems = additionalKeyValueItems
        self._additionalDictItems = additionalDictItems

    def signature(self):
        return '; -*- fmf version: 1.0 -*-'

    def header(self):
        hd = self.signature()
        hd += NL + '[*reference]'
        if self._title != None:
            hd += NL + 'title: '   + self._title
        if self._creator != None:
            hd += NL + 'creator: ' + self._creator
        hd += NL + 'created: ' +  datetime.now().isoformat(' ')
        if self._place != None:
             hd += NL + 'place: ' + self._place
        hd += self.__entries__(self._additionalKeyValueItems)
        hd += self.__entries__(self._additionalDictItems.items())
        return hd
      
    def arbitrarySection(self, title, *arbitraryKeyValueItems, **arbitraryDictItems):
        sec = '[' + title + ']'
        sec += self.__entries__(arbitraryKeyValueItems)
        sec += self.__entries__(arbitraryDictItems.items())
        return sec
    
    def tableSection(self, *tableKeyValueDefinitions, **tableDictDefinitions):
        tab = '[*table definitions]'
        tab += self.__entries__(tableKeyValueDefinitions)
        tab += self.__entries__(tableDictDefinitions.items())
        return tab

    def dataSection(self, name, *dataDefinitions):
        if name != None:
            ds = '[*data definitions: {0}]'.format(name)
            ds += self.__entries__(dataDefinitions)
            ds += NL + '[*data: {0}]'.format(name)
        else:           
            ds = '[*data definitions]'
            ds += self.__entries__(dataDefinitions)
            ds += NL + '[*data]'
        return ds

    def __entries__(self, kvEntries):
        ent = ''
        for key, value in kvEntries:
            ent += NL + key + ': ' + value
        return ent

class FMF_11_Serializer(FMF_Serializer):      
    def __init__(self, title, creator, place, *additionalKeyValueItems, **additionalDictItems):
        FMF_Serializer.__init__(self, title, creator, place, *additionalKeyValueItems, **additionalDictItems)

    def signature(self):
        return '; -*- fmf version: 1.1 -*-'
