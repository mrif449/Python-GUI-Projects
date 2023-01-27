import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer App")

        self.time = tk.StringVar()
        self.time.set("00:00")

        self.label = tk.Label(master, textvariable=self.time)
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.interval = None

    def start(self):
        if not self.running:
            self.running = True
            self.interval = self.master.after(1000, self.tick)

    def stop(self):
        if self.running:
            self.running = False
            self.master.after_cancel(self.interval)

    def reset(self):
        self.stop()
        self.minutes = 0
        self.seconds = 0
        self.time.set("00:00")

    def tick(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
            self.time.set(f"{self.minutes:02d}:{self.seconds:02d}")
            self.interval = self.master.after(1000, self.tick)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
