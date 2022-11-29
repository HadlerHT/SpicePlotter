# import matplotlib as plt
# import numpy as np
# import csv

from tkinter import *
from tkinter import filedialog
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


def fileBrowser():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    print(filename)


def function1():
    ctk.set_appearance_mode("Light")


def resize(buffer):
    print("resize")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Spice Plotter")

        # self.iconbitmap("myIcon.ico")

        self.bind('<Configure>', resize(self))

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)

        menuFrame = self.createMenuFrame()
        menuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=0, row=0)

        self.functionFrame = ctk.CTkFrame(master=self, corner_radius=10)
        self.functionFrame.grid(sticky=ctk.NSEW, padx=5, pady=5, column=1, row=0)

        previewFrame = ctk.CTkFrame(master=self, corner_radius=10)
        previewFrame.grid(sticky=ctk.NSEW, padx=5, pady=5, column=2, row=0)

    def createMenuFrame(self):
        menuFrame = ctk.CTkFrame(master=self, corner_radius=0)

        fileBrowserButton = ctk.CTkButton(master=menuFrame, text="Browse Files",
                                          command=fileBrowser, corner_radius=0)
        fileBrowserButton.pack(fill=X, ipady=10)

        #menuCommand = {"Data": self.dataMenuHandler,
        #               "Curve": self.curveMenuHandler,
        #               "Axes": self.axesMenuHandler,
        #               "Title": self.titleMenuHandler,
        #               "Legend": self.legendMenuHandler}

        menuName = ("Data", "Curve", "Axes", "Title", "Legend")
        menuCommand = (self.dataMenuHandler, self.curveMenuHandler, self.axesMenuHandler,
                       self.titleMenuHandler, self.legendMenuHandler)

        menuButtons = list()
        for i in range(len(menuName)):
            menuButtons.append(ctk.CTkButton(master=menuFrame, text=menuName[i],
                                             command=menuCommand[i], corner_radius=0))
            menuButtons[i].pack(fill=X)

        return menuFrame

    def dataMenuHandler(self):
        print(self.functionFrame.corner_radius)
        print(self.title)

    def curveMenuHandler(self):
        print(self.title)

    def axesMenuHandler(self):
        print(self.title)

    def titleMenuHandler(self):
        print(self.title)

    def legendMenuHandler(self):
        print(self.title)


if __name__ == '__main__':
    app = App()
    app.mainloop()