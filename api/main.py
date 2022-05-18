# !pip install FastAPI -q
# !pip install uvicorn -q
# !pip install fastapi nest-asyncio pyngrok uvicorn -q
# !pip install noisereduce -q
import soundfile as sf
import noisereduce as nr
from scipy.io import wavfile
from fastapi.responses import Response, FileResponse

import sys
import os
import pandas as pd
import subprocess
import json
import codecs
import unidecode
import nest_asyncio
from pyngrok import ngrok
import uvicorn

is_initialized = False

from nemo.collections.tts.models import FastPitchModel
from nemo.collections.tts.models import HifiGanModel
from nemo.collections.nlp.models.machine_translation import MTEncDecModel

synthesis_models = {
    'en': {
        'spec_gen': 'tts_en_fastpitch',
        'vocoder': 'tts_hifigan'
    }
}

def models_init():
    global is_initialized
    if is_initialized:
        return True
    try:
        ckpt = "/content/gdrive/MyDrive/ljspeech_to_6097_no_mixing_5_mins/FastPitch/2022-05-13_18-13-53/checkpoints/FastPitch--v_loss=0.7351-epoch=24-last.ckpt"
        synthesis_models['en']['spec_gen'] = FastPitchModel.load_from_checkpoint(ckpt).eval().cuda()
        synthesis_models['en']['vocoder'] = HifiGanModel.from_pretrained('tts_hifigan').eval()
        is_initialized = True
        return 200
    except:
        return 404

def process_text(text: str) -> str:
    text = text.replace('&quest', '?')
    return text

def normalize_text(txt: str) -> str:
    #You can change it
    valid_chars = (" ", "'", "!", "?", ".", ",", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z")
    new_txt = unidecode.unidecode(txt.lower().strip())
    res_arr = []
    for c in new_txt:
        if c in valid_chars:
            res_arr.append(c)
        else:
            res_arr.append(' ')
    res = ''.join(res_arr).strip()
    return ' '.join(res.split())

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Translator for message exchange API is currently on."}

@app.get('/test_audio')
async def test_audio():
    return FileResponse('test_audio.wav')

@app.get("/init")
async def init():
    init_result = models_init()
    return {"status": "init_result"}

@app.get("/synthesize/{text}")
async def synthesize(text: str):
    pr_text = process_text(text)
    normalized_text = normalize_text(pr_text)
    try:
        with open(f'/audio/{normalized_text}.wav') as f:
            return FileResponse(f'audio/{normalized_text}.wav')
    except IOError:
        spec_gen = synthesis_models['en']['spec_gen']
        vocoder = synthesis_models['en']['vocoder']

        parsed = spec_gen.parse(normalized_text)
        spectrogram = spec_gen.generate_spectrogram(tokens=parsed)
        waveform = vocoder.convert_spectrogram_to_audio(spec=spectrogram)
        audio = waveform[0].cpu().detach().numpy().tolist()
        sf.write(f'audio/{normalized_text}.wav', audio, 22050)
        return FileResponse(f'audio/{normalized_text}.wav')