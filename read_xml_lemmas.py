from xml.etree import ElementTree as ET
from collections import Counter
from string import punctuation
import regex as re
import glob

"""
This script assumes the xml format is the same as in Risamáldeild,
(A Very Large Icelandic Text Corpus): http://malfong.is/?pg=rmh
It is known as tei: http://www.tei-c.org/ns/1.0
"""



xml_files = glob.glob('path/to/files/with/wml/files/**/*.xml')
# It might prove useful to add recursive=True, if the files are
# in subdirectories

# Reads multi-digit numbers in file names as a single number
# Also known as human sorting
# Necessary here to keep consistency between .txt and .lmms files
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)


xml_files = natural_sort(xml_files)


# Returns lemmas from xml files
def get_xml():
    for file in xml_files:
        xml = []
        with open(file, 'r', encoding = 'utf-8') as content:
            tree = ET.parse(content)
            root = tree.getroot()
            for element in tree.iter():
                if element.attrib.get('lemma') != None:
                    xml.append(element.attrib.get('lemma'))
                if element.text in punctuation:
                    xml.append(element.text)
        yield xml


xml = [w for w in get_xml()]


# Takes in a list, file ending and means of separating lemmas
def write_to_file(lst, ending, separator):
    for (i, l) in enumerate(lst):
        with open(xml_files[i][:-3]+ending, 'w', encoding = 'utf-8') as file:
            if lst == xml:
                file.write(separator.join(set(l)))


if __name__ == '__main__':
    write_to_file(xml, 'lmms', ' ')
