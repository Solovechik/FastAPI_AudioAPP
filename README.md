# FastAPI_AudioAPP


Переменные для запуска можно изменить в файле .env.

Сборка образа:
  - docker-compose build --no-cache;
  - docker-compose up.

Для подключения к БД: 
  - psql -h 127.0.0.1 -p 5433 -d bewise -U bewiseusr.

Создание пользователя:

curl -X 'POST' \
  'http://127.0.0.1:8000/user/create/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username"
}'

Загрузка аудио-файла:

curl -X 'POST' \
  'http://127.0.0.1:8000/record/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'user_id=5' \
  -F 'user_token=a17ba550-f736-4d79-a927-ede401ebd456' \
  -F 'wav_file=@/home/solovechik/Downloads/file_example_WAV_10MG.wav;type=audio/x-wav'

Получение аудио-файла:

curl -X 'GET' \
  'http://127.0.0.1:8000/record/?id=d1f6a81e-5e88-4e85-b800-b480173c17b2&user=5' \
  -H 'accept: */*' \
  -O -J
