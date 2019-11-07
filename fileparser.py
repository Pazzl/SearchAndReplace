import argparse

parser = argparse.ArgumentParser(description="Find/replace some string in text file")
parser.add_argument("file", metavar="<filename>", type=str)
parser.add_argument("--search", metavar="<string to search>", type=str, required=True)
parser.add_argument("--replace", metavar="<string to replace>", type=str, required=False)

args = parser.parse_args()
if args.replace is None:
    try:
        with open(args.file, mode='rt') as readFile:
            data = readFile.read()
        sCount = data.count(args.search)
        if sCount != 0:
            print("Found %d matches of text '%s' in file '%s'" % (sCount, args.search, args.file))
        else:
            print("Can't find any matches for text '%s' in file '%s'" % (args.search, args.file))
    except OSError as exception:
        print("%s: %s" % (args.file, exception.strerror))
else:
    try:
        with open(args.file, mode='rt') as readFile:
            data = readFile.read()
        if data.count(args.search) != 0:
            data = data.replace(args.search, args.replace)
            with open(args.file, mode="wt") as writeFile:
                writeFile.write(data)
                writeFile.flush()
                print("Successfully replaced text '%s' with '%s' in file '%s'" % (args.search, args.replace, args.file))
        else:
            print("Can't find any matches for text '%s' in file '%s' for replace with '%s'" % (
                args.search, args.file, args.replace))
    except OSError as exception:
        print("%s: %s" % (args.file, exception.strerror))
