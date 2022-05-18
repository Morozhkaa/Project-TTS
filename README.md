# Project-TTS

## API
> Framework is ___[Fastapi](https://fastapi.tiangolo.com/)___


## Models
>  TTS Model:  ___[En FastPitch](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_en_fastpitch)___
> 
>  TTS Vocoder: ___[Hifigan](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_hifigan)___

## Руководство пользователя

1.  Перейдите по ___[ссылке](https://drive.google.com/drive/folders/1UbTUgJIVP9jP7-jZf-0FMzGboQOuBRCL?usp=sharing)___ и скачайте файлы "last_checkpoint.ckpt"_(524 МБ)_ и "data.tar.gz"_(139 МБ)_.

 2. Откройте свой _[Google-диск](https://www.google.com/intl/ru_ru/drive/)_ и создайте папку под названием "TTS-Project". В неё загрузите оба скачанных файла.

Теперь можно начинать работу.

3. Откройте "Блокнот_TTS-Model_FastPitch.ipynb" в Google Colab и настройте среду выполнения: 

        Cреда выполнения -> Сменить среду выполнения -> выбрать "GPU" в качестве аппаратного ускорителя.


4. После этого последовательно запустите все блоки с кодом.

<br>

### Варианты использования:

> 1).  Вы можете синтезировать речь прямо в блокноте. Для этого нужно передать текст, который вы хотите озвучить, в качестве параметра в функцию _infer_. Сделать это можно следующим образом:

> <img src="https://github.com/Morozhkaa/Project-TTS/blob/main/images/get_audio.png" width="550">

<br>

> 2). Либо, после выполнения еще нескольких блоков кода, вы сможете запустить FastAPI следующей командой (затем надо будет перейти по _Public URL_):

> <img src="https://github.com/Morozhkaa/Project-TTS/blob/main/images/run_API.png" width="550">

>>* В первую очередь вам нужно проинициализировать TTS-model. Для этого нужно в конец URL дописать _/init_ и нажать _Enter_. Это займет некоторое время, после чего на экране вы увидите сообщение _"status": "successfully initialized"_

>>![init](https://github.com/Morozhkaa/Project-TTS/blob/main/images/initialization.gif)

>> * Отлично! Теперь, дописав в конец URL команду вида _synthesize/any text_ вы получите синтезированную речь с возможностью скачивания и изменения скорости. Пример:

>> ![synthesize](https://github.com/Morozhkaa/Project-TTS/blob/main/images/synthesis_process.gif)
