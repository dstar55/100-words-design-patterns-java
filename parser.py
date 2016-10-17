'''
Created on 5 Oct 2016

@author: dstar55@yahoo.com
'''
import constants
import re
import utils


# parses readme.md and creates array of dictionaries with key values pairs:
# patternName, PatternCategory, patternStory, patternUMLPath, patternSourceCodePath     
def parseReadme(readmeLocalPath):
        
    lines = tuple(open(readmeLocalPath, 'r'))
    
    isInPatternDescriptionSection = False
    isInStory = False    
    arrayList = []    
    currentPatternName = ""
    currentPatternID = ""
    currentStory = ""
    
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
            
            arrayList.append(dict)
        
        # find a description paragraph for each pattern
        #  ##### <a id="Singleton"></a>Singleton
        if "id=" in strLine:
            
            isInPatternDescriptionSection = True
            
            # strip text after between "" -> pattern id 
            currentPatternID = re.search(r'\"(.*)\"', strLine).group(1)
            
            # strip text after a> and remove last char -> pattern name
            #currentPatternName = strLine.partition('a>')[2][:-1]            
                        
        # tag '* Implementation' telling us that story paragraph is finished
        if "* Implementation" in strLine: 
            isInStory = False 
            
            
            # update dictionary with story            
            # TODO refactor               
            utils.updateDict(arrayList, currentPatternID, constants.DICT_KEY_PATTERN_STORY, currentStory)    
            #for dict in arrayList:
            #    if currentPatternID == dict.get(constants.DICT_KEY_PATTERN_ID):
            #        dict.update({constants.DICT_KEY_PATTERN_STORY : currentStory})
                
                
            # clean current text
            currentStory = ""
            

        # append story, since story can be described in more lines 
        if isInStory == True:
            currentStory = currentStory + strLine
                            
        # find a story paragraph inside pattern description paragraph                            
        if isInPatternDescriptionSection == True and "* Story" in strLine: 
            isInStory = True        
        
        # find a UML file name, data is in line which contains substring "alt text"                            
        if isInPatternDescriptionSection == True and "alt text" in strLine:
            
            # update dictionary with pattern UML file name
            # TODO refactor update
            utils.updateDict(arrayList, currentPatternID, constants.DICT_KEY_PATTERN_UML_FILE_NAME, currentPatternID.lower() + ".png")
            #for dict in arrayList:
            #    if currentPatternID == dict.get(constants.DICT_KEY_PATTERN_ID):
            #        dict.update({constants.DICT_KEY_PATTERN_UML_FILE_NAME : currentPatternID.lower() + ".png"})        
                   
                   
        # find source code, data is in paragraph which contains substring "Source Code"
        if isInPatternDescriptionSection == True and "Source Code" in strLine:

            # update dictionary with PATTERN_SOURCE_CODE_PACKAGE_NAME and DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME
            # TODO refactor update 
            utils.updateDict(arrayList, currentPatternID, constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME, constants.PATTERN_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower())
            utils.updateDict(arrayList, currentPatternID, constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME, constants.PATTERN_TEST_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower())
            
            #for dict in arrayList:
            #    if currentPatternID == dict.get(constants.DICT_KEY_PATTERN_ID):                    
            #        dict.update({constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME : constants.PATTERN_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower()})
            #        dict.update({constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME : constants.PATTERN_TEST_SOURCE_CODE_PACKAGE_PREFIX + currentPatternID.lower()})
                            
             
    return arrayList
