import tkinter as tk


class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Timer")

        # Create variables to store timer values
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        # Create timer label
        self.timer_label = tk.Label(
            master, text="00:00:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        # Create start and stop buttons
        self.start_button = tk.Button(master, text="Start", font=(
            "Helvetica", 14), command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(master, text="Stop", font=(
            "Helvetica", 14), command=self.stop_timer, state="disabled")
        self.stop_button.pack(pady=10)

        # Create timer update function
        self.update_timer = None

    def start_timer(self):
        # Disable start button and enable stop button
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        # Start timer
        self.update_timer = self.master.after(1000, self.update_timer_label)

    def stop_timer(self):
        # Enable start button and disable stop button
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

        # Reset timer values
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        # Cancel timer update function
        if self.update_timer is not None:
            self.master.after_cancel(self.update_timer)
            self.update_timer = None

        # Update timer label
        self.timer_label.config(text="00:00:00")

    def update_timer_label(self):
        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Update timer label
        self.timer_label.config(
            text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        # Increment seconds
        self.seconds += 1

        # Schedule next update
        self.update_timer = self.master.after(1000, self.update_timer_label)


root = tk.Tk()
root.geometry("300x400")
app = Timer(root)
root.mainloop()
