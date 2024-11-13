import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds >= 0:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"{hrs:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("\nTime's up!")

def get_time_input():
    while True:
        try:
            time_input = input("Insert time to count down (h:m:s): ")
            h, m, s = map(int, time_input.split(':'))
            
            if h < 0 or m < 0 or s < 0:
                print("Error: Hours, minutes, and seconds must be non-negative integers.")
                continue

            if m >= 60 or s >= 60:
                print("Error: Minutes and seconds must be within 0 and 59.")
                continue

            return h, m, s
        except ValueError:
            print("Invalid format. Please enter time in the format h:m:s, using integers.")

if __name__ == "__main__":
    hours, minutes, seconds = get_time_input()
    countdown_timer(hours, minutes, seconds)
