# Keylogger Converter by Natalie Schultz Henry.
# https://github.com/schultzhenry/keylogger

# Import Python modules JSON, Time and Datetime
import json
from time import time as t
from datetime import datetime as dt
# https://docs.python.org/3/library/json.html#module-json
# https://docs.python.org/3/library/time.html#module-time
# https://docs.python.org/3/library/datetime.html#module-datetime



# Name of input file with JSON data. Default
# from keylogger.pyw selected; change as desired.
input_filename = 'log_original.txt'

# Title of output HTML page. Change as desired.
title = 'My Keylog Data'

# Default output filename on line 82 for storing
# accurate timestamp in name. Change as desired.

# Load JSON key entry and convert into HTML tag.
def my_format(jsonLog):

    # Load JSON entry, storing attributes.
    jsonLog = json.loads('{0}'.format(jsonLog))
    stamp = jsonLog['time']
    key = jsonLog['key']
    app = jsonLog['application']

    # If special key, convert to unicode symbol.
    # If you would like to change the character
    # your HTML file displays for a given key,
    # add or edit an existing if statement
    # below. Decimal codes for unicode symbols
    # can be found by category here:
    # http://unicode.org/charts/
    if key == 'Key.shift_r' or key == 'Key.shift':
        key = '&#8593;'
    elif key == 'Key.cmd' or key == 'Key.cmd_r':
        key = '&#8984;'
    elif key[:2] == 'u\"' and key[-1:] == '\"':
        key = key[-2:-1]
    elif key == 'Key.backspace':
        key = '&#9003;'
    elif key == 'Key.space':
        key = '&#9251;'
    elif key == 'Key.enter':
        key = '&#8617;'
    elif key == 'Key.ctrl':
        key = '^'
    elif key == 'Key.up':
        key = '&#9652;'
    elif key == 'Key.down':
        key = '&#9662;'
    elif key == 'Key.left':
        key = '&#9666;'
    elif key == 'Key.right':
        key = '&#9656;'
    elif key == 'Key.tab':
        key = '&#9633;'
    elif key == "click":
        key = '&#8226;'
    elif key == 'Key.esc':
        key = '&#9099;'

    # Convert entry to HTML span with timestamp
    # as ID, application as second class, and key
    # as span text.
    idinfo = '<span id={0} '.format(stamp)
    classinfo = 'class="application {0}">'.format(app)
    textinfo = '{0}</span>\n'.format(key)
    tag = idinfo + classinfo + textinfo

    # Return formatted HTML tag.
    return tag



# Open input file in read mode.
inputFile = open(input_filename, 'r')

# Log current time, adding to name of new output
# file. Open output file in write mode.
time_now = str(dt.fromtimestamp(t())).replace(' ', '-')
outputFile = open('log_{0}.html'.format(time_now), 'w')

# Write head of HTML output file.
outputFile.write('<!doctype html>\n<html lang="en">\n'+
                 '<head>\n<meta charset="utf-8">\n'+
                 '<title>{0}</title>\n'+
                 '<link rel="stylesheet" '+
                 'type="text/css" href="log_format.css">\n'+
                 '</head>\n<body>'.format(title))

# For each JSON key entry, call my_format and
# write the result to HTML output file.
for line in inputFile:
    outputFile.write(my_format(line))

# Write end of HTML output file and close.
outputFile.write('</body>\n</html>')
outputFile.close()
