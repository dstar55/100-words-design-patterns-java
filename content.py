'''
Created on 5 Oct 2016

@author: dstar55@yahoo.com
'''
import glob
import os
import constants
import utils
from fileinput import filename


# creates content for the gh-pages branch
# for every element(dictionary which contains pattern details) in list markdown file is created with appropriate structure under the /gh-pages/_drafts/ folder(branch:gh-pages) 
def createGHPagesContent(dictsArray):
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

# creates slides for https://gitpitch.com/dstar55/100-words-design-patterns-java
# for every element(dictionary which contains pattern details) in list markdown file is created with appropriate structure under the /course folder(branch:master) 
def createSlidesContent(dictsArray):
    #print dictsArray
    
    print "Generating slides content ..."
    # create slide files for each pattern and put that file under MASTER_BRANCH/course
    filePath = constants.LOCAL_MASTER_REPOSITORY_PATH + '/' + constants.COURSE_FOLDER + '/'
    
    # check if folder exists otherwise make it
    if not os.path.exists(filePath):
        os.mkdir(filePath)
       
    # loop over elements of the list and create content file(jekyll page) for each element(pattern)    
    for dict in dictsArray:
        fileName = filePath + dict.get(constants.DICT_KEY_PATTERN_ID) + ".md"
        try:
            with open(fileName, 'w') as destFile:
                createSlide(destFile, dict)
                
        except IOError as e:
            print e    
    
    print "Generating slides content ... done"
        
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

# add page header
def createPageHeaderSection(destFile, dict):
    
    destFile.write('---\n')
    destFile.write('layout: page\n')
    destFile.write('title: ' + dict.get(constants.DICT_KEY_PATTERN_NAME) + '\n')
    destFile.write('permalink: /patterns/' + dict.get(constants.DICT_KEY_PATTERN_ID) + '/\n')
    destFile.write('tag: pattern\n')
    destFile.write('---\n\n')

#add page content links
def createPageTableOfContentSection(destFile):
    
    destFile.write('* [Story](#Story)\n')
    destFile.write('* [Image](#Image)\n')
    destFile.write('* [UML](#UML)\n')
    destFile.write('* [Implementation](#Implementation)\n')
    destFile.write('* [Usage](#Usage)\n')

# add page content -> story
def createPageStorySection(destFile, dict):
    
    destFile.write('\n\n')
    destFile.write('###  <a id="Story"></a>Story \n')
    destFile.write(dict.get(constants.DICT_KEY_PATTERN_STORY) + '\n')
    destFile.write('\n')

# add page content -> image
def createPageImageSection(destFile, dict):
    
    if dict.get(constants.DICT_KEY_PATTERN_IMAGE) != None:
        destFile.write('\n\n')
        destFile.write('###  <a id="Image"></a>Image \n')
        destFile.write(dict.get(constants.DICT_KEY_PATTERN_IMAGE) + '\n')
        destFile.write('\n')

# add page UML image
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

# add page standard UML
def createStandardPageUMLImageSection(destFile, dict):

    imagePath = '/assets/img/uml/' + dict.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME)
 
    destFile.write('[![](' + imagePath + ')](' + imagePath + ')\n')            
    destFile.write('\n')
        
# add page adapter UML -> special case
def createAdapterPageUMLImageSection(destFile, title, imagePath):
    
    destFile.write('#### ' + title + '\n')
    destFile.write('[![](' + imagePath + ')](' + imagePath + ')\n')            
    destFile.write('\n')
    
# add page implementation details, source code
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

# create page standard implementation content  
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
     
# create page implementation content
def createPageImplementationSectionContent(destFile, sortedList):
    for item in sortedList:
                
        # item[1] is file name
        destFile.write('#### *' + item[1] + '* \n')
        destFile.write('```java \n')
        # copy code snippet, item[2] is absoluteFilePath
        for line in tuple(open(item[2], 'r')):
            destFile.write(line)
        
        destFile.write('```\n\n')
                
#add page usage
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

    

# create a content for one slidee(pattern)
def createSlide(destFile, dict):
    
    print "Generating slide for ... " + str(destFile.name)
    
    destFile.write(createSlideHeaderSection(dict))    
    #createPageTableOfContentSection(destFile)
    #createPageStorySection(destFile, dict)
    #createPageImageSection(destFile, dict)
    #createPageUMLImageSection(destFile, dict)
    #createPageImplementationSection(destFile, dict)        
    #createPageUsageSection(destFile, dict)

# add page header
def createSlideHeaderSection(dict):
    
    header = "# " + dict.get(constants.DICT_KEY_PATTERN_ID) 
    header = header + "\n\n"
    header = header + "---"
    header = header + "\n\n"
    return header

    #destFile.write('---\n')
    #destFile.write('layout: page\n')
    #destFile.write('title: ' + dict.get(constants.DICT_KEY_PATTERN_NAME) + '\n')
    #destFile.write('permalink: /patterns/' + dict.get(constants.DICT_KEY_PATTERN_ID) + '/\n')
    #destFile.write('tag: pattern\n')
    #destFile.write('---\n\n')
