import time
import sys, subprocess

representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    ':': ('   ', '   ', '  #', '   ', '  #'),
}

def clear_screen():
    operating_system = sys.platform
    if operating_system == "win32":
        subprocess.run('cls', shell=True)
    elif operating_system == "linux" or operating_system == "darwin":
        subprocess.run('clear', shell=True)

def seven_segment(number):
    digits = [representations[digit] for digit in str(number)]
    lines = []
    for i in range(5):
        lines.append("  ".join(segment[i] for segment in digits))
    return lines

def pomo_timer(minutes, rest, times):
    my_time = minutes * 60
    for i in range(times):
        for x in range(my_time, 0, -1):
            ss = x % 60
            mm = int(x / 60) % 60
            clear_screen()
            
            minutes_segments = seven_segment(f"{mm:02}")
            seconds_segments = seven_segment(f"{ss:02}")
            colon_segments = seven_segment(":")

            print("-------TIME TO WORK!-------\n")
            for line_min, line_colon, line_sec in zip(minutes_segments, colon_segments, seconds_segments):
                print(line_min + "    " + line_colon + "    " + line_sec)
            
            time.sleep(1)

        for y in range(rest * 60, 0, -1):
            ss = y % 60
            mm = int(y / 60) % 60
            clear_screen()

            minutes_segments = seven_segment(f"{mm:02}")
            seconds_segments = seven_segment(f"{ss:02}")
            colon_segments = seven_segment(":")

            print("-------TIME TO REST!-------\n")
            for line_min, line_colon, line_sec in zip(minutes_segments, colon_segments, seconds_segments):
                print(line_min + "    " + line_colon + "    " + line_sec)
                 
            time.sleep(1)

if __name__ == "__main__":
    activity_time = int(input("Activity Time (minutes): "))
    rest_time = int(input("Rest Time (minutes): "))
    pomodoro_number = int(input("Pomodoro Number (times): "))

    pomo_timer(activity_time, rest_time, pomodoro_number)
