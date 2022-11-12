## Проект чемпионата "Цифровой прорыв сезон: ИИ" Омская область
### Детекция человеческих силуэтов на снимках лесного массива, полученных с помощью БПЛА (Person Detection from Aerial Drone Images)

### Установка

Для запуска проекта необходимо установить [docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker) с поддержкой nvidia. Для трекинга экспериментов необходимо установить [wandb](https://wandb.ai/site) и запустить сервер (опционально).

Установка WandB:
``` bash
pip install wandb
wandb server start
```

Сборка docker контейнера:
``` bash
docker build . -t pytorch:v1
```

Запуск контейнера:
``` bash
docker run --gpus all --ipc=host --network=host -it --rm -v $(pwd):/app  pytorch:v1
```

Для использования трекинга экспериментов при помощи WandB необходимо выполнить login:
``` bash
python3 -m wandb login --relogin --host=http://localhost:8080/ "WandB Token"
```

### Подготовка данных
Подготовка данных осуществляется в ноутбуках jupyter. Перед началом работы необходимо загрузить архивы с данными по задаче и расположить из по пути **/data/raw/**. Для работы рекомендуется использовать Jupyter Lab:
``` bash
jupyter lab
```

### Обучение нейронной сети
Обучение нейронной сети можно выполнить при помощи ноутбука **2-pdn-data-preparation** после подготовки данных, либо при помощи Bash скрипта:
``` bash
bash ./scripts/train.sh
```
Данные по лучшему обучению доступны на [Google Disk](https://drive.google.com/file/d/18Ot_4_iqFHad7ntMhvr1WU1nPigOGAXe/view?usp=share_link).

### Описание структуры проекта
```
├── data
│   ├── interim                                 <- Промежуточные данные
│   ├── processed                               <- Итоговые данные
│   ├── raw                                     <- Исходные данные
│   └── train                                   <- Данные для обучения НС
│
├── docs                                        <- Описание задачи от организаторов чемпионата
│
├── notebooks                                   <- Jupyter notebooks
│   ├── 1-pdn-initial-data-exploration.ipynb    <- Исследование данных
│   ├── 2-pdn-data-preparation.ipynb            <- Обработка данных
│   ├── 3-pdn-dataset-viewing.ipynb             <- Просмотр данных
│   ├── 4-pdn-submission-preparing.ipynb        <- Формирование решения
│   └── 5-pdn-image-augmentation.ipynb          <- Аугментация данных
│
├── src                                         <- Вспомогательные функции
│   ├── iou.py                                  <- Intersection over union
│   ├── markup_convertors.py                    <- Функции преобразования разметки
│   ├── nms.py                                  <- Non max suppression
│   └── transforms.py                           <- Функции трансформации изображений
│
├── scripts                                     <- Вспомогательные функции
│   ├── train.sh                                <- Скрипт для обучения НС
│   └── detect.sh                               <- Скрипт для формирования детекций
│
├── requirements.txt                            <- Зависомости, необходимые для запуска проекта
│
└── Dockerfile                                  <- Файл для сборки Docker образа
```