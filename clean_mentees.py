import csv,json,sys
def menteeCleaner(fileName):
    try:
        menteeCsv = csv.reader(open(fileName, 'rb'))
        mentees = list(menteeCsv)
        dictmentees = []
        for row in mentees:
            tempDict={}
            tempDict['name'] = row[0]
            tempDict['rollNo'] = row[1]
            tempDict['gender'] = row[2]
            tempDict['email'] = row[3]
            tempDict['dept'] = row[4]
            tempDict['dasa'] = row[5]
            tempDict['language'] = row[6]
            tempDict['state'] = row[7]
            tempDict["other_langs"] = row[8]
            tempDict["mobile"] = row[9]
            dictmentees.append(tempDict)
        with open('mentees_raw_data_sample.json', 'w') as outfile:
            dictmentees = sorted(dictmentees, key=lambda student: student["dept"])
            json.dump(dictmentees, outfile)
    except IOError:
        print("File could not be found.")
        sys.exit()
if __name__=="__main__":
    menteeFileName = sys.argv[1]
    menteeCleaner(menteeFileName)