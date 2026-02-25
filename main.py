import rumps

import time

class PomodoroBar(rumps.App):
    def __init__(self):
        super(PomodoroBar, self).__init__("PomodoroBar")
        self.menu = ["Start Pomodoro"]
        self.timer = None
        self.time_left = 0

    @rumps.clicked("Start Pomodoro")
    def start_pomodoro(self, _):
        self.time_left = 25 * 60  # 25 minutes in seconds
        self.title = self._format_time(self.time_left)
        if self.timer:
            self.timer.stop()
        self.timer = rumps.Timer(self._on_tick, 1)
        self.timer.start()
        rumps.notification("Pomodoro Started", "25 minutes timer", "Good luck!")

    def _on_tick(self, sender):
        if self.time_left > 0:
            self.time_left -= 1
            self.title = self._format_time(self.time_left)
        else:
            self.title = "PomodoroBar"
            sender.stop()
            rumps.notification("Pomodoro Finished", "Take a break!", "Well done!")

    def _format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

if __name__ == "__main__":
    PomodoroBar().run()