import sys
import time

import seven_segment_display_module

try:
    while True:
        print("\n" * 60)

        current_time = time.localtime()
        hours = str(current_time.tm_hour % 12)
        if hours == 0:
            hours = "12"
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        hour_digits = seven_segment_display_module.sev_seg_disp(hours, 2)
        hour_top_row, hour_middle_row, hour_bottom_row = hour_digits.splitlines()

        minute_digits = seven_segment_display_module.sev_seg_disp(minutes, 2)
        minute_top_row, minute_middle_row, minute_bottom_row = minute_digits.splitlines()

        second_digits = seven_segment_display_module.sev_seg_disp(seconds, 2)
        second_top_row, second_middle_row, second_bottom_row = second_digits.splitlines()

        # Displaying the digits.
        print(hour_top_row + '     ' + minute_top_row + '     ' + second_top_row)
        print(hour_middle_row + '  *  ' + minute_middle_row + '  *  ' + second_middle_row)
        print(hour_bottom_row + '  *  ' + minute_bottom_row + '  *  ' + second_bottom_row)

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    sys.exit()
