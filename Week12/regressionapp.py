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
        # input_panel.SetBackgroundColour(wx.Colour(255, 0, 0))
        input_box = wx.FlexGridSizer(2, 3, 5, 5)

        x_label = wx.StaticText(
            input_panel,
            label="x - Values",
            style=wx.ALIGN_LEFT,
        )
        self.x_input = wx.TextCtrl(
            input_panel,
            style=wx.TE_PROCESS_ENTER | wx.EXPAND,
            value="1, 2, 3, 4, 5",
        )
        y_label = wx.StaticText(input_panel, label="y - Values", style=wx.ALIGN_LEFT)
        self.y_input = wx.TextCtrl(
            input_panel,
            style=wx.TE_PROCESS_ENTER,
            value="1, 4, 9, 16, 25",
        )
        clear_button = wx.Button(input_panel, label="Clear")
        clear_button.Bind(wx.EVT_BUTTON, self.on_clear)
        run_button = wx.Button(input_panel, label="Run")
        run_button.Bind(wx.EVT_BUTTON, self.on_run)

        input_box.Add(x_label, 0, wx.ALL, 5)
        input_box.Add(self.x_input, 1, wx.ALL | wx.EXPAND, 0)
        input_box.Add(clear_button, 0, wx.ALL, 5)
        input_box.Add(y_label, 0, wx.ALL, 5)
        input_box.Add(self.y_input, 1, wx.ALL | wx.EXPAND, 0)
        input_box.Add(run_button, 0, wx.ALL, 5)
        input_box.AddGrowableCol(1, 1)

        input_panel.SetSizer(input_box)
        # input_box.Fit(input_panel)
        # input_panel.Layout()

        box.Add(input_panel, 0, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(box)
        # box.Fit(self)
        # panel.Layout()
        panel.Bind(wx.EVT_SIZE, self.on_size)
        input_panel.Bind(wx.EVT_SIZE, self.on_size_input_panel)

    def on_size_input_panel(self, event):
        print(f"Input Panel Resized to: {event.GetSize()}")
        event.Skip()
        self.Refresh()

    def on_size(self, event):
        print(f"Resized to: {event.GetSize()}")
        event.Skip()
        self.Refresh()

    def on_clear(self, event):
        self.x_input.SetValue("")
        self.y_input.SetValue("")

    def on_run(self, event):
        x_values = np.array([float(x) for x in self.x_input.GetValue().split(",")])
        y_values = np.array([float(y) for y in self.y_input.GetValue().split(",")])

        slope, intercept, r_value, p_value, std_err = stats.linregress(
            x_values, y_values
        )
        line = f"y = {slope:.2f}x + {intercept:.2f}"
        r_squared = f"R-squared: {r_value ** 2:.2f}"

        plt.plot(x_values, y_values, "o", label="original data")
        plt.plot(x_values, slope * x_values + intercept, "r", label="fitted line")
        plt.legend()
        plt.title(f"Linear Regression\n{line}\n{r_squared}")
        plt.show()


if __name__ == "__main__":
    app = RegressionApp(False)
    app.MainLoop()
