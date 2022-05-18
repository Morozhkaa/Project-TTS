# Project-TTS
## Использование

Перейдите по ___[ссылке](https://drive.google.com/drive/folders/1UbTUgJIVP9jP7-jZf-0FMzGboQOuBRCL?usp=sharing)___ и скачайте файлы "last_checkpoint.ckpt"_(524 МБ)_ и "data.tar.gz"_(139 МБ)_.

 Откройте свой _[Google-диск](https://www.google.com/intl/ru_ru/drive/)_ и создайте папку под названием "TTS-Project". В неё загрузите оба скачанных файла.

Теперь можно начинать работу. Откройте "Блокнот_TTS-Model_FastPitch.ipynb" в Google Colab и настройте среду выполнения: 

    Cреда выполнения -> Сменить среду выполнения -> выбрать "GPU" в качестве аппаратного ускорителя.


После этого последовательно запускаем блоки с кодом.

Вы можете синтезировать речь прямо в блокноте. Для этого нужно передать текст, который вы хотите озвучить, в качестве параметра в функцию _infer_. Сделать это можно следующим образом:

![get_audio](https://github.com/Morozhkaa/Project-TTS/blob/main/images/get_audio.png)

Либо, после выполнения еще нескольких блоков кода, вы сможете запустить FastAPI следующей командой. Затем надо будет перейти по _Public URL_:

![run_API](https://github.com/Morozhkaa/Project-TTS/blob/main/images/run_API.png)

В первую очередь вам нужно проинициализировать TTS-model. Для этого нужно в конец URL дописать _/init_ и нажать _Enter_. Это займет некоторое время, после этого на экране вы увидите сообщение _"status": "successfully initialized"_

![init](https://github.com/Morozhkaa/Project-TTS/blob/main/images/initialization.gif)

Отлично! Теперь, дописав в конец URL команду вида _synthesize/any text_ вы получите синтезированную речь с возможностью скачивания и изменения скорости. Пример:

![synthesize](https://github.com/Morozhkaa/Project-TTS/blob/main/images/synthesis_process.gif)
