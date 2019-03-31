# # from tkinter import *
# #
# # def show_entry_fields():
# #      print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# #
# # master = Tk()
# # Label(master, text="First Name").grid(row=0)
# # Label(master, text="Last Name").grid(row=1)
# #
# # e1 = Entry(master)
# # e2 = Entry(master)
# #
# # e1.grid(row=0, column=1)
# # e2.grid(row=1, column=1)
# #
# # Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
# # Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# #
# # mainloop( )
#
#
# import os
# import sys
# import tkinter as tkinter
# sys.path.insert(0, 'gst-python')
# import gobject
# import g
#
# def on_sync_message(bus, message, window_id):
#         if not message.structure is None:
#             if message.structure.get_name() == 'prepare-xwindow-id':
#                 image_sink = message.src
#                 image_sink.set_property('force-aspect-ratio', True)
#                 image_sink.set_xwindow_id(window_id)
#
# gobject.threads_init()
#
# window = tkinter.Tk()
# window.geometry('500x400')
#
# video = tkinter.Frame(window, bg='#000000')
# video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
#
# window_id = video.winfo_id()
#
# player = gst.element_factory_make('playbin2', 'player')
# player.set_property('video-sink', None)
# player.set_property('uri', 'file://%s' % (os.path.abspath(sys.argv[1])))
# player.set_state(gst.STATE_PLAYING)
#
# bus = player.get_bus()
# bus.add_signal_watch()
# bus.enable_sync_message_emission()
# bus.connect('sync-message::element', on_sync_message, window_id)
#
# window.mainloop()

import tkinter as tk
import threading
import imageio
from PIL import Image, ImageTk

video_name = "movie.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    frame = 0
    for image in video.iter_data():
        frame += 1                                    #counter to save new frame number
        image_frame = Image.fromarray(image)
        image_frame.save('frame_%d.png' % frame)      #if you need the frame you can save each frame to hd
        frame_image = ImageTk.PhotoImage(image_frame)
        label.config(image=frame_image)
        label.image = frame_image
        if frame == 40: break                         #after 40 frames stop, or remove this line for the entire video

if __name__ == "__main__":

    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()