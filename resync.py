import click

@click.command()
@click.option("-f", "--file", help="The path to the subtitles file")
@click.option("-o", "--output", default="correctedsubs.srt", help="The output path for the corrected file")
@click.option("-d", "--delay", help="The delay to add in format hour:minute:second.millisecond")
def main(file, output, delay):
	print(f"You want to add a {delay} to {file} and output it to {output}")

if __name__ == "__main__":	
    main()