'''
Created on 02 Sep 2016

Generates content for design-patterns-story site  

@author: DS

'''

import constants
import clone  
import parser
import content

def main():
           
    # clone repos
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.MASTER_BRANCH, constants.LOCAL_MASTER_REPOSITORY_PATH)
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.GH_PAGES_BRANCH, constants.LOCAL_GH_PAGES_REPOSITORY_PATH)
   
    # parse readme.md from master and create a content
    content.createContent(parser.parseReadme(constants.LOCAL_MASTER_REPOSITORY_PATH + constants.SLASH + constants.README_FILE_NAME))

           
if __name__ == '__main__':
    main()
