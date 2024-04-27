import wx
import wx.grid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from scipy import stats


class RegressionApp(wx.App):
    def __init__(self, redirect=False):
        wx.App.__init__(self, redirect)

    def OnInit(self):
        self.frame = RegressionFrame(
            None, title="Linear Regression Tool", size=(800, 600)
        )
        self.frame.Show()
        return True


class RegressionFrame(wx.Frame):
    def __init__(self, parent, title, size=(800, 600)):
        super().__init__(parent, title=title, size=size)

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        input_panel = wx.Panel(panel)
        input_box = wx.GridBagSizer(5, 5)

        x_label = wx.StaticText(
            input_panel,
            label="x - Values",
            style=wx.ALIGN_LEFT,
        )
        self.x_input = wx.TextCtrl(
            input_panel,
            size=(500, -1),
            style=wx.TE_PROCESS_ENTER,
            value="1, 2, 3, 4, 5",
        )
        y_label = wx.StaticText(
            input_panel, label="y - Values", style=wx.ALIGN_LEFT, size=(70, 20)
        )
        self.y_input = wx.TextCtrl(
            input_panel,
            size=(500, -1),
            style=wx.TE_PROCESS_ENTER,
            value="1, 4, 9, 16, 25",
        )

        # Space |
        # Label | Input
        # Space |
        # Label | Input
        # Space |
        input_box.Add(size=(-1, -1), pos=(0, 0))
        input_box.Add(x_label, pos=(1, 0), flag=wx.EXPAND)
        input_box.Add(self.x_input, pos=(0, 1), span=(2, 1), flag=wx.EXPAND)
        input_box.Add(size=(-1, -1), pos=(2, 0), span=(1, 2))
        input_box.Add(size=(-1, -1), pos=(3, 0))
        input_box.Add(y_label, pos=(4, 0), flag=wx.EXPAND)
        input_box.Add(self.y_input, pos=(3, 1), span=(2, 1), flag=wx.EXPAND)

        input_panel.SetSizer(input_box)

        box.Add(input_panel, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(box)


if __name__ == "__main__":
    app = RegressionApp(False)
    app.MainLoop()
