import threading

import cv2
import matplotlib.pyplot as plt
import numpy as np


class ImagePlots:
    mutex = threading.Lock()

    def __init__(self):
        self.fig, self.axes = plt.subplots(nrows=2, ncols=2)
        self.parade = self.axes[0][0]

    def __enter__(self, *args):
        return self

    def __exit__(self, *args):
        plt.close(self.fig)

    def render(self, data: bytes):
        with self.mutex:
            self.draw_parade(data)

    def new_image(self, data: bytes):
        if self.mutex.locked():
            return

        # spawn a new thread.
        thread = threading.Thread(
            target=self.render,
            args=(data,),
            daemon=True,
        )

        thread.start()
        plt.pause(0.001)

    def draw_parade(self, data: bytes):
        # Convert bytes to numpy array
        image_array = np.frombuffer(data, dtype=np.uint8)

        # Decode the image
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Invalid image data")

        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Split the image into channels
        R, G, B = cv2.split(img)

        # Create x-axis values (column indices)
        x = np.arange(img.shape[1])  # Image width

        # Plot each channel with vertical stacking
        for i, (channel, color) in enumerate(zip([R, G, B], ["red", "green", "blue"])):
            # Normalize intensity values to 0-1 for plotting
            channel = channel.astype(np.float32) / 255.0

            # Scatter plot with vertical shift for stacking
            y_values = channel + i * 1.1  # Stacking each channel
            self.parade.scatter(
                np.tile(x, img.shape[0]),
                y_values.flatten(),
                color=color,
                s=0.1,
                alpha=0.5,
            )

        # Adjust plot aesthetics
        self.parade.set_xlim(0, img.shape[1])
        self.parade.set_ylim(-0.1, 3.3)
        self.parade.set_xticks([])
        self.parade.set_yticks([])
        self.parade.set_title("RGB Parade")
        self.parade.set_facecolor("black")
