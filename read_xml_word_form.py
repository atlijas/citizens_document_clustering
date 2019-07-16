from xml.etree import ElementTree as ET
from collections import Counter
import glob

"""
This script assumes the xml format is the same as in Risamáldeild,
(A Very Large Icelandic Text Corpus), http://malfong.is/?pg=rmh,
known as tei: http://www.tei-c.org/ns/1.0
"""



xml_files = glob.glob('path/to/files/with/xml/files/**/*.xml')
# It might prove useful to add recursive=True, if the files are
# in subdirectories

def get_xml():
    xml = []
    for file in xml_files:
        with open(file, 'r', encoding = 'utf-8') as content:
            tree = ET.parse(content)
            root = tree.getroot()
            for element in tree.iter():
                xml.append(element.text)
        yield xml


xml = [w for w in get_xml()]


def write_to_file(lst, ending, separator):
    for (i, l) in enumerate(lst):
        with open(xml_files[i][:-3]+ending, 'w', encoding = 'utf-8') as file:
            if lst == xml:
                file.write(separator.join(set(l)))


if __name__ == '__main__':
    write_to_file(xml, 'txt', ' ')
