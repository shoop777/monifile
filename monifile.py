from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import sys


target_dir = "/Users/sho/Desktop/test"
f = open('/Users/sho/Documents/python/monifile_Log','a')
set = time.ctime()
now = time.strptime(set)
f.write(time.strftime("%Y/%m/%d %H:%M", now) + " : start\n")
print(time.strftime("%Y/%m/%d %H:%M", now) + " : start")

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        set_created = time.ctime()
        now_created = time.strptime(set_created)
        f.write(time.strftime("%Y/%m/%d %H:%M", now_created) + " : " + filename + " が作成されました\n" )
        print(time.strftime("%Y/%m/%d %H:%M", now_created) + " : " + filename + " が作成されました")

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        set_modified = time.ctime()
        now_modified = time.strptime(set_modified)
        f.write(time.strftime("%Y/%m/%d %H:%M", now_modified) + " : " + filename + "が変更されました\n")
        print(time.strftime("%Y/%m/%d %H:%M", now_modified) + " : " + filename + "が変更されました")

    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        set_deleted = time.ctime()
        now_delited = time.strptime(set_deleted)
        f.write(time.strftime("%Y/%m/%d %H:%M", now_delited) + " : " + filename + "が削除されました\n")
        print(time.strftime("%Y/%m/%d %H:%M", now_delited) + " : " + filename + "が削除されました")

if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            set = time.ctime()
            now = time.strptime(set)
            f.write(time.strftime("%Y/%m/%d %H:%M", now) + " : finish\n")
            f.close()
            print(time.strftime("%Y/%m/%d %H:%M", now) + " : finish")
            observer.stop()
            sys.exit()
        observer.join()
