# Pascal

A program used to simplify the process of uploading video game music soundtracks to [Maya's Archive](https://www.youtube.com/@MayasArchive/).

(Named after my friend, Pascal — I wouldn't have the strength to engage in projects like these without her.)

## What it does

Pascal simply documents a directory of **audio files**, pairs them with an associated **image file**, and from that uses FFmpeg to render **video files** which mux each audio file and the image file. Each video is uniquely identifiable through a UUID within its title.

The user then manually uploads all videos to the desired YouTube channel, and, after accepting the prompt to continue, is asked a few questions which will then generate appropriate descriptions, titles and a playlist for the batch upload.

## Why aren't you uploading the videos through the API?
YouTube API's daily quota for new developers is currently **10,000**. Each video upload costs 1,600 tokens, meaning that I could only upload a maximum of 6 videos per day if I were to upload it through the API. By handling this part of the process myself, massive amounts of API tokens are saved for what's ultimately the harder end of the work: metadata formatting, video titling, and playlist management.

## Requirements
[ffmpeg](https://ffmpeg.org/) — .exe can be stored in runtime dir, or PATH variable
[google-api-python-client](https://pypi.org/project/google-api-python-client/) >= 2.85.0
[google-auth-httplib2](https://pypi.org/project/google-auth-httplib2/) >= 0.1.0
[google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/) >= 1.0.0

## Usage
### Before you begin...
There's a specific file structure the program will adhere to. Keep this in mind. It's best to create the osts folder yourself, and the folder for the specific OST in question before you begin the program, structuring it similar to the example below.

 - pascal
	 - src/
	 - output/
	 - osts/
		 - smb1
			 - "01. 1-1 Overworld.wav", "02. 1-2 Underground.wav", etc...
			 - thumbnail.png **(always make sure the thumbnail is named this)**
	 - ffmpeg.exe (or PATH variable)
	 - main.py
	 - requirements.txt

**Step 1.** Run main.py and answer the preliminary question about where the OST is. You can use the relative path here.

**Step 2.** It'll ask you if you want to make any Regex-style subtractive modifications to the song titles in the folder. In this case, we want to get rid of the "01. ", "02. " at the beginning of each song, so we'll specify a regex expression for it to use: *\d\d\.\w*

**Step 3.** Wait for the videos to render out. They'll be in a folder now created in the output directory, which is named with the batch's unique identifier.

**Step 4.** Upload all the videos to YouTube manually through your browser. Again, we're saving on API usage here, and every little bit counts.

**Step 5.** Answer all necessary questions to generate the appropriate description, title and playlist data for each upload.

Your uploads should now be appropriately titled, descriptions should be properly added, and they should be within the appropriate playlist, with all that heavy lifting finished by the program.

# Future
For now, the user has to manually publicize the uploads after they're uploaded. I don't have a real justification for this, other than like, it's 6:00AM at the time of making this initial commit, and I just want to get to sleep. 

It's certainly riddled with bugs, and abilities for the user to do things to make it just... fail.

However, it's just a hobbyist project, and as it stands right now, I'm happy enough with it.

"Let's positive thinking!"
*- Maya Amano*
