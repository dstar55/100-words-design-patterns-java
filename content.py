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
def createContent(dictsArray):
    #print dictsArray
    
    print "Generating content ..."
    # create page files for each pattern and put that file under LOCAL_GH_PAGES_REPOSITORY_PATH/_drafts
    filePath = constants.LOCAL_GH_PAGES_REPOSITORY_PATH + '/' + constants.DRAFTS_FOLDER + '/'
    
    # check if folder exists otherwise make it
    if not os.path.exists(filePath):
        os.mkdir(filePath)
       
    # loop over elements of the list and create content file(jekyll page) for each element(pattern)    
    for dict in dictsArray:
        fileName = filePath + dict.get(constants.DICT_KEY_PATTERN_ID) + ".md"
        try:
            with open(fileName, 'w') as destFile:
                createPage(destFile, dict)
                
        except IOError as e:
            print e    
    
    print "Generating content ... done"
        
# create a content for one page(pattern)
def createPage(destFile, dict):
    
    print "Generating page ... " + str(destFile.name)
    #TODO refactor function should return string and than write into destFile(destFile should not be argument for belowed functions)
    createPageHeaderSection(destFile, dict)    
    createPageTableOfContentSection(destFile)
    createPageStorySection(destFile, dict)
    createPageImageSection(destFile, dict)
    createPageUMLImageSection(destFile, dict)
    createPageImplementationSection(destFile, dict)        
    createPageUsageSection(destFile, dict)

# add header
def createPageHeaderSection(destFile, dict):
    
    destFile.write('---\n')
    destFile.write('layout: page\n')
    destFile.write('title: ' + dict.get(constants.DICT_KEY_PATTERN_NAME) + '\n')
    destFile.write('permalink: /patterns/' + dict.get(constants.DICT_KEY_PATTERN_ID) + '/\n')
    destFile.write('tag: pattern\n')
    destFile.write('---\n\n')

#add content links
def createPageTableOfContentSection(destFile):
    
    destFile.write('* [Story](#Story)\n')
    destFile.write('* [Image](#Image)\n')
    destFile.write('* [UML](#UML)\n')
    destFile.write('* [Implementation](#Implementation)\n')
    destFile.write('* [Usage](#Usage)\n')

# add content -> story
def createPageStorySection(destFile, dict):
    
    destFile.write('\n\n')
    destFile.write('###  <a id="Story"></a>Story \n')
    destFile.write(dict.get(constants.DICT_KEY_PATTERN_STORY) + '\n')
    destFile.write('\n')

# add content -> image
def createPageImageSection(destFile, dict):
    
    if dict.get(constants.DICT_KEY_PATTERN_IMAGE) != None:
        destFile.write('\n\n')
        destFile.write('###  <a id="Image"></a>Image \n')
        destFile.write(dict.get(constants.DICT_KEY_PATTERN_IMAGE) + '\n')
        destFile.write('\n')

# add UML image
def createPageUMLImageSection(destFile, dict):
    
    destFile.write('###  <a id="UML"></a>UML\n')
    
    #adapter is special case, while we have two implementations for one pattern, object adapter and class adapter
    if dict.get(constants.DICT_KEY_PATTERN_ID) == 'Adapter':            
        # class adapter             
        createAdapterPageUMLImageSection(destFile, 'Class Adapter', '/assets/img/uml/class' + dict.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME)) 
        
        # object adapter
        createAdapterPageUMLImageSection(destFile, 'Object Adapter', '/assets/img/uml/object' + dict.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))
    else:
        createStandardPageUMLImageSection(destFile, dict)

def createStandardPageUMLImageSection(destFile, dict):

    imagePath = '/assets/img/uml/' + dict.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME)
 
    destFile.write('[![](' + imagePath + ')](' + imagePath + ')\n')            
    destFile.write('\n')
        
# add adapter UML -> special case
def createAdapterPageUMLImageSection(destFile, title, imagePath):
    
    destFile.write('#### ' + title + '\n')
    destFile.write('[![](' + imagePath + ')](' + imagePath + ')\n')            
    destFile.write('\n')
    
# add implementation details, source code
def createPageImplementationSection(destFile, dict):
    
    destFile.write('###  <a id="Implementation"></a>Implementation \n\n')
    
    #adapter is special case, while we have two implementations for one pattern, object adapter and class adapter
    if dict.get(constants.DICT_KEY_PATTERN_ID) == 'Adapter':
        
        destFile.write('#### Class Adapter\n')
        sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME) + '/clazz/*.java'
        createStandardPageImplementationSection(destFile, dict, sourcePath)

        destFile.write('#### Object Adapter\n')
        sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME) + '/object/*.java'
        createStandardPageImplementationSection(destFile, dict, sourcePath)

    else:
        sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME) + '/*.java'
        createStandardPageImplementationSection(destFile, dict, sourcePath)

# create standard implementation content  
def createStandardPageImplementationSection(destFile, dict, sourcePath):
               
    # declares an empty list 
    lst = [] 
    
    # grab a fileNames
    for absoluteFileName in glob.glob(sourcePath):
                
        fileName = absoluteFileName[(absoluteFileName.rfind('/') + 1):]
        # append to list tuple [position of the file, file name, absolute file path]
        lst.append([utils.getFilePosition(dict.get(constants.DICT_KEY_PATTERN_ID), fileName), fileName, absoluteFileName])
    
    # sort a list according to file position 
    sortedList = utils.sort(lst)
    
    # create content
    createPageImplementationSectionContent(destFile, sortedList)
     
# create implementation content
def createPageImplementationSectionContent(destFile, sortedList):
    for item in sortedList:
                
        # item[1] is file name
        destFile.write('#### *' + item[1] + '* \n')
        destFile.write('```java \n')
        # copy code snippet, item[2] is absoluteFilePath
        for line in tuple(open(item[2], 'r')):
            destFile.write(line)
        
        destFile.write('```\n\n')
                
#add usage
def createPageUsageSection(destFile, dict):
    
    destFile.write('###  <a id="Usage"></a>Usage \n\n')
    sourcePath = constants.LOCAL_MASTER_REPOSITORY_PATH + dict.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME) + '/*.java'
        
    for fileName in glob.glob(sourcePath):        
                    
        destFile.write('#### *' + fileName[(fileName.rfind('/') + 1):] + '* \n')
        destFile.write('```java \n')
        
        # copy code snippet
        for line in tuple(open(fileName, 'r')):
            destFile.write(line)
        
        destFile.write('```\n\n')

    

