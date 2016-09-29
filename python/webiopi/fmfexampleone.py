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
#   The simulated sensors device used in this example is not part of the
#   official release of WebIOPi. But you can simply replace this with
#   some sensor that is officially supported by WebIOPi. To do this
#   - add the sensor you want to use to your config file
#   - modify DEVICENAME below to retrieve the correct sensor instance
#   - update VALUELOG.append(...) in loop() so that only the available values are
#     retrieved from the sensor (most sensors deliver only one value, some
#     (e.g. BMP085) provide two or more values)
#   - Update the startDataSection(...) calls to be consistent with the values
#     provided by your sensor.
#   - Update the format string in the addDataSection...(...) calls to be
#     consistent with the number and type of the logged sensor values.
#
#   Simultaneous logging from different sensors is also possible. This is shown
#   in another script.
#

import webiopi
from datetime import datetime
from collections import deque
from fmf import fmfwriter

SAMPLINGINTERVAL = 1     #(in seconds)
LASTSAMPLINGTIME = None
SAMPLESIZE       = 1000
VALUELOG         = deque(maxlen=SAMPLESIZE)

DEVICENAME   = 'simulatedSensors'

def setup():
    global sensor
    sensor = webiopi.deviceInstance(DEVICENAME)

def loop():
    global VALUELOG
    global sensor
    global LASTSAMPLINGTIME

    if sensor != None:
        # Read all sensor values and add them as tuple to the value log.
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
        # Update the latest timestamp
        LASTSAMPLINGTIME = datetime.now().isoformat(' ')

    # Sleep until the next interval
    webiopi.sleep(SAMPLINGINTERVAL)

@webiopi.macro
def fmfTempLog():
    global VALUELOG
    global sensor

    fmfTextWriter = fmfwriter.FMF_SpooledText(
                                'WebIOPi FMF example temperature log',
                                webiopi.utils.version.VERSION_STRING,
                                'n/a'
                                )

    fmfTextWriter.addSection(
        "measurement",
        ('sampling interval', '{} ms'.format(SAMPLINGINTERVAL * 1000)),
        ('last sampling time', '{}'.format(LASTSAMPLINGTIME)),
        ('sampled values', '{}'.format(len(VALUELOG)))
         )

    abstractions = familyHelper(sensor.__family__())

    fmfTextWriter.addSection(
        'webiopi ' + DEVICENAME,
        ('device class', sensor.__class__.__name__),
        ('device abstraction(s)', abstractions)
         )

    fmfTextWriter.startDataSection(None, (DEVICENAME, 'temperature/c [degC]'))

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

    fmfTextWriter.addSection(
        "measurement",
        ('sampling interval', '{} ms'.format(SAMPLINGINTERVAL * 1000)),
        ('last sampling time', '{}'.format(LASTSAMPLINGTIME)),
        ('sampled values', '{}'.format(len(VALUELOG)))
         )

    abstractions = familyHelper(sensor.__family__())
    fmfTextWriter.addSection(
        'webiopi ' + DEVICENAME,
        ('device class', sensor.__class__.__name__),
        ('device abstraction(s)', abstractions)
         )

    fmfTextWriter.startDataSection(
        None,
        (DEVICENAME + ' c1', 'temperature/c [degC]'),
        (DEVICENAME + ' c2', 'pressure/pa [Pa]'),
        (DEVICENAME + ' c3', 'luminosity/lux [lx]'),
        (DEVICENAME + ' c4', 'distance/mm [mm]'),
        (DEVICENAME + ' c5', 'humidity/percent [%]'),
        (DEVICENAME + ' c6', 'color/rgbhex')
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

