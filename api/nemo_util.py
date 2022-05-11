from nemo.collections.tts.models import FastPitchModel
from nemo.collections.tts.models import HifiGanModel
from nemo.collections.nlp.models.machine_translation import MTEncDecModel
from scipy.io import wavfile

translation_models = {
    'en': {
        'ru': 'nmt_en_ru_transformer6x6',
    },
    'ru': {
        'en': 'nmt_ru_en_transformer6x6',
    }
}

synthesis_models = {
    'en': {
        'spec_gen': 'tts_en_fastpitch',
        'vocoder': 'tts_hifigan'
    }
}

is_initialized = False
initialize_on_startup = True

def models_init():
    global is_initialized
    if is_initialized:
        return True

    try:
        translation_models['en']['ru'] = MTEncDecModel.from_pretrained(model_name="nmt_en_ru_transformer6x6")
        translation_models['ru']['en'] = MTEncDecModel.from_pretrained(model_name="nmt_ru_en_transformer6x6")
        synthesis_models['en']['spec_gen'] = FastPitchModel.from_pretrained('tts_en_fastpitch').eval().cuda()
        synthesis_models['en']['vocoder'] = HifiGanModel.from_pretrained('tts_hifigan').eval()
        is_initialized = True
        return 200
    except:
        return 404


if initialize_on_startup:
    models_init()