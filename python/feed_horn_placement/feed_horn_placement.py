import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class FeedHornPlacementApp:
    def __init__(self, master):
        self.master = master
        master.title("Feed Horn Placement App")

        self.focal_length_label = tk.Label(master, text="Focal Length:")
        self.focal_length_label.grid(row=0, column=0, sticky='w')
        self.focal_length_entry = tk.Entry(master)
        self.focal_length_entry.grid(row=0, column=1)
        self.focal_length_entry.insert(0, "10")

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=0, column=2)

        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.grid(row=1, columnspan=3)

    def calculate(self):
        focal_length = float(self.focal_length_entry.get())
        self.visualize_dish(focal_length)

    def parabolic_reflector(self, x, y, focal_length):
        return x**2 / (4 * focal_length) + y**2 / (4 * focal_length)

    def visualize_dish(self, focal_length, resolution=100):
        x = np.linspace(-focal_length, focal_length, resolution)
        y = np.linspace(-focal_length, focal_length, resolution)
        X, Y = np.meshgrid(x, y)
        Z = self.parabolic_reflector(X, Y, focal_length)

        self.canvas.delete("all")

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.contour(X, Y, Z, levels=20)
        ax.set_xlabel('X axis (cm)')
        ax.set_ylabel('Y axis (cm)')
        ax.set_title('Parabolic Reflector Dish')
        ax.grid(True)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    app = FeedHornPlacementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
