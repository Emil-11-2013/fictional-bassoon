# PSEUDO CODE:

# 1. Import necessary libraries:
#    - requests
#    - config module containing HF_API_KEY
import requests
from config import HF_API_KEY

# 2. Set MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
# 3. Set API_URL = "https://api-inference.huggingface.co/models/"/{MODEL_ID}

MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
API_URL = "https://api-inference.huggingface.co/models/{MODEL_ID}"

# 4. headers = {
#     "Authorization": "Bearer " + HF_API_KEY
headers = {
    "Authorization":f"Bearer {HF_API_KEY}"
}

# 5. FUNCTION caption_single_image():
#     5.1. image_source = "test.jpg"
#     5.2. TRY to open image_source in binary mode as file:
#         image_bytes = read file contents
#        CATCH error:
#         print error message
#         return
def caption_single_image():
    image_source = "test.jpg"
    try:
        with open(image_source, "rb") as file:
            image_bytes = file.read()
    except Exception as e:
        print(f"Error opening image: {e}")
        return
#     5.3. Make POST request to API_URL with headers and image_bytes as data
#     5.4. Parse JSON response into result
#     5.5. IF result is a dictionary containing "error":
#         print the error message
#         return
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    result = response.json()

    if isinstance(result, dict) and "error" in result:
        print(f"API Error: {result['error']}")
        return
#     5.6. Extract caption from result[0].get("generated_text", "No caption found.")
#     5.7. Print the image source and the generated caption
    caption = result[0].get("generated_text", "No caption found.")
    print(f"Image: {image_source}")
    print(f"Caption: {caption}")
# 6. FUNCTION main():
#     6.1. Call caption_single_image()
def main():
    caption_single_image()

# 7. IF __name__ == "__main__":
#     7.1. Call main()

if __name__ == "__main__":
    main()