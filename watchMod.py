import pyinotify
import os

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CLOSE_WRITE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print("Edited", event.pathname)
        os.system('python3 filereader_serialwriter.py')

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/path/to/file/mytext.txt', mask, rec=True) # change your path and file names accordingly

notifier.loop()