'''
Created on 13 Apr 2017

@author: dstar55@yahoo.com
'''

import unittest
import decorator
import parser
import constants

class TestDecorator(unittest.TestCase):
    
    def setup(self):
        pass

    def test_decorate(self):
        
        # first lets parse TestRadme.md file
        dictsArray = parser.parseReadme('./TestReadme.md')
         
        #test content of the image section
        # check the number of elements in dictsArray        
        self.assertEqual(23, len(dictsArray))

        # first member of the array is singleton dictionary
        singletonContent = dictsArray[0] 

        # check Singleton image section
        self.assertEqual(True, ("https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/singleton.jpg" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
                
        # lets decorate  
        dictsArray = decorator.decorate(dictsArray)
                    
        # number of elements in dictsArray should remain the same        
        self.assertEqual(23, len(dictsArray))
        
        # first member of the array is singleton dictionary
        singletonContent = dictsArray[0] 
        
        # check Singleton image section
        self.assertEqual(True, ("/assets/img/image/singleton.jpg" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        
        
if __name__ == '__main__':
    unittest.main()         
    
