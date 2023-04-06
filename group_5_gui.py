import tkinter as tk
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# initialize y data:
y_data = []
days_data = []

# DYNAMICAL DISPLAY
class Display:

    def __init__(self, root,y_data,days_data):
        self.y_data = y_data
        self.days_data = days_data
        self.root = root
        self.root.title("Average Temperature in Vietnam in 100 days from Nov 1, 2022")

        # Initialize data
        self.data = []
        self.x_data=[]
        # assign the first 5 values
        for i in range(1):
            self.data.append(y_data.pop(0))
            self.x_data.append(days_data.pop(0))

        # Initialize figure and axis for line chart
        self.fig_line = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax_line = self.fig_line.add_subplot(111)
        self.ax_line.set_title("Line Chart")
        self.ax_line.set_ylim([0, 35])
        self.line_chart = FigureCanvasTkAgg(self.fig_line, master=root)
        self.line_chart.get_tk_widget().grid(row=0, column=0)

        # Initialize figure and axis for bar chart
        self.fig_bar = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax_bar = self.fig_bar.add_subplot(111)
        self.ax_bar.set_title("Bar Chart")
        self.bar_chart = FigureCanvasTkAgg(self.fig_bar, master=root)
        self.bar_chart.get_tk_widget().grid(row=0, column=1)

        # Initialize button
        self.go_button = tk.Button(root, text="Start Demo", command=self.initUI)
        self.go_button.grid(row=1, column=0, columnspan=2)

        # Initialize thread for updating data
        self.update_thread = None

    def initUI(self):
        self.update_thread = threading.Thread(target=self.update_values)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_values(self):

        while y_data != []:
            # Generate new data and update dataset
            new_data = y_data.pop(0)
            self.data.append(new_data)
            self.data.pop(0)

            new_x_data = days_data.pop(0)
            self.x_data.append(new_x_data)
            self.x_data.pop(0)

            # Update line chart
            self.ax_line.clear()
            self.ax_line.plot(self.x_data,self.data)
            self.ax_line.set_title("Line Chart")
            self.ax_line.set_ylim([0, 35])
            self.ax_line.set_xticks(np.arange(min(self.x_data), max(self.x_data)+1, 1))
            self.line_chart.draw()

            # Update bar chart
            self.ax_bar.clear()
            self.ax_bar.set_title("Bar Chart")
            self.ax_bar.set_ylim([0, 35])
            self.ax_bar.bar(self.x_data, self.data)
            self.ax_bar.set_xticks(np.arange(min(self.x_data), max(self.x_data)+1, 1))
            self.bar_chart.draw()

            # Sleep for a short while (0.5 of a second)
            time.sleep(0.5)

    def stop_update_thread(self):
        if self.update_thread is not None:
            self.update_thread.stop()
            self.update_thread = None


if __name__ == '__main__':
    root = tk.Tk()
    app = Display(root)
    root.mainloop()
