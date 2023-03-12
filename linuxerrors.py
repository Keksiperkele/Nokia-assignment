"""
This script will read a log file and separate lines with potential errors in it to a 1
different file and print out the errors to the user. The errors in the file will be in JSON-format.
"""
import optparse
import datetime
import json

months = {
    #Mapping the months to their corresponding digits.
    "Jan": 1, 
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5, 
    "Jun": 6, 
    "Jul": 7,
    "Aug": 8, 
    "Sep": 9, 
    "Oct": 10, 
    "Nov": 11, 
    "Dec": 12
}

keywords = ["fail", "stop", "error", "too large", "too long"]
#I'm using the given keywords and also 'too large' and 'too long' here for date testing purposes.

parser = optparse.OptionParser()
parser.add_option(
    #This option let's the user choose the output file and directory.
    "-o",
    "--output",
    type="string",
    dest="filename",
    default="errors_in_log.txt",
    help="Choose output file and directory",
    )

parser.add_option(
    #This option let's the user choose the final day of the parsing.
    "-u",
    "--until",
    type="string",
    dest="time",
    default="0",
    help="Set a date as integers in the form of YYYY-MM-DD."
    "The script will run from the chosen day to the current day."
    )

(options, args) = parser.parse_args()

#First we try to create and open the wanted file. Default is errors_in_log.txt
try:
    open(options.filename, "x")
    errors = open(options.filename, "w")
except FileExistsError:
    errors = open(options.filename, "w")

if options.time == "0":
#If the until date isn't specified the script tries to go through the whole log file.
    try:
        #Be sure to add the correct log directory here.
        with open("dmesg.log", "r") as log:
            for line in log:
                for i in keywords:
                    if i in line:
                        errors.write(json.dumps(line))
                        print(line)
    except FileNotFoundError:
        print("File not found. Check file/script directory.")
else:
    try:
    #First we format the given date so we can check it properly from the logs.
        untildate = options.time.split("-")
        for i in range(0, len(untildate)):
            untildate[i] = int(untildate[i])
        try:
            #Be sure to run the script in the log directory.
            with open("dmesg.log", "r") as log:
                for line in log:
                    #Here we check if we have the until-date reached.
                    for i in keywords:
                        if i in line:
                            lyear = int(line[21:25])
                            lmonth = int(months[line[5:8]])
                            lday = int(line[9:11].strip())
                            if datetime.date(lyear, lmonth, lday) <= datetime.date(untildate[0], untildate[1], untildate[2]):
                                errors.write(json.dumps(line))
                                print(line)
        except FileNotFoundError:
            print("File not found. Check file/script directory.")

    except ValueError:
        print("Please check time formatting. (Use --help command for the correct form)")
    except IndexError:
        print("Please check time formatting. (Use --help command for the correct form)")
