'''
Created on 21 Feb 2017

@author: dstar55@yahoo.com

'''
import utils
import os


"""
 publish site
 
"""      
def publish():

    # copy content from draft directory to 
    for item in utils.orderedPatternFilesDict:
        copyCommand = "cp ./gh-pages/_drafts/" + item + ".md ./gh-pages/patterns/gof"
        print copyCommand
        os.system(copyCommand)