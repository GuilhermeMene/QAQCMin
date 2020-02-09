# -*- coding: utf-8 -*-

##########################################
#Name: Guilherme Mene Ale Primo
#Date: 02/02/2020
# QAQC geochemical data control and report
##########################################

import wx
import wx.lib.agw.aui as aui
import wx.lib.mixins.inspection as wit

import matplotlib.figure as Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar


class STD_Plot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)

        #set the plot settings
        self.fig = Figure()
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        
        #set sizer of data into panel
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)


class PlotNotebook(wx.Panel):
    def __init__(self, parent, id=-1):
        wx.Panel.__init__(self, parent, id=id)

        #set the note for input data
        self.nb = aui.AuiNotebook(self)
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)


    #set function to add the pages into notebook
    def add(self, name="Plot"):
        page = STD_Plot(self.nb)
        self.nb.AddPage(page, name)
        return page.figure


