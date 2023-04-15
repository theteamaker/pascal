import random, json, os, ffmpeg

def render():

    try:
        random.seed()
        batch_identifier = random.randint(100001, 999999)

        os.mkdir(f"output/{str(batch_identifier)}")

        with open('dictionary.json', 'r') as openfile:
            loaded_dict = json.load(openfile)

            for num, video in enumerate(loaded_dict):

                if str(video) == "thumbnail":
                    continue

                id = str(video)
                audio = ffmpeg.input(loaded_dict[video]["file"])
                thumbnail = ffmpeg.input(loaded_dict["thumbnail"], loop=1, t=1, framerate=15)
                ffmpeg.concat(thumbnail, audio, v=1, a=1).output(f"output/{batch_identifier}/{num + 1} {batch_identifier} {id}.mp4", audio_bitrate=320000, vcodec="h264").run(overwrite_output=True)

        return batch_identifier
    
    except Exception as e:
        return e