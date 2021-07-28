FROM ubuntu:18.04

WORKDIR /code

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y git vim tmux

# Python package management and basic dependencies
RUN apt-get install -y python3.7 python3.7-dev python3.7-distutils

# Register the version in alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

# Set python 3 as the default python
RUN update-alternatives --set python /usr/bin/python3.7

RUN apt-get install -y python3-pip
RUN pip3 install -Iv pep8==1.7.0

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
