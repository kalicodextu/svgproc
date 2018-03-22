import sys
import re
from os import path, walk
from xmlparssing import *

REGEX = re.compile(r'#[\w, -]*')
IDRECORD = set()

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
    fileName, ex = path.splitext(fileName_Ex)
    return fileName

def node_proc(element, filename):
    if len(element.getchildren())>0:
        for child in element:
            if 'id' in child.keys():
                IDRECORD.add(child.attrib['id'])
                print child.attrib['id']
                child.set('id', filename + child.attrib['id'])
                print filename + child.attrib['id']
            for key in child.keys():
                value=child.attrib[key]
                id_ref_list = REGEX.findall(value)
                for id_ref in id_ref_list:
                    _id = id_ref[1:]
                    if _id in IDRECORD:
                        value = value.replace(_id, filename+_id, 1)
                        print id_ref
                child.set(key, value)
            node_proc(child, filename)
    else:
        return

def FileProcess(filePath):
    IDRECORD.clear()
    print 'file: ' + filePath
    filename = getfileName(filePath)
    tree = read_xml(filePath)
    root = tree.getroot()
    for child in root:
        node_proc(child, filename)
    write_xml(tree, './' + filename + '_out.svg')
    print IDRECORD, len(IDRECORD)
    

def ForderProcess(filePath):
    print 'forder: ' + filePath
    for root, dirs, files in walk(filePath, topdown=False):
        for _file in files:
            FileProcess(path.join(root,_file))
            

if __name__ == '__main__':
    print sys.argv[1]
    if len(sys.argv) < 2:
        print "Needs a parameter to specify the file or folder to process\nuse 'svg_proc.py -h' for help"

    else:
        if sys.argv[1].lower() == '-h':
           showHelp() 
        elif FileOrForderExist(sys.argv[1]) == 0:
            print "Needs a parameter to specify the file or folder to process\nuse 'svg_proc -h' for help"
        elif FileOrForderExist(sys.argv[1]) == 2:
            FileProcess(sys.argv[1])
        else:
            ForderProcess(sys.argv[1])
    print "...Done"
