FROM fedora:latest

RUN dnf update -y
RUN dnf install -y python gcc-c++ glibc.i686 libstdc++.i686

RUN mkdir QAestro
WORKDIR /QAestro

ADD . /QAestro
