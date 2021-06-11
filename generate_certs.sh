#!/bin/bash

# look up local hostname
my_ip=$(hostname -I | cut -d' ' -f1)

# generate private key.pem file and public cert.pem file
openssl req -x509 -newkey rsa:4096 -nodes -keyout docker-registry-key.pem -out docker-registry-cert.pem -days 365 -subj "/C=/ST=/L=/O=/CN=${my_ip}"

# generate the Diffie-Hellman parameter
openssl dhparam -out dhparam.pem 2048

