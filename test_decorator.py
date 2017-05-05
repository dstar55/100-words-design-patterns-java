'''
Created on 13 Apr 2017

@author: dstar55@yahoo.com
'''

import unittest
import decorator
import parser
import constants

class TestDecorator(unittest.TestCase):
    
    def setUp(self):
        # first lets parse TestRadme.md file
        self.dictsArray = parser.parseReadme('./TestReadme.md')

    def test_decorate(self):
                
        # check the number of elements in dictsArray        
        self.assertEqual(23, len(self.dictsArray))

        # first member of the array is singleton dictionary
        singletonContent = self.dictsArray[0] 

        # check Singleton image section
        self.assertEqual(True, ("https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/singleton.jpg" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        
        #TODO more asserts        

    def test_decorateGHPagesContent(self):
        
        # lets decorate prepare for the gh-pages content
        dictsArray = decorator.decorateGHPagesContent(self.dictsArray)
                    
        # number of elements in dictsArray should remain the same        
        self.assertEqual(23, len(dictsArray))
        
        # first member of the array is singleton dictionary
        singletonContent = dictsArray[0] 
        
        # check Singleton image section
        self.assertEqual(True, ("/assets/img/image/singleton.jpg" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        self.assertEqual(True, ("http://www.design-patterns-stories.com/assets/img/image/singleton.jpg" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        
        self.assertEqual("http://www.design-patterns-stories.com/assets/img/uml/singleton.png", singletonContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))

        #template method
        templateMethodContent = dictsArray[21]
        
        self.assertEqual("TemplateMethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_ID))
        self.assertEqual("http://www.design-patterns-stories.com/assets/img/uml/templatemethod.png", templateMethodContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))
        
        #TODO more asserts
        
        
if __name__ == '__main__':
    unittest.main()         
    
