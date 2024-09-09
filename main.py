import getopt, sys
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Remove first argument
new_arguments = sys.argv[1:]

# Options
options = "hu:a:v:f:"

# Long options
long_options = []

def help_command():
    print('help command')

def file_command(file):
    try:
        file = open(file=file, mode='rt')
        for line in file:
            values = line.split(',')
            url = values[0] or None
            parent_path = './'
            path = parent_path + values[1] or parent_path
            path_stripped = path.strip()
            if path is not None and not os.path.exists(path_stripped):
                os.mkdir(path_stripped)                    
            if url is not None:
                url_command(url=url, only_audio=False, only_video=False, output_path=path_stripped)    
        file.close()
    except IOError as err:
        print(str(err))

def url_command(url, output_path, only_audio = False, only_video=False):
    file_extension = 'mp4'
    try: 
        YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete_callback) \
            .streams \
            .filter(progressive=True, file_extension=file_extension, only_audio=only_audio, only_video=only_video) \
            .order_by('resolution') \
            .first() \
            .download(output_path=output_path)
    except Exception as error: 
        print(error)

def audio_only_command(url):
    url_command(url=url, only_audio=True)

def video_only_command(url):
    url_command(url=url, only_video=True)

def on_complete_callback(stream, file_path):
    print('Task ' + file_path + ' completed. ')

try:
    args, values = getopt.getopt(new_arguments, options, long_options)
    for current, value in args:
        if(current in ('-h')):
            help_command()
        elif(current in('-u')):
            url_command(url=value)
        elif(current in('-a')):
            audio_only_command(url=value)
        elif(current in('-v')):
            video_only_command()
        elif(current in ('-f')):
            file_command(file=value)
except getopt.error as err:
    print(str(err))