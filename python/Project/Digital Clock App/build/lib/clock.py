import time
import os


def clock(format=None):
    def format12(box):
        while True:
            try:      
                os.system("cls")
                print(box.format(time.strftime("%I:%M:%S"), time.strftime("[%p]")), flush= True)
                time.sleep(1)
            except KeyboardInterrupt:
                os.system("cls")
                print(box.format(time.strftime("%I:%M:%S"), time.strftime("[%p]")), flush=True)
                print("Bye!")
                break
    def format24(box):
        while True:
            try:
                os.system("cls")
                print(box.format(time.strftime("%H:%M:%S"), "    "), flush= True)
                time.sleep(1)
            except KeyboardInterrupt:
                os.system("cls")
                print(box.format(time.strftime("%H:%M:%S"), "    "), flush= True)
                print("Bye!")
                break
    

    box = """\n\n\n\n\n\n\n             
    \t\t\t\t\t\t\t\t\t\t\t          -= -=- =-
    \t\t\t\t\t\t\t\t\t\t\t       = -         - =
    \t\t\t\t\t\t\t\t\t\t\t    = -               - =
    \t\t\t\t\t\t\t\t\t\t\t  = -                   - =
    \t\t\t\t\t\t\t\t\t\t\t ==                       ==
    \t\t\t\t\t\t\t\t\t\t\t =-       {}        -=
    \t\t\t\t\t\t\t\t\t\t\t ==                       ==
    \t\t\t\t\t\t\t\t\t\t\t  = -                   - =
    \t\t\t\t\t\t\t\t\t\t\t    = -     {}      - = 
    \t\t\t\t\t\t\t\t\t\t\t       = -         - = 
    \t\t\t\t\t\t\t\t\t\t\t          -= -=- =-    

    """

    if format:       # format specified; runs.
        if format not in (12,24):
            print("Error: Invalid format. Format can only be 12 or 24.")
        elif format == 12:
            format12(box)
        else:
            format24(box)


    else:            # no format specified; runs.      
        format = input("\ta. 12 hour format\n\tb. 24 hour format\nEnter time format (a or b): ")# takes format from user input.
        
        if format.lower() not in ('a','b'):# check format a or b or not
            print("Error: Invalid format. Choose a or b.")
        elif format.lower() == 'a':
            format12(box)
        else:
            format24(box)

def info():
    """
    Clock Module Information:

    This module provides a simple digital clock that can display the current time in either 12-hour or 24-hour format.
    
    Usage:
    - Run the `clock()` function to start the clock.
    - You can specify the format as `clock(12)` for 12-hour format or `clock(24)` for 24-hour format.
    - If no format is specified, the user will be prompted to choose one.
    - The clock will run continuously until interrupted.

    How to Stop:
    - To stop the clock, press `Ctrl + C` in the terminal or console where the clock is running.
    
    Author:
    - Created by Raiyan Khan.

    Version:
    - 1.0.0
    
    License:
    - 9F7C-6A5D-3B2E-1A8B

    Additional Notes:
    - The clock display uses ASCII art for a decorative border.
    - This module is for educational and demonstration purposes.
    
    """
    print(info.__doc__)
        
def location():
    """
/home/ [name of user] /.local/lib/python3.10/site-packages
    """  
    print(location.__doc__)
