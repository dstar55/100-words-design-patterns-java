'''
Created on 12 Apr 2017

@author: dstar55@yahoo.com
'''

import unittest
import parser
import constants

class TestParser(unittest.TestCase):
    
    def setup(self):
        pass

    def test_parseReadme(self):
        
        # parse method returns arrayList which is 
        arrayList = parser.parseReadme('./TestReadme.md')
        
        for element in arrayList:
            print element.get(constants.DICT_KEY_PATTERN_IMAGE)
            
        # check the number of elements in arrayList        
        self.assertEqual(23, len(arrayList))
        
        # first member of the array is singleton dictionary
        singletonContent = arrayList[0] 
        
        # check Singleton
        self.assertEqual("Singleton", singletonContent.get(constants.DICT_KEY_PATTERN_ID))        
        self.assertEqual("Singleton", singletonContent.get(constants.DICT_KEY_PATTERN_NAME))                
        self.assertEqual(True, ("Singleton ensures that only one(single) object can be created from the class." in singletonContent.get(constants.DICT_KEY_PATTERN_STORY)))
        self.assertEqual(True, ("Brick Lane Graffiti Usain Bolt" in singletonContent.get(constants.DICT_KEY_PATTERN_IMAGE)))
        self.assertEqual("singleton.png", singletonContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))        
        self.assertEqual("/src/main/java/com/hundredwordsgof/singleton", singletonContent.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME))
        self.assertEqual("/src/test/java/com/hundredwordsgof/singleton", singletonContent.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME))

        # template method: image is not defined
        templateMethodContent = arrayList[21]

        # check TemplateMethod
        self.assertEqual("TemplateMethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_ID))        
        self.assertEqual("Template Method", templateMethodContent.get(constants.DICT_KEY_PATTERN_NAME))
        self.assertEqual("templatemethod.png", templateMethodContent.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))            
        self.assertEqual(True, ("Defines a skeleton of an algorithm in an operation." in templateMethodContent.get(constants.DICT_KEY_PATTERN_STORY)))
        #image content is not define, dict.get(...) for key which does not exists returns None
        self.assertEqual(True, (templateMethodContent.get(constants.DICT_KEY_PATTERN_IMAGE) == None))        
        self.assertEqual("/src/main/java/com/hundredwordsgof/templatemethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME))
        self.assertEqual("/src/test/java/com/hundredwordsgof/templatemethod", templateMethodContent.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME))
        
        
if __name__ == '__main__':
    unittest.main()         