def number_of_melons(day, filepath):
    """Iterates through a list a prints a report for each day"""

    print(f"Day {day}")
    melon_report = open(filepath)


    for line in melon_report:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    melon_report.close()
