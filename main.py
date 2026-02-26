import rumps

import time

class PomodoroBar(rumps.App):
    def __init__(self):
        super().__init__(
            name="PomodoroBar",
            icon="icons/menu_icon.png",
            template=True
        )
        self.menu = ["Start", "Pause", "Resume"]
        self.timer = None
        self.time_left = 0

    @rumps.clicked("Start")
    def start_pomodoro(self, _):
        self.time_left = 25 * 60  # 25 minutes in seconds
        self.title = self._format_time(self.time_left)
        if self.timer:
            self.timer.stop()
        self.timer = rumps.Timer(self._on_tick, 1)
        self.timer.start()
        rumps.notification("Pomodoro Started", "25 minutes timer", "Good luck!")

    @rumps.clicked("Pause")
    def pause(self, _):
        if self.timer:
            self.timer.stop()
            self.timer = None
  
    @rumps.clicked("Resume")
    def resume(self, _):
        if self.timer is None and self.time_left > 0:
            self.timer = rumps.Timer(self._on_tick, 1)
            self.timer.start()
  
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