import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/yajat/Downloads" 
to_dir = "C:/Users/yajat/OneDrive/Desktop/Downloaded_Files"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hey,{event.src_path}has been created!")
    def on_deleted(self, event):
        print(f"oops! someone deleted the file,{event.src_path}!")
        
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

        
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()