# Imports the Google Cloud client libraries
from google.cloud import translate_v2 as translate

def detect_language(text: str) -> dict:
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print(f"Text: {text}")
    print("Confidence: {}".format(result["confidence"]))
    print("Language: {}".format(result["language"]))

    return result

# Uncomment the following code to test just the backend
# Example: python translate.py --text "ciao"
# if __name__ == "__main__":
#     import argparse
#     # defined required argument
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-t", "--text", type=str,required=True)
#     args = parser.parse_args()
#     detect_language(args.text)