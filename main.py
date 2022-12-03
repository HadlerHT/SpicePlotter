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


class PlotConfiguration:

    def __init__(self):
        self.axesScaleType = dict()


class App(ctk.CTk):

    def __init__(self, plotParameters):
        super().__init__()

        self.geometry("1200x600")
        self.title("Spice Plotter")

        # self.iconbitmap("myIcon.ico")

        self.bind('<Configure>', resize(self))

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)

        self.menuFrame = self.createMenuFrame()
        self.menuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=0, row=0)

        self.dataMenuFrame = self.createDataMenuFrame()
        self.dataMenuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=1, row=0)

        self.axesMenuFrame = self.createAxesMenuFrame(plotParameters)
        self.axesMenuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=1, row=0)

        previewFrame = ctk.CTkFrame(master=self, corner_radius=10)
        previewFrame.grid(sticky=ctk.NSEW, padx=5, pady=5, column=2, row=0)

    def createMenuFrame(self):
        frame = ctk.CTkFrame(master=self, corner_radius=0)

        fileBrowserButton = ctk.CTkButton(master=frame, text="Browse Files",
                                          command=fileBrowser, corner_radius=0)
        fileBrowserButton.pack(fill=X, ipady=10)

        menus = {"Data": self.dataMenuHandler,
                 "Curve": self.curveMenuHandler,
                 "Axes": self.axesMenuHandler,
                 "Title": self.titleMenuHandler,
                 "Legend": self.legendMenuHandler}

        menuButtons = dict()
        for menuKey in menus.keys():
            menuButtons[menuKey] = ctk.CTkButton(master=frame, text=menuKey,
                                                 command=menus[menuKey], corner_radius=0)
            menuButtons[menuKey].pack(fill=X)

        return frame

    def createDataMenuFrame(self):
        frame = ctk.CTkFrame(master=self, corner_radius=0)

        frame.configure(fg_color='white')

        return frame

    def createAxesMenuFrame(self, plot):
        frame = ctk.CTkFrame(master=self, corner_radius=0, fg_color="#363636")

        # Axe Names
        axes = ("X", "Y1", "Y2")

        # Dictionary of axe interfaces
        axesInterface = dict()
        for axe in axes:
            # Creates a frame where the inputs for each axe will be placed
            axesInterface[axe] = ctk.CTkFrame(master=frame, corner_radius=10, height=120)
            axesInterface[axe].pack(fill=X, padx=10, pady=5)

            # =========== FRAME TITLE ===========
            for column in range(3):
                axesInterface[axe].columnconfigure(column, weight=1)

            #axesInterface[axe].rowconfigure(0, weight=1)
            #axesInterface[axe].rowconfigure(1, weight=5)


            # =========== FRAME TITLE ===========
            title = ctk.CTkLabel(master=axesInterface[axe], text=axe+" Axes").\
                grid(column=0, columnspan=3)
            # ===================================

            # =========== ENABLE SECONDARY Y AXE ===========
            if axe == "Y2":
                ctk.CTkCheckBox(master=axesInterface[axe], text="Enable").\
                    grid(sticky=N, column=0)

            # ==============================================

            # =========== RADIO BUTTONS - AXES SCALE ===========
            plot.axesScaleType[axe] = ctk.StringVar(value="lin")

            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesScaleType[axe],
                               text="Linear", value="lin").\
                grid(sticky=W, column=0, padx=10, pady=2)

            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesScaleType[axe],
                               text="Logarithmic", value="log").\
                grid(sticky=W, column=0, padx=10, pady=2)
            # =================================================

            def f1():
                print(list(plot.axesScaleType.values())[0].get())

            ctk.CTkButton(master=axesInterface[axe], command=f1).grid(column=1)

        return frame

    def dataMenuHandler(self):
        self.dataMenuFrame.lift()

    def curveMenuHandler(self):
        print(self.title)

    def axesMenuHandler(self):
        self.axesMenuFrame.lift()

    def titleMenuHandler(self):
        print(self.title)

    def legendMenuHandler(self):
        print(self.title)


if __name__ == '__main__':

    plotParameters = PlotConfiguration()

    app = App(plotParameters)
    app.mainloop()