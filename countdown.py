import sys
import time

import seven_segment_display_module

seconds_left = int(input("Please input how many second you want to countdown from."))

try:
    while True:
        print("\n" * 60)
        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600) // 60)
        seconds = str(seconds_left % 60)

        hour_digits = seven_segment_display_module.sev_seg_disp(hours, 2)
        hour_top_row, hour_middle_row, hour_bottom_row = hour_digits.splitlines()

        minute_digits = seven_segment_display_module.sev_seg_disp(minutes, 2)
        minute_top_row, minute_middle_row, minute_bottom_row = minute_digits.splitlines()

        second_digits = seven_segment_display_module.sev_seg_disp(seconds, 2)
        second_top_row, second_middle_row, second_bottom_row = second_digits.splitlines()

        # Displaying the digits.
        print(hour_top_row + "   " + minute_top_row + "   " + second_top_row)
        print(hour_middle_row + "  *  " + minute_middle_row + "  *  " + second_middle_row)
        print(hour_bottom_row + "  *  " + minute_bottom_row + "  *  " + second_bottom_row)

        if seconds_left == 0:
            print("\n")
            print("   * * * * END * * * *")
            break

        print("\n")
        print("Press Ctrl-C to quit.")
        time.sleep(1)
        seconds_left -= 1
except KeyboardInterrupt:
    sys.exit()
