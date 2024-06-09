import time
from tqdm import tqdm
from plyer import notification

def countdown(minutes, message):
    seconds = minutes * 60
    for remaining in tqdm(range(seconds), desc=message, ncols=100):
        time.sleep(1)

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=20
    )

def pomodoro_timer(work_duration, short_break_duration, long_break_duration, cycles):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}: Work for {work_duration} minutes")
        countdown(work_duration, "Working")
        notify("Pomodoro Timer", "Work session complete! Take a break.")

        if cycle % 4 == 0:
            print(f"Take a long break for {long_break_duration} minutes")
            countdown(long_break_duration, "Long Break")
            notify("Pomodoro Timer", "Long break complete! Get ready for the next cycle.")
        else:
            print(f"Take a short break for {short_break_duration} minutes")
            countdown(short_break_duration, "Short Break")
            notify("Pomodoro Timer", "Short break complete! Get ready for the next cycle.")
            
        print("Pomodoro cycle complete!")

if __name__ == "__main__":
    WORK_DURATION = 25  # in minutes
    SHORT_BREAK_DURATION = 5  # in minutes
    LONG_BREAK_DURATION = 15  # in minutes
    CYCLES = 4  # number of Pomodoro cycles

    pomodoro_timer(WORK_DURATION, SHORT_BREAK_DURATION, LONG_BREAK_DURATION, CYCLES)
