'''
Created on 19 Feb 2017

@author: dstar55@yahoo.com

'''

import constants
import os


"""
 remove directories
 
"""   
def removeDirs():
    print "deleting ..."
    removeDir(constants.LOCAL_MASTER_REPOSITORY_PATH)
    removeDir(constants.LOCAL_GH_PAGES_REPOSITORY_PATH)
    removeDir(constants.LOCAL_GH_PAGES_RESOURCES_REPOSITORY_PATH)
    print  "deleting ... done"
    
def removeDir(sourcePath):

    # check does source path exists    
    if os.path.exists(sourcePath):
        removeDirCommand = "rm -rf " + sourcePath
        print removeDirCommand
        os.system(removeDirCommand)
    else:
        print "directory " + sourcePath + " does not exists"   
