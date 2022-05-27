# util that merges Windows IIS logs etc. that have one log file for every day
# merges all day files in a folder into one log file keeping all info
# currently not i the Common Log Format: https://en.wikipedia.org/wiki/Common_Log_Format

import sys, os, datetime, re
from os.path import basename, join


def mergeLogs(foldername, outputFile):

    with open(outputFile, 'w') as outfile:
        outfile.write("#Fields: date time c-ip cs-method cs-uri-stem sc-status" + "\n")

        for logfile in sorted(os.listdir(foldername)):
            if len(logfile) > 5 and logfile[0:2] == "ex" and logfile[-3:] == "log":
                date = datetime.datetime.strptime(logfile[2:-4], "%y%m%d")
                filecontent = open(join(foldername, logfile), "r").read()
                for line in filecontent.split("\n"):
                    if len(line) == 0 or line[0] == "#":
                        continue
                        
                    if re.match("(\d*:\d*:\d*)", line[0:8]):
                        outfile.write("\n" + date.strftime("%Y-%m-%d") + " " + line)
                    else:
                        outfile.write(line)
        
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: buildLog.py <foldername> <outputFile>")
        sys.exit(0)
    mergeLogs(sys.argv[1], sys.argv[2])