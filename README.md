# docker-registry
This repository contains a semi-scripted docker registry deployment that utilizes user authentication and private cert TLS.

## Overall approach
The overall approach is to create private certs and basic auth using the [generate_user_and_certs.py](generate_user_and_certs.py) script.  After that, a `data` directory needs to be created, which will be the location where all of the docker registry's images are stored.  It is assumed that you are doing this on the host machine where you want the docker registry to be run.

## Setup
1. Copy the [generate_user_and_certs.py](generate_user_and_certs.py) and [docker-compose.yml](docker-compose.yml) files to where you want to store the docker registry data.
2. Create a directory named `data` - this is where the docker registry's data will be generated and kept.  Ex: `mkdir data`.
4. Run the [generate_user_and_certs.py](generate_user_and_certs.py) script.  Ex:  `./generate_user_and_certs.py`.
5. Launch the registry: `docker-compose up -d`
