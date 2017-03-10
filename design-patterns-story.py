'''
Created on 02 Sep 2016

Generates content for design-patterns-story site  

@author: dstar55@yahoo.com

'''

import constants
import clone  
import parser
import content
import deletedir
import publish
import shutil 
import os
import argparse

# script for publishing design-pattern-stories.com site. User can clone a repo, generate a content, publish a content and clean data
# be aware that script expect that user follows proper orders in action: 1. clone, 2. generate, 3. publish, 4. delete
def main():
    parser = argparse.ArgumentParser(description="This is a script for publishing content for www.design-pattern-stories.com site." \
                                     "User can clone necessary repositories, generate site content, publish content to the live site and clean all generated data.@" \
                                     "It is expected that user follows proper orders in action: 1. clone, 2. generate, 3. publish, 4. delete")
    parser.add_argument("-c","--clone", action='store_true', help="clone necessary github repositories")
    parser.add_argument("-g", "--generate", action='store_true', help="generate content for site: www.design-pattern-stories.com")
    parser.add_argument("-p", "--publish", action='store_true', help="publish content to the live site: www.design-pattern-stories.com")
    parser.add_argument("-d", "--delete", action='store_true', help="clean all generated data")
    
    args = parser.parse_args()
    if args.clone:
        main_clone()
    elif args.generate:
        main_generate()    
    elif args.publish:
        main_publish()
    elif args.delete:
        main_delete()
    else:
        parser.print_help() 

# clone repos
def main_clone():
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.MASTER_BRANCH, constants.LOCAL_MASTER_REPOSITORY_PATH)
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.GH_PAGES_BRANCH, constants.LOCAL_GH_PAGES_REPOSITORY_PATH)
    clone.cloneRepo(constants.REMOTE_REPOSITORY_PATH, constants.GH_PAGES_RESOURCES_BRANCH, constants.LOCAL_GH_PAGES_RESOURCES_REPOSITORY_PATH)
    
# parse readme.md from master and create a content    
def main_generate():
    content.createContent(parser.parseReadme(constants.LOCAL_MASTER_REPOSITORY_PATH + constants.SLASH + constants.README_FILE_NAME))
    
def main_publish():
    publish.publish()
    
def main_delete():
    deletedir.removeDirs()
    
if __name__ == '__main__':
    main()
