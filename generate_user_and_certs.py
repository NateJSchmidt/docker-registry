#!/usr/bin/env python3
"""
This python script creates the certs that will be used by the docker registry.  In addition, it will also generate
username/password style credentials to be used by the registry.
"""

import click
import os
import pathlib
import subprocess


@click.command()
@click.option('--username', prompt='Enter username: ', help='The username.')
@click.option('--password', prompt='Enter password: ', hide_input=True, confirmation_prompt=True)
def main(username, password):
    # create the certs directory
    certs_dir = pathlib.Path.cwd().joinpath('certs')
    certs_dir.mkdir(exist_ok=True)
    os.chdir(str(certs_dir.absolute()))

    print("This may take some time, please be patient...")
    
    # create the users file
    subprocess.run(f'docker container run --entrypoint htpasswd httpd:2 -Bbn {username} {password} > users', check=True, shell=True)

    # create the certs
    my_ip = subprocess.run("hostname -I | cut -d' ' -f1", check=True, capture_output=True, shell=True).stdout.decode().strip()
    subprocess.run(f'openssl req -x509 -newkey rsa:4096 -nodes -keyout docker-registry-key.pem -out ' \
        f'docker-registry-cert.pem -days 365 -subj "/C=/ST=/L=/O=/CN={my_ip}" -addext "subjectAltName = DNS:192.168.0.10',
        check=True,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
    # generate the Diffie-Hellman parameter
    subprocess.run(f'openssl dhparam -out dhparam.pem 2048', check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("All done!")


if __name__ == '__main__':
    main()
