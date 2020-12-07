#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import os
from moviepy.editor import *

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Convert Video to Audio Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        fieldset = ttk.LabelFrame(frame, text='Choose Video')
        fieldset.pack(side=tk.TOP, expand=True, padx=10, pady=(10, 0), fill=tk.BOTH)

        self.button = ttk.Button(fieldset, text='Browse', command=self.get_file)
        self.button.pack(side=tk.LEFT, anchor=tk.NW)

        self.filename = tk.StringVar()
        self.entry = ttk.Entry(fieldset, width=80, textvariable=self.filename, state=tk.DISABLED)
        self.entry.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.X, ipady=5)

        self.button = ttk.Button(frame, text='Convert to Audio', command=self.convert)
        self.button.pack(side=tk.RIGHT, anchor=tk.W, padx=(0, 10), pady=10)

    # ------------------------------------------
    def get_file(self):
        self.entry.config(state=tk.NORMAL)
        file = fd.askopenfile(mode='r')
        name = file.name
        self.filename.set(name)
        self.entry.config(state=tk.DISABLED)

    def convert(self):
        # load video file
        video_clip = VideoFileClip(self.filename.get())
        # convert video file to audio file
        audio_clip = video_clip.audio

        base = os.path.basename(self.filename.get())
        os.path.splitext(base)
        filename = os.path.splitext(base)[0]

        # create mp3 file using write function
        audio_clip.write_audiofile(f'{filename}.mp3')

        # close audio and video
        audio_clip.close()
        video_clip.close()

        # play audio
        os.startfile(f'{filename}.mp3')


#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()