def PrintName(str):
   "function_docstring"
   print(str)
   return

def ExtractInfo(tempString, searchStarting, searchEnding):

    
    #LeftPoint = tempString.find(' target="_blank">')
    LeftPoint = tempString.find(searchStarting)

    #tempString = tempString[LeftPoint + 17:]
    tempString = tempString[LeftPoint + len(searchStarting):]

    #RightPoint = tempString.find('</a>')
    RightPoint = tempString.find(searchEnding)


    FoundString = tempString[:RightPoint]

    FoundString = FoundString.replace(',','')
    FoundString = FoundString.strip()

    return (tempString, FoundString)






def ExtractHorseSummary(tempString):

    tempString, HorseNumber = ExtractInfo(tempString, '<td class="no">', '</td>')
    TextToSave =  ",Horse Number," + str(HorseNumber)

    tempString, HorseLast10 = ExtractInfo(tempString, '<td class="last">', '</td>')
    TextToSave = TextToSave + ",HorseLast 10," + str(HorseLast10)

    tempString, HorseName = ExtractInfo(tempString, 'target="_blank">', '</a>')
    TextToSave = TextToSave + ",Horse Name," + str(HorseName)

    tempString, HorseTrainer = ExtractInfo(tempString, 'target="_blank">', '</a>')
    TextToSave = TextToSave + ",Horse Trainer," + str(HorseTrainer)

    tempString, HorseJockey = ExtractInfo(tempString, "<span class='Hilite'>", '</span>')
    TextToSave = TextToSave + ",Horse Jockey," + str(HorseJockey)
    #print(TextToSave)
    return (TextToSave, tempString)


#def ExtractHorseIndividualStats(tempString):





def ExtractHorseNameFromArray(tempString):
   #Horse Name,
   
   tempString, HorseName = ExtractInfo(tempString, "Horse Name,", ',')
   return HorseName








def SaveFile(HorseStrings):

   FullStr = ""

   for x in range(len(HorseStrings)):
      FullStr = FullStr + HorseStrings[x] + "\n"


   SaveFile = open('data.csv', 'w')
   SaveFile.write(FullStr)
   SaveFile.close()
