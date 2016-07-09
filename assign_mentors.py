import sys,json

mentorFileName = sys.argv[1] #These are the cleaned JSON files
menteeFileName = sys.argv[2]

mentorFile = open(mentorFileName, "rb")
menteeFile = open(menteeFileName, "rb")

mentorList = json.load(mentorFile)
menteeList = json.load(menteeFile)
 