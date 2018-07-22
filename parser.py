'''
Created on 5 Oct 2016

@author: dstar55@yahoo.com
'''
import constants
import re
import utils


# parses readme.md and creates array of dictionaries with key values pairs:
# patternName, patternCategory, patternStory, patternUMLPath, patternSourceCodePath, ...     
def parseReadme(readmeLocalPath):
        
    lines = tuple(open(readmeLocalPath, 'r'))
    
    isInPatternDescriptionSection = False
    isInStory = False    
    isInMotivation = False
    dictsArray = []        
    currentPatternID = ""
    currentStory = ""
    currentMotivation = ""
    
    for line in lines:
        strLine = str(line)
        
        # find name of the pattern e.g.
        # * [Singleton](#Singleton)
        if strLine.startswith('* ['):
            dict = {}
                                                                                        
            # extracts substring between [] -> pattern name + updates dictionary
            dict.update({constants.DICT_KEY_PATTERN_NAME: utils.extractSubStringBetween(strLine, '\[', '\]')})
            
            # extracts substring between #) -> pattern id + updates dictionary
            dict.update({constants.DICT_KEY_PATTERN_ID: utils.extractSubStringBetween(strLine, '\#', '\)')})            
            
            dictsArray.append(dict)
        
        # find a description paragraph for each pattern
        # ##### <a id="Singleton"></a>Singleton
        if "id=" in strLine:
            
            isInPatternDescriptionSection = True
            
            # strip text after between "" -> pattern id 
            currentPatternID = re.search(r'\"(.*)\"', strLine).group(1)
                                    
        # tag '* Implementation' telling us that story paragraph is finished
        if "* Implementation" in strLine: 
            isInStory = False 
                        
            #  split the story text into two chunks, first is story part and second is image part if exists
            if "* Image" in currentStory:
                currentStorySplited = currentStory.split("* Image")
                utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_STORY, currentStorySplited[0])
                utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_IMAGE, currentStorySplited[1])
            else:               
                # update dictionary with story                                    
                utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_STORY, currentStory)                    
                
            # clean current text
            currentStory = ""

        # append motivation, since motivation is described in more lines 
        if isInMotivation == True:
            if "* Story" in strLine:
                # end of the Motivation section
                isInMotivation = False  
                
                #update dictionary with motivation
                utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_MOTIVATION, currentMotivation)
                
                # clean the motivation text
                currentMotivation = ""
            else:    
                currentMotivation = currentMotivation + strLine
            #print(currentMotivation)
                            
        # find a story paragraph inside pattern description paragraph                            
        if isInPatternDescriptionSection == True and "* Motivation" in strLine: 
            isInMotivation = True        
            

        # append story, since story can be described in more lines 
        if isInStory == True:
            currentStory = currentStory + strLine
                            
        # find a story paragraph inside pattern description paragraph                            
        if isInPatternDescriptionSection == True and "* Story" in strLine: 
            isInStory = True      
            
            
        # find a UML file name, data is in line which contains substring "alt text"                            
        if isInPatternDescriptionSection == True and isInStory == False and "alt text" in strLine:
            
            # update dictionary with pattern UML file name
            utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_UML_FILE_NAME, currentPatternID.lower() + ".png")
                   
                   
        # find source code, data is in paragraph which contains substring "Source Code"
        if isInPatternDescriptionSection == True and isInStory == False and "Source Code" in strLine:

            # update dictionary with PATTERN_SOURCE_CODE_PACKAGE_NAME and DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME 
            utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME, constants.PATTERN_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower())
            utils.updateDict(dictsArray, currentPatternID, constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME, constants.PATTERN_TEST_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower())
                                        
             
    return dictsArray
