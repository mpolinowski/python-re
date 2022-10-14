import re
from pathlib import Path


# get archives from a specified month from path

root_dir = Path('files')
filenames = root_dir.iterdir()
file_list = list(filenames)
# print(file_list)
files = [file.name for file in file_list]
# print(files)

zip_pattern = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}_archive.zip')
date_pattern = re.compile('2022-09[^ ]+')

# filter all non-zip files
matching_container = [file for file in files if zip_pattern.findall(file)]
# get zip files of specific date
matching_date = [file for file in matching_container if date_pattern.findall(file)]

print(matching_date)
# => ['2022-09-15_archive.zip', '2022-09-30_archive.zip']




