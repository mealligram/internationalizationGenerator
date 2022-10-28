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


kr_stringFile = open('./ko_strings.xml', 'w')
en_stringFile = open('./en_strings.xml', 'w')
es_stringFile = open('./es-419_strings.xml', 'w')
jp_stringFile = open('./jp_strings.xml', 'w')
hant_stringFile = open('./hant_strings.xml', 'w')
hans_stringFile = open('./hans_strings.xml', 'w')

def get_csv():
    with open('int.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            key.append(row[0])
            property.append(row[1])
            kr.append(row[2])
            en.append(row[3])
            jp.append(row[4])
            es.append(row[5])
            hans.append(row[6])
            hant.append(row[7])

def generate_string_Field():
    for index in range(len(key)):
        krString = "<string name=\"" + key[index] + "\">" + kr[index] + "</string>" + "\n"
        enString = "<string name=\"" + key[index] + "\">" + en[index] + "</string>" + "\n"
        esString = "<string name=\"" + key[index] + "\">" + es[index] + "</string>" + "\n"
        jpString = "<string name=\"" + key[index] + "\">" + jp[index] + "</string>" + "\n"
        hansString = "<string name=\"" + key[index] + "\">" + hans[index] + "</string>" + "\n"
        hantString = "<string name=\"" + key[index] + "\">" + hant[index] + "</string>" + "\n"

        kr_stringFile.write(krString)
        en_stringFile.write(enString)
        es_stringFile.write(esString)
        jp_stringFile.write(jpString)
        hans_stringFile.write(hansString)
        hant_stringFile.write(hantString)

get_csv()
generate_string_Field()