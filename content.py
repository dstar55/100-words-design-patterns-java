'''
Created on 5 Oct 2016

@author: dstar55@yahoo.com
'''
import glob
import os
import constants
import utils
from fileinput import filename


# creates content for every element(dictionary which contains pattern details) in list 
def createContent(arrayList):
    #print arrayList
    
    # create page files for each pattern and put that file under LOCAL_GH_PAGES_REPOSITORY_PATH/_drafts
    filePath = constants.LOCAL_GH_PAGES_REPOSITORY_PATH + '/' + constants.DRAFTS_FOLDER + '/'
    
    # check if folder exists otherwise make it
    if not os.path.exists(filePath):
        os.mkdir(filePath)
       
    # loop over elements of the list and create content file(jekyll page) for each element(pattern)    
    for dict in arrayList:
        fileName = filePath + dict.get(constants.DICT_KEY_PATTERN_ID) + ".md"
        try:
            with open(fileName, 'w') as aFile:
                createPage(aFile, dict)
                
        except IOError as e:
            print e    
    

# create a content for one page(pattern)
def createPage(aFile, dict):
    
    #TODO refactor function should return string and than write into aFile(aFile should not be argument for belowed functions)
    createPageHeaderSection(aFile, dict)    
    createPageTableOfContentSection(aFile)
    createPageStorySection(aFile, dict)
    createPageUMLImageSection(aFile, dict)
    createPageImplementationSection(aFile, dict)        
    createPageUsageSection(aFile, dict)

# add header
def createPageHeaderSection(aFile, dict):
    
    aFile.write('---\n')
    aFile.write('layout: page\n')
    aFile.write('title: ' + dict.get(constants.DICT_KEY_PATTERN_NAME) + '\n')
    aFile.write('permalink: /patterns/' + dict.get(constants.DICT_KEY_PATTERN_ID) + '/\n')
    aFile.write('tag: pattern\n')
    aFile.write('---\n\n')

#add content links
def createPageTableOfContentSection(aFile):
    
    aFile.write('* [Story](#Story)\n')
    aFile.write('* [UML](#UML)\n')
    aFile.write('* [Implementation](#Implementation)\n')
    aFile.write('* [Usage](#Usage)\n')

# add content -> story
def createPageStorySection(aFile, dict):
    
    aFile.write('\n\n')
    aFile.write('###  <a id="Story"></a>Story \n')
    aFile.write(dict.get(constants.DICT_KEY_PATTERN_STORY) + '\n')
    aFile.write('\n')

# add UML image
def createPageUMLImageSection(aFile, dict):
    
    imagePath = '{{site.baseurl}}/assets/img/' + dict.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME)
     
    aFile.write('###  <a id="UML"></a>UML \n')
    aFile.write('[![](' + imagePath + ')](' + imagePath + ')\n')            
    aFile.write('\n')

# add implementation details, source code
def createPageImplementationSection(aFile, dict):
    
    aFile.write('###  <a id="Implementation"></a>Implementation \n\n')
    sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME) + '/*.java'
       
    # declares an empty list 
    lst = [] 
    
    # grab a fileNames
    for absoluteFileName in glob.glob(sourcePath):
                
        fileName = absoluteFileName[(absoluteFileName.rfind('/') + 1):]
        # append to list tuple [postion of the file, file name, absolute file path]
        lst.append([utils.getFilePosition(dict.get(constants.DICT_KEY_PATTERN_ID), fileName), fileName, absoluteFileName])
        #lst.append([utils.getFilePosition(dict.get(constants.DICT_KEY_PATTERN_ID), fileName), fileName])
    
    # sort a list according to file position 
    sortedList = utils.sort(lst)
    
    # create content
    for item in sortedList:
                
        # item[1] is file name
        aFile.write('#### *' + item[1] + '* \n')
        aFile.write('```java \n')
        # copy code snippet, item[2] is absoluteFilePath
        for line in tuple(open(item[2], 'r')):
            aFile.write(line)
        
        aFile.write('```\n\n')
            
#add usage
def createPageUsageSection(aFile, dict):
    
    aFile.write('###  <a id="Usage"></a>Usage \n\n')
    sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME) + '/*.java'
        
    for fileName in glob.glob(sourcePath):        
                    
        aFile.write('#### *' + fileName[(fileName.rfind('/') + 1):] + '* \n')
        aFile.write('```java \n')
        
        # copy code snippet
        for line in tuple(open(fileName, 'r')):
            aFile.write(line)
        
        aFile.write('```\n\n')

    

