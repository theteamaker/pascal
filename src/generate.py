import os, re, uuid, json

def generate_soundtrack(dir):

    soundtrack = []

    # I'd prefer that this expression be simplified down to
    # cover only .wav and .flac files, but I know sometimes we
    # just can't get soundtracks in lossless format, as tragic
    # as that may be. :sadcat:
    exp = (r'[\s\S]*.(wav|flac|mp3|ogg|aac|m4a)$')

    for file in dir:
        if re.search(exp, file):
            soundtrack.append(file)
    
    return soundtrack

def generate_json():
    try:

        soundtrack = []

        while True:
            folder_name = input("Input Soundtrack Folder Name: ")
            folder_path = f"osts/{folder_name}"

            try:
                os.listdir(folder_path)
            except FileNotFoundError:
                print("Directory not found. Please try again.")
                continue

            generated_soundtrack = generate_soundtrack(os.listdir(folder_path))

            if len(generated_soundtrack) == 0:
                print("There don't seem to be any files in this directory. Please try again.")
                print(os.listdir(folder_path))
                print(generated_soundtrack)
                continue
            else:
                soundtrack = generated_soundtrack
                break

        master_dict = {}

        exp = ""
        while True:
            to_exp = input("Regex Expression (leave blank if title editing is unnecessary): ")

            if to_exp == "":
                break
            
            # Print an example for confirmation 
            print(re.sub(to_exp, "", soundtrack[0])) 
            correct = input("Is the expected formatting correct? (y/n)\n")
            if correct.lower() == "y":
                exp = to_exp
                break
            elif correct.lower() == "n":
                continue

        for filename in soundtrack:

            unstripped_title = re.sub(exp, "", filename)
            title = re.sub(r'.(wav|mp3|flac|ogg|aac|m4a)$', "", unstripped_title)

            unique_uuid = uuid.uuid4()
            uuid_string = str(unique_uuid).replace("-", "")
            master_dict[uuid_string] = {
                "title": title,
                "file": os.path.abspath(f"{folder_path}/{filename}")
            }

        master_dict['thumbnail'] = os.path.abspath(f"{folder_path}/thumbnail.png")
        json_object = json.dumps(master_dict, indent=4)

        with open("dictionary.json", "w") as outfile:
            outfile.write(json_object)
            
        return len(soundtrack)
    
    except Exception as e:
        return e