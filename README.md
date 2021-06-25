# VKR
My VKR work 

### Данные 
[Данные для обучения](https://drive.google.com/file/d/1-5Lik8QjreZ4jTOU6o5aYoJ01hsbUeCy/view?usp=sharing)
[Базовая модель YOLOv3](https://drive.google.com/file/d/1hJXQx8UGSKmgB6du9T-tUA5QsFe4ntwR/view?usp=sharing)
[Переобученная модель](https://drive.google.com/file/d/1nMi0_z4eq0e5-2m9Uap7hCPVY3DhSpO6/view?usp=sharing)


### Создание Docker-образа
```bash
docker build -t fire-ner:training -f Dockerfile .
```

### Запуск Docker-контейнера
```bash
docker run --rm -it -v "$PWD":/usr/src -p 5000:5000 fire-net:training
```