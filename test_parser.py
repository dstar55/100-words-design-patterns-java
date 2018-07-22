'''
Created on 12 Apr 2017

@author: dstar55@yahoo.com
'''

import unittest
import parser
import constants

class TestParser(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_parseReadme(self):
        
        # parse method returns dictsArray which is 
        dictsArray = parser.parseReadme('./TestReadme.md')
                    
        # check the number of elements in dictsArray        
        self.assertEqual(23, len(dictsArray))
        
        # first member of the array is singleton dictionary
        singletonContent = dictsArray[0] 
        
        # check Singleton
        self.assertEqual("Singleton", singletonContent.get(constants.DICT_KEY_PATTERN_ID))        
        self.assertEqual("Singleton", singletonContent.get(constants.DICT_KEY_PATTERN_NAME))                
        self.assertEqual(True, ("100 meters world record holder is a singleton." in singletonContent.get(constants.DICT_KEY_PATTERN_STORY)))
        self.assertEqual(True, ("Brick Lane Graffiti Usain Bolt" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        self.assertEqual(True, ("Objects reside inside heap memory, " in singletonContent.get(constants.DICT_KEY_PATTERN_MOTIVATION)))
        self.assertEqual("singleton.png", singletonContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))        
        self.assertEqual("/src/main/java/com/hundredwordsgof/singleton", singletonContent.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME))
        self.assertEqual("/src/test/java/com/hundredwordsgof/singleton", singletonContent.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME))
        
        # template method: image is not defined
        templateMethodContent = dictsArray[21]

        # check TemplateMethod
        self.assertEqual("TemplateMethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_ID))        
        self.assertEqual("Template Method", templateMethodContent.get(constants.DICT_KEY_PATTERN_NAME))
        self.assertEqual("templatemethod.png", templateMethodContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))            
        self.assertEqual(True, ("Daily routine is example of the Template Method." in templateMethodContent.get(constants.DICT_KEY_PATTERN_STORY)))
        self.assertEqual(True, ("We decide to use JDBC" in templateMethodContent.get(constants.DICT_KEY_PATTERN_MOTIVATION)))
        #image content is not define, dict.get(...) for key which does not exists returns None
        self.assertEqual(True, (templateMethodContent.get(constants.DICT_KEY_PATTERN_IMAGE) == None))        
        self.assertEqual("/src/main/java/com/hundredwordsgof/templatemethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME))
        self.assertEqual("/src/test/java/com/hundredwordsgof/templatemethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME))
               
        
if __name__ == '__main__':
    unittest.main()         