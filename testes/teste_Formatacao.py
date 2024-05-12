from pathlib import Path
import hashlib
import cv2
import numpy as np
from google.protobuf import wrappers_pb2 as wrappers
import google.generativeai as genai
genai.configure(api_key="AIzaSyCZOxfEvWViYVA4dEIX6wbPwrRXruapf1A")# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

def extract_video_frames(pathname: str) -> list:
    """Extrai frames de um vídeo.

    Args:
        pathname (str): O caminho para o arquivo de vídeo.

    Returns:
        list: Uma lista de frames do vídeo.
    """

    frames = []
    vidcap = cv2.VideoCapture(pathname)

    while True:
        success, image = vidcap.read()

        if not success:
            break

        frames.append(numpy_to_blob(image))

    return frames

import numpy as np
from google.protobuf import wrappers_pb2 as wrappers

def numpy_to_blob(array: np.ndarray) -> wrappers.BytesValue:
    """Converte um array NumPy em um objeto Blob.

    Args:
        array (np.ndarray): O array NumPy a ser convertido.

    Returns:
        wrappers.BytesValue: O objeto Blob convertido.
    """

    return wrappers.BytesValue(value=array.tobytes())

convo = model.start_chat(
    history=[
        {"role": "user", "parts": extract_video_frames("C:\\Users\\eacorreia\\Desktop\\Imersao_Alura\\uploads\\teste video.mp4")},
        {"role": "user", "parts": ["a pessoa no video usa oculos?"]},
        {"role": "model", "parts": ["Sim, a pessoa no vídeo usa óculos."]},
    ]
)

convo.send_message("a pessoa no video usa oculos?")
print("********************************************************************************")
print("********************************************************************************")
print("********************************************************************************")
print("********************************************************************************")
print("********************************************************************************")
print("********************************************************************************")
print("********************************************************************************")

print(convo.last.text)