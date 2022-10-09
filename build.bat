echo building
docker build -t andresgroselj/turismoreal-api-central .

echo creating
docker stop turismoreal-api-central
docker container rm turismoreal-api-central
docker create -it -p 8081:8081 --add-host host.docker.internal:host-gateway --name turismoreal-api-central andresgroselj/turismoreal-api-central