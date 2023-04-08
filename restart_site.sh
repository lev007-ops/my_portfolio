echo Stop docker compose
docker-compose down

echo Pulling data from git
git pull


echo Start docker compose
docker-compose up --build -d

echo Migrate
docker-compose exec web python3 manage.py migrate