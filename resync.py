import click

timestamp_indexes = []
timestamps = []
delayed_stamps = []
numbers = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }

class Timestamp:
    def __init__(self, hours, minutes, seconds, milli):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milli = milli

# process_timestamp takes a timestamp string and converts it into classform for easier use
def process_timestamp(raw_timestamp):
    components = raw_timestamp.split(":")
    hours = int(components[0])
    minutes = int(components[1])
    seconds_components = components[2].split(",")
    seconds = int(seconds_components[0])
    milli = int(seconds_components[1])
    return Timestamp(hours, minutes, seconds, milli)

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
            stamps = line.split(" ")
            firstTimestamp = process_timestamp(stamps[0])
            secondTimestamp = process_timestamp(stamps[2])
            timestamps.append([firstTimestamp, secondTimestamp])
        index = index + 1
        
def add_timestamps(timestamp, delay_stamp):
    milli = timestamp.milli + delay_stamp.milli
    seconds_extra = int(milli / 1000)
    milli = milli % 1000
    
    seconds = timestamp.seconds + delay_stamp.seconds + seconds_extra
    minutes_extra = int(seconds / 60)
    seconds = seconds % 60
    
    minutes = timestamp.minutes + delay_stamp.minutes + minutes_extra
    hours_extra = int(minutes / 60)
    minutes = minutes % 60
    
    hours = timestamp.hours + delay_stamp.hours + hours_extra
    hours = hours % 100
    
    return Timestamp(hours, minutes, seconds, milli)

# add_delay goes through all of the collected timestamps and adds the user-specified delay
def add_delay(delay):
    for timestamp in timestamps:
        delayed_stamp_1 = add_timestamps(timestamp[0], delay)
        delayed_stamp_2 = add_timestamps(timestamp[1], delay)
        delayed_stamps.append([delayed_stamp_1, delayed_stamp_2])

@click.command()
@click.option("-f", "--file", help="The path to the subtitles file")
@click.option("-o", "--output", default="correctedsubs.srt", help="The output path for the corrected file")
@click.option("-d", "--delay", help="The delay to add in format hour:minute:second,millisecond")
def main(file, output, delay):
    # get timestamps from subtitle file
    collect_timestamps(file)
    # add delay to each timestamp
    delay_stamp = process_timestamp(delay)
    add_delay(delay_stamp)
    # generate updated subtitles file
    
if __name__ == "__main__":	
    main()