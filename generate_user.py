#!/usr/bin/env python3

import click
import subprocess


@click.command()
@click.option('--username', prompt='Enter username: ', help='The username.')
@click.option('--password', prompt='Enter password: ', hide_input=True, confirmation_prompt=True)
def main(username, password):
    subprocess.run(f'docker container run --entrypoint htpasswd httpd:2 -Bbn {username} {password} > users', check=True, shell=True)


if __name__ == '__main__':
    main()
