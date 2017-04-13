'''
Created on 14 Apr 2017

@author: dstar55@yahoo.com
'''

import unittest
import parser
import constants

class TestParser(unittest.TestCase):
    
    def setup(self):
        pass

    def test_parseReadmet(self):
        
        # parse method returns arrayList which is 
        arrayList = parser.parseReadme('./TestReadme.md')
        
        # check the number of elements in arrayList        
        self.assertEqual(23, len(arrayList))
        
        # first member of the array is singleton dictionary
        singleton = arrayList[0] 
        
        # check Singleton
        self.assertEqual("Singleton", singleton.get(constants.DICT_KEY_PATTERN_ID))        
        self.assertEqual("Singleton", singleton.get(constants.DICT_KEY_PATTERN_NAME))
        self.assertEqual("singleton.png", singleton.get(constants.DICT_KEY_PATTERN_UML_FILE_NAME))        
        self.assertEqual(True, ("Singleton ensures that only one(single) object can be created from the class." in singleton.get(constants.DICT_KEY_PATTERN_STORY)))
        self.assertEqual(True, ("Brick Lane Graffiti Usain Bolt" in singleton.get(constants.DICT_KEY_PATTERN_IMAGE)))        
        self.assertEqual("/src/main/java/com/hundredwordsgof/singleton", singleton.get(constants.DICT_KEY_PATTERN_SOURCE_CODE_PACKAGE_NAME))
        self.assertEqual("/src/test/java/com/hundredwordsgof/singleton", singleton.get(constants.DICT_KEY_PATTERN_TEST_SOURCE_CODE_PACKAGE_NAME))
        
        
        
if __name__ == '__main__':
    unittest.main()         