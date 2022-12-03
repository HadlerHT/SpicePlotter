# import matplotlib as plt
# import numpy as np
# import csv

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

titleFont = ('Arial', 14, 'bold')
labelFont = ('Arial', 12)


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
        self.axesLimitsType = dict()
        self.axesLimitsMax = dict()
        self.axesLimitsMin = dict()
        self.y2Enabled = False


def entryupdate():
    #print(sv, i, self.fruit[i], sv.get())
    print("here")


class App(ctk.CTk):

    def __init__(self, plotParameters):
        super().__init__()

        self.geometry("1200x600")
        self.title("Spice Plotter")

        # self.iconbitmap("myIcon.ico")

        # self.bind('<Configure>', resize(self))

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(3, weight=2)

        self.menuFrame = self.createMenuFrame()
        self.menuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=0, row=0)

        self.dataMenuFrame = self.createDataMenuFrame()
        self.dataMenuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=1, row=0)

        self.axesMenuFrame = self.createAxesMenuFrame(plotParameters)
        self.axesMenuFrame.grid(sticky=ctk.NSEW, padx=0, pady=0, column=1, row=0)

        def printPlot():
            # print(plotParameters.axesScaleType)
            # print(plotParameters.y2Enabled)
            print(plotParameters.axesLimitsType["X"].get())
            print(plotParameters.axesLimitsType["Y"].get())
            print(plotParameters.axesLimitsType["Y2"].get())
            print("-------")

        previewFrame = ctk.CTkFrame(master=self, corner_radius=10)
        previewFrame.grid(sticky=ctk.NSEW, padx=5, pady=5, column=3, row=0)

        ctk.CTkButton(master=previewFrame, text="Plot", command=printPlot).grid()

    # def entryupdate(self, sv, i):

    def createMenuFrame(self):
        frame = ctk.CTkFrame(master=self, corner_radius=0)

        fileBrowserButton = ctk.CTkButton(master=frame,
                                          text="Browse Files", text_font=("Arial", 12, "bold"),
                                          command=fileBrowser,
                                          corner_radius=0, height=30, pady=1)
        fileBrowserButton.pack(fill=X, ipady=10)

        menus = {"Data": self.dataMenuHandler,
                 "Curve": self.curveMenuHandler,
                 "Axes": self.axesMenuHandler,
                 "Title": self.titleMenuHandler,
                 "Legend": self.legendMenuHandler}

        menuButtons = dict()
        for menuKey in menus.keys():
            menuButtons[menuKey] = ctk.CTkButton(master=frame,
                                                 text=menuKey, text_font=("Arial", 12, "bold"),
                                                 command=menus[menuKey],
                                                 corner_radius=0, height=40, pady=1)
            menuButtons[menuKey].pack(fill=X)

        return frame

    def createDataMenuFrame(self):
        frame = ctk.CTkFrame(master=self, corner_radius=0)

        frame.configure(fg_color='white')

        return frame

    def createAxesMenuFrame(self, plot):

        y = IntVar()

        frame = ctk.CTkFrame(master=self, corner_radius=0, fg_color="#363636")

        scrollbar = ctk.CTkScrollbar(master=frame, orientation="vertical")
        scrollbar.pack()

        frame.configure(yscrollcommand=scrollbar.get)

        # Axe Names
        axes = ("X", "Y", "Y2")

        axesInterface = dict()
        for axe in axes:
            # Logic for enabling second Y axe
            def enableSecondaryYAxes():
                if y.get() == 0:
                    axesInterface["Y2"].lower()
                else:
                    axesInterface["Y2"].lift()

            # Creates checkbox that selects if secondary Y axe is enabled
            if axe == "Y2":
                ctk.CTkCheckBox(master=frame, text="Enable Secondary Y Axe", variable=y,
                                onvalue=1, offvalue=0, command=enableSecondaryYAxes).\
                    pack(fill=X, padx=20, pady=5, ipadx=10)

            # Creates a frame where the inputs for each axe will be placed
            axesInterface[axe] = ctk.CTkFrame(master=frame, corner_radius=10, height=120)
            if axe == "Y2":
                axesInterface[axe].lower()
            axesInterface[axe].pack(fill=X, padx=10, pady=5)

            # Separates each axes frame into 3 columns of same weight
            for column in range(3):
                axesInterface[axe].columnconfigure(column, weight=1)

            ctk.CTkLabel(master=axesInterface[axe], text=axe+" Axe", text_font=("Arial", 12, "bold")).\
                grid(column=0, columnspan=3, row=0)

            # Generates radio buttons for choosing axe scale
            plot.axesScaleType[axe] = ctk.StringVar(value="lin")

            ctk.CTkLabel(master=axesInterface[axe],
                         text="Scale", anchor=ctk.W, text_font=("Arial", 11)).\
                grid(sticky=W, column=0, ipadx=10, padx=10, pady=10, row=1)
            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesScaleType[axe],
                               text="Linear", value="lin").\
                grid(sticky=W, column=0, padx=10, ipady=5, row=2)

            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesScaleType[axe],
                               text="Logarithmic", value="log").\
                grid(sticky=W, column=0, padx=10, ipady=5, row=3)

            # Generates areas to define axe limits
            plot.axesLimitsType[axe] = ctk.StringVar(value="auto")

            ctk.CTkLabel(master=axesInterface[axe],
                         text="Limits", anchor=ctk.W, text_font=("Arial", 11)). \
                grid(sticky=W, column=1, ipadx=10, padx=0, pady=10, row=1)

            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesLimitsType[axe],
                               text="Auto", value="auto").\
                grid(sticky=W, column=1, padx=0, ipady=5, row=2)
            ctk.CTkRadioButton(master=axesInterface[axe], variable=plot.axesLimitsType[axe],
                               text="Manual", value="manual").\
                grid(sticky=W, column=1, padx=0, ipady=5, row=3)

            plot.axesLimitsMax[axe] = StringVar(value="max")
            ctk.CTkLabel(master=axesInterface[axe], text="Max:", anchor=ctk.W).\
                grid(sticky=W, column=1, row=4)
            ctk.CTkEntry(master=axesInterface[axe], textvariable=plot.axesLimitsMax[axe], width=100).\
                grid(sticky=W, column=1, padx=40, row=4)

            plot.axesLimitsMin[axe] = StringVar(value="min")
            ctk.CTkLabel(master=axesInterface[axe], text="Min:", anchor=ctk.W). \
                grid(sticky=W, column=1, row=5)
            ctk.CTkEntry(master=axesInterface[axe], textvariable=plot.axesLimitsMin[axe], width=100).\
                grid(sticky=W, column=1, padx=40, row=5)

            ctk.CTkLabel(master=axesInterface[axe], text="", height=10).grid(column=1, row=6)

            # Axes personalisation
            ctk.CTkLabel(master=axesInterface[axe],
                         text="Personalization", anchor=ctk.W, text_font=("Arial", 11)). \
                grid(sticky=W, column=2, ipadx=10, padx=0, pady=10, row=1)

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