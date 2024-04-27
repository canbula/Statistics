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
            None, title="Linear Regression Tool", size=(800, 800)
        )
        self.frame.Show()
        return True


class RegressionFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, title=title, size=size)

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        title_label = wx.StaticText(
            panel, label="Linear Regression Tool", style=wx.ALIGN_CENTER
        )
        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        title_label.SetFont(font)
        box.Add(title_label, 0, wx.ALL | wx.EXPAND, 5)

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

        plot_panel = wx.Panel(panel)
        # plot_panel.SetBackgroundColour(wx.Colour(0, 255, 0))
        plot_box = wx.BoxSizer(wx.HORIZONTAL)

        self.figure = plt.figure()
        self.figure.patch.set_facecolor((0, 0, 0, 0))
        self.canvas = FigureCanvas(plot_panel, -1, self.figure)

        plot_box.Add(self.canvas, 1, wx.ALL | wx.EXPAND, 5)

        plot_panel.SetSizer(plot_box)
        # plot_box.Fit(plot_panel)
        # plot_panel.Layout()

        box.Add(input_panel, 0, wx.ALL | wx.EXPAND, 5)
        box.Add(plot_panel, 1, wx.ALL | wx.EXPAND, 5)

        panel.SetSizer(box)
        # box.Fit(self)
        # panel.Layout()
        panel.Bind(wx.EVT_SIZE, self.on_size)
        input_panel.Bind(wx.EVT_SIZE, self.on_size_input_panel)
        # bind the close event
        self.Bind(wx.EVT_CLOSE, self.on_close)

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
        label = f"y = {intercept:.2f} + {slope:.2f}x  (r^2={r_value ** 2:.2f})"

        self.figure.clear()
        system_appearance = wx.SystemSettings.GetAppearance()
        if system_appearance.IsDark():
            self.figure.patch.set_facecolor((0, 0, 0, 0))
            ax = self.figure.add_subplot(111)
            ax.patch.set_facecolor((0, 0, 0, 0))
            ax.spines["bottom"].set_color("white")
            ax.spines["top"].set_color("white")
            ax.spines["left"].set_color("white")
            ax.spines["right"].set_color("white")
            ax.xaxis.label.set_color("white")
            ax.yaxis.label.set_color("white")
            ax.tick_params(axis="x", colors="white")
            ax.tick_params(axis="y", colors="white")
            ax.title.set_color("white")
            # set grid color
            ax.grid(color=(0.25, 0.25, 0.25, 1))
        else:
            ax = self.figure.add_subplot(111)
        ax.set_title(label)
        ax.set_xlabel("x-values")
        ax.set_ylabel("y-values")
        ax.plot(x_values, y_values, "or")
        ax.plot(
            x_values,
            slope * x_values + intercept,
            "b-",
        )
        plt.tight_layout()
        self.canvas.draw()

    def on_close(self, event):
        plt.close(self.figure)
        self.Destroy()


if __name__ == "__main__":
    app = RegressionApp(False)
    app.MainLoop()
