#
# Base Docker image for wger images
#
#
# This dockerfile simply installs all common dependencies for the
# other images and does not do anything on its own.
#
# docker build --tag asgards254/base .
#

FROM ubuntu:16.04

MAINTAINER Andela Asgards <asgards@andela.com>

# Install dependencies
RUN apt-get update;\
    apt-get install -y nodejs nodejs-legacy npm git \
        python-virtualenv python3-dev \
        libjpeg8-dev zlib1g-dev libwebp-dev \
        sudo

# Add wger user
RUN adduser wger --disabled-password --gecos ""
RUN echo "wger ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/wger
