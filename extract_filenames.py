import re


# get archives from a specified month from a list

files = [
    "2022-10-13_archive.zip",
    "2022-10-13.txt",
    "2022-09-30_archive.zip",
    "2022-09-30.txt",
    "2022-09-15_archive.zip",
    "2022-09-15.txt"
    ]

for path in files:
    # print(path)
    archive_match = re.search("[^ ]+_archive.zip", path)
    # skip none archives
    if archive_match != None:
        # print(archive_matches.string)
        # search for date
        if "2022-09-" in archive_match.string: 
            print(archive_match.string)
# => 2022-09-30_archive.zip
# => 2022-09-15_archive.zip 
