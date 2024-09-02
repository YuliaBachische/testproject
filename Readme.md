# API Documentation


## Проверка запросов в постман
Все подробности находятся в testprojectcollection.postman_collection.json
## Примеры curl команд
### 1. Login Endpoint
curl -X POST "http://127.0.0.1:8000/login" \
-H "Content-Type: application/json" \
-d '{
  "username": "johndoe",
  "password": "testpassword"
}'
### 2. Get User Information
curl -X GET "http://127.0.0.1:8000/users/me?username=johndoe&password=testpassword" \
-H "Content-Type: application/json"
### 3. List User Notes
curl -X GET "http://127.0.0.1:8000/notes?username=johndoe&password=testpassword" \
-H "Content-Type: application/json"
### 4. Create a New Note
curl -X POST "http://127.0.0.1:8000/notes?username=johndoe&password=testpassword" \
-H "Content-Type: application/json" \
-d '{
  "title": "New Note",
  "content": "This is the content of the new note"
}'
