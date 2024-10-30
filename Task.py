import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"{hrs:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    time_input = input("Insert time to count down (h:m:s) ")
    h, m, s = map(int, time_input.split(':'))
    countdown_timer(h, m, s)
