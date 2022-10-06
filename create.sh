sudo docker stop turismoreal-api-central
sudo docker container rm turismoreal-api-central
sudo docker create -it -p 8081:8081 --add-host host.docker.internal:host-gateway --name turismoreal-api-central andresgroselj/turismoreal-api-central