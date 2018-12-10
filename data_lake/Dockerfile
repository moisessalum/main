FROM centos:7

MAINTAINER "Moisés Salum" <rodriguez.fq@gmail.com>

RUN mkdir downloads
COPY .bashrc .bashrc
RUN yum install -y wget
# Install Java JDK from Oracle JDK download page
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm
RUN rpm --install jdk-8u131-linux-x64.rpm
# Install Hadoop 2.7.3
RUN wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz
RUN tar -xzvf hadoop-2.7.3.tar.gz
# 
