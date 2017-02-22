
import requests
import RaceFunctions


#aList = [123, 'xyz', 'zara', 'abc'];
#aList.append( 2009 );
#print "Updated List : ", aList




#Get HTML for the page

#Main
#page = requests.get('http://www.racingaustralia.horse/FreeFields/Form.aspx?Key=2016Apr23,NSW,Rosehill%20Gardens')

#Test 1
page = requests.get('http://www.racingaustralia.horse/FreeFields/Form.aspx?Key=2016May07,NSW,Cobar')
print("Site Downloaded")
# http://www.racingaustralia.horse/FreeFields/Form.aspx?Key=2016May07,NSW,Cobar

#Test 2
#page = requests.get("http://www.racingaustralia.horse/FreeFields/Results.aspx?Key=2016Apr28,NSW,Wyong")



#Put the HTML code to a varible
searchString = page.text

#This is backup (searchString) of the string incase needed later
tempString = searchString


#=====================================

#This "Hcp Rating" is the last heading before the horses are listed
#Main
StrLocation = tempString.find('<th class="hcp">Hcp Rating</th>')

#Test 1
#StrLocation = tempString.find('<th class="penalty">Penalty</th>')


#This removes the stuff from the left of the string and places the left over
#in the new var tempString.




tempString = tempString[StrLocation:]



#Race Number
RaceNumber = 1

HorseStrings = []

y = 1

for x in range(0, 9):
    TextToSave = ""
    TextToSave = "Race Number," + str(RaceNumber)
    tempTextToSave, tempString = RaceFunctions.ExtractHorseSummary(tempString)
    HorseStrings.append(TextToSave + tempTextToSave)

print("====================")



#print(RaceFunctions.ExtractHorseNameFromArray(HorseStrings[0]))


for x in range(0, 9):

    #Find Horse
    LeftPoint = tempString.find(RaceFunctions.ExtractHorseNameFromArray(HorseStrings[x]))
    tempString = tempString[LeftPoint:]


    tempString, HorseRecord = RaceFunctions.ExtractInfo(tempString, '<b>Record:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Record," + str(HorseRecord)

    tempString, HorsePrizemoney = RaceFunctions.ExtractInfo(tempString, '<b>Prizemoney:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Prizemoney," + str(HorsePrizemoney)

    tempString, HorseFirstUp = RaceFunctions.ExtractInfo(tempString, '<b>1st Up:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",1st Up," + str(HorseFirstUp)

    tempString, HorseSecondUp = RaceFunctions.ExtractInfo(tempString, '<b>2nd Up:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",2st Up," + str(HorseSecondUp)

    tempString, HorseTrack = RaceFunctions.ExtractInfo(tempString, '<b>Track:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Track," + str(HorseTrack)

    tempString, HorseDist = RaceFunctions.ExtractInfo(tempString, '<b>Dist:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Dist," + str(HorseDist)

    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Track/Dist:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Track/Dist," + str(tempHorseInfo)

    '''
    'This is currently turned off as not available with all horses
    '''
    #Distance(s) Won:
    #tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Distance(s) Won:</b>', '<br')
    #HorseStrings[x] =  HorseStrings[x] + ",Distance(s) Won," + str(tempHorseInfo)

    #Firm:
    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Firm:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Firm," + str(tempHorseInfo)

    #Good:
    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Good:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Good," + str(tempHorseInfo)

    #Soft:
    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Soft:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Soft," + str(tempHorseInfo)

    #Heavy:
    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Heavy:</b>', '&')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Heavy," + str(tempHorseInfo)



    #Synthetic:
    tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, '<b>Synthetic:</b>', '</td>')
    HorseStrings[x] =  HorseStrings[x] + ",Horse Synthetic," + str(tempHorseInfo)




    nextHorseIndex = tempString.find('</table>')
    nextPositionIndex = tempString.find("<td class='Pos'>")


    #nextHorseIndex = tempString.find('</table>')
    #nextPositionIndex = tempString.find("<td class='Pos'>")

	#if Horse Position index is before the next horse index then there is a position listing
    while (tempString.find("<td class='Pos'>")) < (tempString.find('</table>')):
        tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, "<td class='Pos'>", '</td>')
        HorseStrings[x] =  HorseStrings[x] + ",Horse Position," + str(tempHorseInfo)

        tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, "target='_blank'>", '</a></b>')
        HorseStrings[x] =  HorseStrings[x] + ",Location/Track," + str(tempHorseInfo)

        tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, "</a></b>", '<a class')
        HorseStrings[x] =  HorseStrings[x] + ",Track Info," + str(tempHorseInfo)
'''
	#if Horse Position index is before the next horse index then there is a position listing
    if nextPositionIndex < nextHorseIndex:
        tempString, tempHorseInfo = RaceFunctions.ExtractInfo(tempString, "<td class='Pos'>", '</td>')
        HorseStrings[x] =  HorseStrings[x] + ",Horse Position," + str(tempHorseInfo)

'''













################################
#Save the completed csv file
RaceFunctions.SaveFile(HorseStrings)
#End
################################print

print("Done")













''''
>>> x = "Hello World!"
>>> x[2:]
'llo World!'
>>> x[:2]
'He'
>>> x[:-2]
'Hello Worl'
>>> x[-2:]
'd!'
>>> x[2:-2]
'llo Worl'
'''

#>>> f.write('This is a test\n')
#, is used to seperate colums as the file is a csv file



''' Potential Class Stuff
class HorseInfo:
    def __init__(self):

    #Get Race Number
    def Race_Number(self, Number):
        self.RaceNumber = Number

    #Get Horse Number
    def Race_Number(self, Number):
        self.RaceNumber = Number

    #Get Horse Name
    def Race_Number(self, Number):
        self.RaceNumber = Number
'''
