!pip install -q -U transformers==4.37.2
!pip install -q bitsandbytes==0.41.3 accelerate==0.25.0
!pip install -q gradio

import torch
from transformers import BitsAndBytesConfig, pipeline

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model_id = "llava-hf/llava-1.5-7b-hf"

pipe = pipeline("image-to-text",
                model=model_id,
                model_kwargs={"quantization_config": quantization_config})

import whisper
import gradio as gr
import time
import warnings
import os

image_path = "img.jpg"

import nltk
nltk.download('punkt')
from nltk import sent_tokenize

import locale
print(locale.getlocale())  # Before running the pipeline
# Run the pipeline
print(locale.getlocale())  # After running the pipeline

max_new_tokens = 200

prompt_instructions ="I need help. What should I respond with, My teacher has asked me a question, it might be related to what is in the picture and this is what she has said before this :"




prompt = "USER: <image>\n" + prompt_instructions + textfinal +"\nASSISTANT:"

outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
# outputs
# print(outputs[0]["generated_text"])
for sent in sent_tokenize(outputs[0]["generated_text"]):
    print(sent)