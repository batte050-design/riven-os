# build container
docker build -f db/Dockerfile.simple -t pg-test .

# run container
docker run -d --rm \
   --name riven-db-test \
   -p 8888:5432 \
   -e POSTGRES_PASSWORD=password \
   -v riven_db_test:/var/lib/postgresql/data \
    pg-test:latest
