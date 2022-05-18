# Project-TTS
## Использование

Перейдите по ___[ссылке](https://drive.google.com/drive/folders/1UbTUgJIVP9jP7-jZf-0FMzGboQOuBRCL?usp=sharing)___ и скачайте файлы "last_checkpoint.ckpt"_(524 МБ)_, "data.tar.gz"_(139 МБ)_, "test_audio.wav"_(278 KБ)_.

 Откройте свой _[Google-диск](https://www.google.com/intl/ru_ru/drive/)_ и создайте папку под названием "TTS-Project". В неё загрузите скачанный файл "last_checkpoint.ckpt".

Теперь можно начинать работу. Откройте "Блокнот_TTS-Model_FastPitch.ipynb" в Google Colab и настройте среду выполнения: 

    Cреда выполнения -> Сменить среду выполнения -> выбрать "GPU" в качестве аппаратного ускорителя.
    
Затем нужно будет загрузить архив с данными. Откройте панель слева, нажмите на "загрузить файлы" и добавьте ранее скачанные "data.tar.gz", "test_audio.wav". Загрузка займет некоторое время.

![gif](https://github.com/Morozhkaa/Project-TTS/blob/main/images/data_loading.gif)
