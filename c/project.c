#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>
// Function to clear the screen
void clear_screen() {
    // This will work on most terminals to clear the screen
    printf("\033[H\033[J");
}

// Function to display the time in a simple box
void display_time(char *time_str, char *ampm) {
    clear_screen();
    printf("*********************\n");
    printf("*                   *\n");
    printf("*    %s     *\n", time_str);
    if (ampm[0] != ' ') { // Only print AM/PM if it's a 12-hour format
        printf("*       %s       *\n", ampm);
    }
    printf("*                   *\n");
    printf("*********************\n");
}

// Function to show the clock in 12-hour or 24-hour format
void show_clock(int format) {
    while (1) {
        time_t now;
        struct tm *timeinfo;
        char time_str[9]; // "HH:MM:SS" is 8 characters + 1 for null terminator
        char ampm[4] = "    "; // Space-padded for 24-hour format

        time(&now); // Get the current time
        timeinfo = localtime(&now); // Convert to local time

        // Choose format based on user input
        if (format == 12) {
            strftime(time_str, sizeof(time_str), "%I:%M:%S", timeinfo);
            strftime(ampm, sizeof(ampm), "%p", timeinfo);
        } else {
            strftime(time_str, sizeof(time_str), "%H:%M:%S", timeinfo);
        }

        // Display the time
        display_time(time_str, ampm);
        
        sleep(1); // Wait for 1 second
    }
}

int main() {
    int choice;

    // Ask the user which format to display
    printf("Choose time format:\n  1. 12-hour format\n  2. 24-hour format\nEnter your choice: ");

    scanf("%d", &choice);

    // Show the clock in the chosen format
    if (choice == 1) {
        show_clock(12); // 12-hour format
    } else if (choice == 2) {
        show_clock(24); // 24-hour format
    } else {
        printf("Invalid choice. Please enter 1 or 2.\n");
    }

    return 0;
}
