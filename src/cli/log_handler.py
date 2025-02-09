import logging

from textual.widgets import Static
from watchdog.events import FileSystemEventHandler


class LogWidget(Static):
    def __init__(self, log_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_file = log_file
        self.log_lines = []
        self.max_lines = 10  # Number of lines to display
        self.load_initial_lines()

    def load_initial_lines(self):
        """Load the last `max_lines` from the log file."""
        try:
            with open("film.log", "r") as file:
                self.log_lines = file.readlines()[-self.max_lines :]
                self.update("\n".join(self.log_lines))
        except FileNotFoundError:
            self.update("Log file not found.")

    def update_log(self, new_lines):
        """Update the widget with new log lines."""
        self.log_lines.extend([line for line in new_lines if line.startswith("src.")])
        if len(self.log_lines) > self.max_lines:
            self.log_lines = self.log_lines[-self.max_lines :]
        self.update("\n".join(self.log_lines))


class LogFileHandler(FileSystemEventHandler):
    def __init__(self, log_widget):
        super().__init__()
        self.log_widget = log_widget

    def on_modified(self, event):
        """Called when the log file is modified."""
        if event.src_path == self.log_widget.log_file:
            with open(self.log_widget.log_file, "r") as file:
                new_lines = file.readlines()[len(self.log_widget.log_lines) :]
                if new_lines:
                    self.log_widget.update_log(new_lines)
