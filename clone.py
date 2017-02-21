'''
Created on 5 Oct 2016

@author: dstar55@yahoo.com

'''

import os

"""
 clone git repository
 
"""   
def cloneRepo(sourcePath, branch, destinationPath):

    # check does destination path exists    
    if os.path.exists(destinationPath):
        removeDirCommand = "rm -rf " + destinationPath
        print removeDirCommand
        os.system(removeDirCommand)
        
    # clone repo 
    gitClonecommand = "git clone -b " + branch + " " + sourcePath + " " + destinationPath
    print gitClonecommand    
    os.system(gitClonecommand)
