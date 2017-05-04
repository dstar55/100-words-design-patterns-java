'''
Created on 13 Apr 2017

@author: dstar55@yahoo.com
'''
import constants

# decorates a content for the gh-pages branch
def decorateGHPagesContent(dictsArray):

    # loop over elements of the dictionary array    
    for dict in dictsArray:
        if dict.get(constants.DICT_KEY_PATTERN_IMAGE) != None:
            decorateGHPagesImageSection(dict)
        
    return dictsArray

# replaces image path according to need for gh-pages branch
def decorateGHPagesImageSection(dict):
    imageContent = dict.get(constants.DICT_KEY_PATTERN_IMAGE)                   
    aImageContent = imageContent.replace("https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/", "/assets/img/image/")           
    dict.update({constants.DICT_KEY_PATTERN_IMAGE: aImageContent})
