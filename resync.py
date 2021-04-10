import click

timestamp_indexes = []
timestamps = []
numbers = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }

# match_timestamp checks to see if a line matches a .srt timestamp
def match_timestamp(line):
    # temporary template detection while regex is being designed
    template = "XX:XX:XX,XXX --> XX:XX:XX,XXX"
    index = 0
    for char in template:
        if char == "X":
            if line[index] not in numbers:
                return False
        else:
            if line[index] != char:
                return False
        index = index + 1
    return True

# collect_timestamps goes through the source file and finds all timestamps
def collect_timestamps(file_path):
    subfile = open(file_path, "r")
    index = 0
    for line in subfile:
        if match_timestamp(line) == True:
            timestamp_indexes.append(index)
            timestamps.append(line)
        index = index + 1

@click.command()
@click.option("-f", "--file", help="The path to the subtitles file")
@click.option("-o", "--output", default="correctedsubs.srt", help="The output path for the corrected file")
@click.option("-d", "--delay", help="The delay to add in format hour:minute:second.millisecond")
def main(file, output, delay):
    # get timestamps from subtitle file
    collect_timestamps(file)
    # add delay to each timestamp
    # generate updated subtitles file

if __name__ == "__main__":	
    main()