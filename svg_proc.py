import sys
from os import path, walk
from xmlparssing import *

def showHelp():
    print "DESC: svg_proc.py is a script for help to replace the node's id"
    print "      or it's references"
    print "USAGE: svg_proc.py [filePath]"
    print "       - filePath can be path of a file or forder"
    print "       - 'svg_proc.py -h' get help"

def FileOrForderExist(filePath):
    if path.isdir(filePath):
        return 1
    elif path.isfile(filePath):
        return 2
    else:
        return 0

def getfileName(filePath):
    fileDir, fileName_Ex = path.split(filePath)
    fileName, ex = path.splitext(fileDir)
    return fileName

def node_proc(elemet, filename):
    for child in element:
        if 'id' in child.keys():
            child.set('id', filename + child.attrib['id'])
            



def node_Traverse(filePath):
    filename = getfileName(filePath)
    tree = read_xml(filePath)
    root = tree.getroot()
    

def FileProcess(filePath):
   pass 
    
    

def ForderProcess(filePath):
    for root, dirs, files in os.walk(filePath, topdown=False):
        for _file in files:
            FileProcess(_file)
            

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Needs a parameter to specify the file or folder to process\nuse 'svg_proc.py -h' for help"

    else:
        if sys.argv[1].lower() == '-h':
           showHelp() 
        elif FileOrForderExist(sys.argv[1]) == 0:
            print "Needs a parameter to specify the file or folder to process\nuse 'svg_proc -h' for help"
        elif FileOrForderExist(sys.argv[1]) == 1:
            FileProcess(sys.argv[1])
        else:
            ForderProcess(sys.argv[1])
