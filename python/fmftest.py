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
#   provided at
#   https://github.com/ariegg/full-metadata_format
#   can be used within WebIOPi.
#
#   In order to work correct please create a /fmf folder in the directory
#   where this script is located and copy all content from the /dist
#   folder of the FMF librsry to this subfolder or take other measures
#   so that the import of the fmf library works correct.
#
#   The simulated devices used in this example are not part of the
#   official release of WebIOPi. But you can simply replace them with
#   some sensor(s) that are supported.


import webiopi
from collections import deque
from fmf import fmfwriter

SAMPLINGTIME = 1
SAMPLESIZE   = 1000
VALUELOG     = deque(maxlen=SAMPLESIZE)

DEVICENAME   = 'simulatedSensors'

def setup():
    global sensor
    sensor = webiopi.deviceInstance(DEVICENAME)

def loop():
    global VALUELOG
    global sensor

    # Read all sensor values and add them as tuple to the value log.
    if sensor != None:
        VALUELOG.append(
                (
                sensor.getCelsius(),
                sensor.getPascal(),
                sensor.getLux(),
                sensor.getMillimeter(),
                sensor.getHumidityPercent(),
                sensor.getRGBHex()
                )
            )

    webiopi.sleep(SAMPLINGTIME)

@webiopi.macro
def fmfTempLog():
    global VALUELOG
    global sensor

    fmfTextWriter = fmfwriter.FMF_SpooledText(
                                'WebIOPi FMF example temperature log',
                                webiopi.utils.version.VERSION_STRING,
                                'n/a'
                                )

    abstractions = familyHelper(sensor.__family__())
    fmfTextWriter.addSection(
        "webiopi",
        ('device name', '{}'.format(DEVICENAME)),
        ('device class', '{}'.format(sensor.__class__.__name__)),
        ('device abstraction(s)', '{}'.format(abstractions))
         )

    fmfTextWriter.addSection(
        "measurement",
        ('sampling interval', '{} ms'.format(SAMPLINGTIME * 1000)),
        ('sampled values', '{}'.format(len(VALUELOG)))
         )

    fmfTextWriter.startDataSection(None, ('{}'.format(DEVICENAME), 'temperature/c [degC]'))

## Alternative 1
##    for values in VALUELOG:
##        fmfTextWriter.addDataSectionLineFromText("{0:<.2f}".format(values[0]))

## Alternative 2
    for values in VALUELOG:
        fmfTextWriter.addDataSectionLineFromObject("{0:<.2f}", values[0])

    fmfresult = fmfTextWriter.text()
    fmfTextWriter.finish()

    return fmfresult

@webiopi.macro
def fmfSensLog():
    global VALUELOG
    global sensor

    fmfTextWriter = fmfwriter.FMF_SpooledText(
                                'WebIOPi FMF example all sensors log',
                                webiopi.utils.version.VERSION_STRING,
                                'n/a'
                                )
    
    abstractions = familyHelper(sensor.__family__())
    fmfTextWriter.addSection(
        "webiopi",
        ('device name', '{}'.format(DEVICENAME)),
        ('device class', '{}'.format(sensor.__class__.__name__)),
        ('device abstraction(s)', '{}'.format(abstractions))
         )

    fmfTextWriter.addSection(
        "measurement",
        ('sampling interval', '{} ms'.format(SAMPLINGTIME * 1000)),
        ('sampled values', '{}'.format(len(VALUELOG)))
         )

    fmfTextWriter.startDataSection(
        None,
        ('column 1', 'temperature/c [degC]'),
        ('column 2', 'pressure/pa [Pa]'),
        ('column 3', 'luminosity/lux [lx]'),
        ('column 4', 'distance/mm [mm]'),
        ('column 5', 'humidity/percent [%]'),
        ('column 6', 'color/rgbhex')
        )
## Alternative 1
##    for values in VALUELOG:
##        fmfTextWriter.addDataSectionLineFromTuple('{0:<10.2f}{1:<10.2f}{2:<10.2f}{3:<10.2f}{4:<10.2f}{5:<10s}', values)

## Alternative 2
    fmfTextWriter.addDataSectionLinesFromTupleMatrix('{0:<10.2f}{1:<10.2f}{2:<10.2f}{3:<10.2f}{4:<10.2f}{5:<10s}', VALUELOG)

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
        
