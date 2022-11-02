def number_of_melons(day, filepath): # Function takes a day and filepath in place of parameters
    """Iterates through a list a prints a report for each day"""

    print(f"Day {day}") # Prints the numbe rof the day
    melon_report = open(filepath) # Opens the log file


    for line in melon_report: # Iterates through each line in log file
        line = line.rstrip() # Strips whitespace from right side
        words = line.split('|') # Creates new list

        melon = words[0] # Item from list
        count = words[1] # Item from list
        amount = words[2] # Item from list

        print(f"Delivered {count} {melon}s for total of ${amount}") # Displays result
    melon_report.close() # Closes log file
