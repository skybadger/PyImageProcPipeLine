import prose
import numpy
import matplotlib as mpl
import imageio
import astropy as ap
import PyYAML as pml
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

###
#Reference folder
#[Default process]
# [camera] UseBias, useDark, useFlat
#[postSession] #capture actions pending at shutdown
#
#[#ref/camera/[date]/[type:dark,bias,flat[filter]]

#Data folder
#/[object name]/[date]/[camera]/[type:light[filter]|dark|flat[filter]|bias]
#
# on new file
#is it a supported image file
#read headers - get attributes - size, res, camera, type, etc. 
#what object is it ?
#is it a reference image type (bias, dark, flat)
#which camera is this for ?
#which filter is this for ?
#is there a folder matching this date ? if N - create one
# #Move image to appropriate ref folder






###
class Watcher:
    DIRECTORY_TO_WATCH = "/c/users/mike/appdata/local" #'/path/to/my/directory"

    def __init__(self):
        self.observer = Observer()
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print( "Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)
    
    def on_created(self, event):

        return super().on_created(event)
    def on_deleted(self, event):
        #check for any pendig actions that are expected to use this file
        #clean up
        return super().on_deleted(event)
    
    def IdFileType( self, event ):
        if event.is_directory():
            return None
        
        isValidFile = False
        #working out fietypes -get this lit fromthe yaml set
        imageFileTypes=["fits","fit","dcraw","nef","tiff","jpg","png"]
        if event.src_path[-4:].contains("."):
            #we have a file with dos filetype extension endings
            if event.src_path[-4:].contains(imageFileTypes):
            isValidFile =True
        
        
        return 0
    
if __name__ == '__main__':

    #parse yaml file
    yamlParser = pml()
    yamlParser.open("")
    execList = list()

    w = Watcher()
    w.run()