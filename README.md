# Subtitles-ReSync

A Python script to correct out-of-sync subtitles files.

Use:

```
python resync.py --file path/to/subtitles.srt --output path/to/output.srt --delay hours:minutes:seconds,milliseconds
```

The script takes the following arguments:
* -f, --file: The path to the .srt subtitles file
* -o, --output: The path and filename of the output file (default: correctedsubs.srt)
* -d, --delay: The delay to add to the file in the format hour:minute:seconds,milliseconds (e.g. 01:23:45,678)