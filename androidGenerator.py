import csv
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump

key = []
property = []
kr = []
en = []
jp = []
es = []
hans = []
hant = []

with open('int.csv', encoding="utf-8", newline='\n') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        key.append(row[0])
        property.append(row[1])
        kr.append(row[2])
        en.append(row[3])
        jp.append(row[4])
        es.append(row[5])
        hans.append(row[6])
        hant.append(row[7])


root = Element('resource')

for index in range(len(key)):
    _string = "string name=" + "\"" + key[index] +"\""
    # xmlString = string
    SubElement(root,_string).text = kr[index]


def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

dump(root)

tree = ElementTree(root)
tree.write('test1.xml')