import re
import os
import shutil
from collections import Counter

BASE_FILE_NAME = 'COMPLEX_QUALIFYING_EXAM_ARCHIVE.tex'
NEW_FILE_NAME = 'complex_archive.tex'
texdoc = []  # a list of string representing the latex document in python
lines_to_add = []
tag_counter = Counter()


lines_to_add.append("\\tableofcontents\n\\newpage\n")
# read the .tex file, and modify the lines
with open(BASE_FILE_NAME) as fin:
    for line in fin:
        if line.startswith('\\item['):

        	# regex to match any item ID's
            regex = r'(?<=id=).\w+'
            list1 = re.findall(regex,line)
            for item in list1:
            	# If it's not the year of the test
                if not re.match(r"[a-zA-Z][0-9]+", item):
                    tag_counter[item] += 1
    fin.seek(0)
    texdoc = fin.readlines()

# Add the category list (e.g: Series)
for tag in tag_counter:
    lines_to_add.append("\\section{{{0}}}\n".format(tag.capitalize()))
    lines_to_add.append("\\begin{{itemize}}\\setlength\\itemsep{{4em}}\\onlyitems[none, include={0}]\n".format(tag))
    lines_to_add.append("\\mylist\n")
    lines_to_add.append("\\end{itemize}\n")
    lines_to_add.append("\\newpage\n\n")

# Add the text to our new tex document.
for i in range(len(texdoc)):
    if "section START" in texdoc[i]:
        texdoc[i+1:i+1] = lines_to_add

with open(NEW_FILE_NAME,'w') as file_to_write:
    contents = "".join(texdoc)
    file_to_write.write(contents)
    file_to_write.close()

# Compile latex.
os.system("pdflatex complex_archive.tex")