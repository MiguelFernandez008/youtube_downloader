# Youtube Downloader
 A command line script to download Youtube videos

## List of available commands

### -h
Displays help
```
python main.py -h
```
### -u
Download the Youtube url passed as the next argument.
```
python main.py -u https://youtube.com/watch?v=12345
```
### -a
Download the Youtube url passed as the next argument. Audio only mode.
```
python main.py -a https://youtube.com/watch?v=12345
```
### -v.
Download the Youtube url passed as the next argument. Video only mode.
```
python main.py -v https://youtube.com/watch?v=12345
```
### -f 
Download a list of urls written in a text file passed as the next argument. 
```
python main.py -f urls.txt
```
Every file we want to download from the text file must be in the following format: video_url,folder_name. 
```
https://youtube.com/watch?v=11111,FOLDER_NAME
https://youtube.com/watch?v=22222,FOLDER_NAME
```