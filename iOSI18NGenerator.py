import csv

key = []
property = []
kr = []
en = []
jp = []
es = []
hans = []
hant = []

# kr_stringFile = open('./ko.lproj/Localizable.strings', 'w')
# en_stringFile = open('./en.lproj/Localizable.strings', 'w')
# es_stringFile = open('./es-419.lproj/Localizable.strings', 'w')
# jp_stringFile = open('./en.lproj/Localizable.strings', 'w')
# hant_stringFile = open('./en.lproj/Localizable.strings', 'w')
# hans_stringFile = open('./en.lproj/Localizable.strings', 'w')
# i18n_file = open('./I18N.swift', 'w')

### 마지막에 추가 하려면 a
### 갱신이면 +

kr_stringFile = open('./ko.strings', 'w')
en_stringFile = open('./en.strings', 'w')
es_stringFile = open('./es-419.strings', 'w')
jp_stringFile = open('./jp.strings', 'w')
hant_stringFile = open('./hant.strings', 'w')
hans_stringFile = open('./hans.strings', 'w')
i18n_file = open('./I18N.swift', 'w')

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
        krString = key[index] + " = " + "\"" + kr[index].replace("%s", "%@") + "\"" + ";\n"
        enString = key[index] + " = " + "\"" + en[index].replace("%s", "%@") + "\"" + ";\n"
        esString = key[index] + " = " + "\"" + es[index].replace("%s", "%@") + "\"" + ";\n"
        jpString = key[index] + " = " + "\"" + jp[index].replace("%s", "%@") + "\"" + ";\n"
        hansString = key[index] + " = " + "\"" + hans[index].replace("%s", "%@") + "\"" + ";\n"
        hantString = key[index] + " = " + "\"" + hant[index].replace("%s", "%@") + "\"" + ";\n"

        kr_stringFile.write(krString)
        en_stringFile.write(enString)
        es_stringFile.write(esString)
        jp_stringFile.write(jpString)
        hans_stringFile.write(hansString)
        hant_stringFile.write(hantString)

def get_content_I18N():
    for index in range(len(key)):
        I18NString = "static let " + key[index] + " = " + "\"" + key[index] + "\"" + ".localized\n"
        i18n_file.write(I18NString)

### I18NString
### I18N 완전체가 필요시
def get_total_I18N():
    i18n_file.write("struct I18N {\n")
    for index in range(len(key)):
        I18NString = "\t" + "static let " + key[index] + " = " + "\"" + key[index] + "\"" + ".localized\n"
        i18n_file.write(I18NString)
    i18n_file.write("}\n")


get_csv()
generate_string_Field()
get_total_I18N()
