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
#   1.0    2016-09-29    Initial release.
#
#   Description
#
#   WebIOPI example script for FMF generation and retrieval. This script
#   can be used as WebIOPi script to show how the FMF writing library
#   provided at https://github.com/ariegg/full-metadata_format
#   can be used within WebIOPi.
#
#   In order to work correct please create a /fmf folder in the directory
#   where this script is located and copy all content from the /dist
#   folder of the FMF librsry to this subfolder or take other measures
#   so that the import statement of the fmf library below works correct.
#
#   The simulated sensors devices used in this example are not part of the
#   official release of WebIOPi. But you can simply replace these with
#   some sensors that are officially supported by WebIOPi. To do this
#   - add the sensors you want to use to your config file
#   - modify DEVICENAMETEMP and DEVICENAMEPRES below to retrieve the
#   correct sensor instances
#   - update VALUELOG.append(...) in loop() so that only the available values are
#     retrieved from the sensors (most sensors deliver only one value, some
#     (e.g. BMP085) provide two or more values)
#   - Update the startDataSection(...) calls to be consistent with the values
#     provided by your sensors.
#   - Update the format string in the addDataSection...(...) calls to be
#     consistent with the number and type of the logged sensor values.
#

import webiopi
from datetime import datetime
from collections import deque
from fmf import fmfwriter

SAMPLINGINTERVAL = 0.5     #(in seconds)
LASTSAMPLINGTIME = None
SAMPLESIZE       = 1000
VALUELOG         = deque(maxlen=SAMPLESIZE)

DEVICENAMETEMP   = 'simulatedTemperature'
DEVICENAMEPRES   = 'simulatedPressure'

def setup():
    global tempsensor
    global pressensor
    tempsensor = webiopi.deviceInstance(DEVICENAMETEMP)
    pressensor = webiopi.deviceInstance(DEVICENAMEPRES)

def loop():
    global VALUELOG
    global tempsensor
    global pressensor
    global LASTSAMPLINGTIME

    if tempsensor != None and pressensor != None:
        # Read all sensor values and add them as tuple to the value log.
        VALUELOG.append(
                (
                tempsensor.getFahrenheit(),
                pressensor.getHectoPascal()
                )
            )
        # Update the latest timestamp
        LASTSAMPLINGTIME = datetime.now().isoformat(' ')

    # Sleep until the next interval
    webiopi.sleep(SAMPLINGINTERVAL)

@webiopi.macro
def fmfTempPresLog():
    global VALUELOG
    global tempsensor
    global pressensor

    fmfTextWriter = fmfwriter.FMF_SpooledText(
                                'WebIOPi FMF example two sensors log',
                                webiopi.utils.version.VERSION_STRING,
                                'n/a'
                                )

    fmfTextWriter.addSection(
        "measurement",
        ('sampling interval', '{} ms'.format(SAMPLINGINTERVAL * 1000)),
        ('last sampling time', '{}'.format(LASTSAMPLINGTIME)),
        ('sampled values', '{}'.format(len(VALUELOG)))
         )

    abstractions1 = familyHelper(tempsensor.__family__())
    fmfTextWriter.addSection(
        'webiopi ' + DEVICENAMETEMP,
        ('device class', tempsensor.__class__.__name__),
        ('device abstraction(s)', abstractions1)
         )

    abstractions2 = familyHelper(pressensor.__family__())
    fmfTextWriter.addSection(
        'webiopi ' + DEVICENAMEPRES,
        ('device class', pressensor.__class__.__name__),
        ('device abstraction(s)', abstractions2)
         )

    fmfTextWriter.startDataSection(
        None,
        (DEVICENAMETEMP + ' c1', 'temperature/f [degF]'),
        (DEVICENAMEPRES + ' c2', 'pressure/hpa [hPa]')
        )

    fmfTextWriter.addDataSectionLinesFromTupleMatrix('{0:<10.2f}{1:<10.2f}', VALUELOG)

    fmfresult = fmfTextWriter.text()
    fmfTextWriter.finish()

    return fmfresult


def familyHelper(family):
    if isinstance(family, str):
        return family
    else:
        famlist = family[0]
        for fam in family[1:]:
            famlist += ', ' + fam
        return famlist

