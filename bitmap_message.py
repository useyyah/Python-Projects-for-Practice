import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Enter the message to display as bitmap.")
message = input()
if message == "":
    sys.exit()

# Loop over each line in the bitmap.
for line in bitmap.splitlines():
    # Loop over each character in the line.
    for i, bit in enumerate(line):
        if bit == " ":
            print(" ", end="")  # Print an empty space for each space in the bitmap.
        else:
            print(message[i % len(message)], end="")
    print("\n")
