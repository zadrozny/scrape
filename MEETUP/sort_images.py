# Sorts pictures in IMAGES directory into a subdirectory -- MEN, WOMEN, or UNKNOWN -- 
# using filenames containing first and last names.
# These are checked against first names listed in the NLTK corpus.

from nltk.corpus import names
import os
import shutil

male_names   = [name for name in names.words('male.txt')]

female_names = [name.lower() for name in names.words('female.txt')]

for f in os.listdir('/IMAGES'):
	if f.split()[0].strip().lower() in male_names:
		shutil.move('/IMAGES/' + f, '/MEN')
	elif f.split('_')[0].strip().lower() in female_names:
		shutil.move('/IMAGES/' + f, '/IMAGES/WOMEN')
	else:
		shutil.move('/IMAGES/' + f, '/IMAGES/UNKNOWN')