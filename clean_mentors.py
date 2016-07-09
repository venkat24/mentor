import csv,json,sys
def mentorCleaner(fileName):
    try:
        mentorCsv = csv.reader(open(fileName, 'rb'))
        mentors = list(mentorCsv)
        dictMentors = []
        for row in mentors:
            tempDict={}
            tempDict['name'] = row[1]
            tempDict['rollNo'] = row[2]
            tempDict['gender'] = row[3]
            tempDict['email'] = row[4]
            tempDict['dept'] = row[5]
            tempDict['gpa'] = float(row[6])
            tempDict['dasa'] = row[7]
            tempDict['language'] = row[8]
            tempDict['state'] = row[9]
            dictMentors.append(tempDict)
        with open('mentors_raw_data.json', 'w') as outfile:
            json.dump(dictMentors, outfile)
    except IOError:
        print("File could not be found.")
        sys.exit()
if __name__=="__main__":
    mentorFileName = sys.argv[1]
    mentorCleaner(mentorFileName)