'''
Created on 13 Apr 2017

@author: dstar55@yahoo.com
'''
import constants

def decorate(dictsArray):

    # loop over elements of the dictionary array    
    for dict in dictsArray:
        if dict.get(constants.DICT_KEY_PATTERN_IMAGE) != None:
            decorateImageSection(dict)
        
    return dictsArray

# replaces image path
def decorateImageSection(dict):
    imageContent = dict.get(constants.DICT_KEY_PATTERN_IMAGE)                   
    aImageContent = imageContent.replace("https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/", "/assets/img/image/")           
    dict.update({constants.DICT_KEY_PATTERN_IMAGE: aImageContent})
