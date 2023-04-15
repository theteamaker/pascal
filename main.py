from src.generate import generate_json
from src.render import render
from src.metaformatter import metaformat
import os

def main():
    try:
        if not os.path.isdir("output"):
            os.mkdir("output")
        if not os.path.isdir("osts"):
            os.mkdir("osts")
        
        generation = generate_json()

        if type(generation) != int:
            print("An error occurred at the generation stage.\n\n", generation)
            return
        
        renderout = render()

        if type(renderout) != int:
            print("An error occured at the render stage.\n\n", renderout)
            return

        input(
            f"The rendering process has been completed.\nUNIQUE IDENTIFIER: {renderout}\nUpload the appropriate files from 'output\{renderout}', and when all selections are finished uploading, press any key to continue...\n")

        specifications = {
            "batch_identifier": renderout,
            "length": generation
        }

        metaformatter = metaformat(specifications)
    except Exception as e:
        print("An error has occurred.\n\n")
        print(e)
        input("\nPress any key to continue...")

if __name__ == "__main__":
    main()