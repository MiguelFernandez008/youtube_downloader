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

# Config
parent_path = './downloads'
file_extension = 'mp4'
help_command_name = '-h'
url_command_name = '-u'
audio_command_name = '-a'
video_command_name = '-v'
file_command_name = '-f'

def help_command():
    print('{} = Displays help.'.format(help_command_name))
    print('{} = Download the youtube url passed as the next argument.'.format(url_command_name))
    print('{} = Download the youtube url passed as the next argument. Audio only mode.'.format(audio_command_name))
    print('{} = Download the youtube url passed as the next argument. Video only mode.'.format(video_command_name))
    print('{} = Download a list of urls written in a text file passed as the next argument. Every file we want to download from the text file must be in the following format: video_url,folder_name. Ex: https://youtube.com/watch?v=12345,FOLDER_NAME'.format(file_command_name))
    print('For for more info go to see repository README file.')

def file_command(file):
    print('Starting file download...')
    try:
        file = open(file=file, mode='rt')
        for index, line in enumerate(file):
            values = line.split(',')
            if len(values) < 2:
                print('Line {} has not correct format'.format(index + 1))
                continue
            url = values[0] or None            
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
    print('Starting audio only download...')
    url_command(url=url, only_audio=True)

def video_only_command(url):
    print('Starting video only download...')
    url_command(url=url, only_video=True)

def on_complete_callback(stream, file_path):
    print('Task ' + file_path + ' completed. ')

try:
    args, values = getopt.getopt(new_arguments, options, long_options)
    for current, value in args:
        if(current in (help_command_name)):
            help_command()
        elif(current in(url_command_name)):
            print('Starting url download...')
            url_command(url=value)
        elif(current in(audio_command_name)):
            audio_only_command(url=value)
        elif(current in(video_command_name)):
            video_only_command()
        elif(current in (file_command_name)):
            file_command(file=value)
except getopt.error as err:
    print(str(err))