FROM centos:latest

# Update package manager
RUN yum -y update
# Install wget
RUN yum -y install wget
# Change to root and download Hadoop
RUN cd /root && wget https://archive.apache.org/dist/hadoop/core/hadoop-2.6.0/hadoop-2.6.0.tar.gz
# Download Hadoop
#RUN wget https://www-eu.apache.org/dist/hadoop/common/hadoop-2.8.5/hadoop-2.8.5-src.tar.gz
# Change to opt directory and untar Hadoop
RUN cd /opt && tar xvzf /root/hadoop-2.6.0.tar.gz
# Extract Hadoop
#RUN tar xvzf /root/hadoop-2.6.0.tar.gz
# Install Java Open JDK
RUN yum -y install java-1.7.0-openjdk
# Make JAVA_HOME available to all users
RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64' > /etc/profile.d/java.sh
#RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.191-2.6.15.4.el7_5.x86_64' > ~/.bashrc
# Add HADOOP_HOME
#RUN echo 'export HADOOP_HOME=/opt/hadoop-2.6.0;export PATH=$HADOOP_HOME/bin:$PATH' > ~/.bashrc
RUN echo 'export HADOOP_HOME=/opt/hadoop-2.6.0;export PATH=$HADOOP_HOME/bin:$PATH' > /etc/profile.d/hadoop.sh
# Source java.sh and hadoop.sh
RUN source /etc/profile.d/java.sh
RUN source /etc/profile.d/hadoop.sh
# Create users and groups
RUN groupadd hadoop
RUN useradd -g hadoop yarn
RUN useradd -g hadoop hdfs
RUN useradd -g hadoop mapred
# Make data and log directories
RUN mkdir -p /var/data/hadoop/hdfs/nn
RUN mkdir -p /var/data/hadoop/hdfs/snn
RUN mkdir -p /var/data/hadoop/hdfs/dn
RUN chown -R hdfs:hadoop /var/data/hadoop/hdfs
RUN mkdir -p /var/log/hadoop/yarn
RUN chown -R yarn:hadoop /var/log/hadoop/yarn
# Create log directory in YARN
RUN cd /opt/hadoop-2.6.0 && mkdir logs && chmod g+w logs && chown -R yarn:hadoop .
#RUN mkdir logs
#RUN chmod g+w logs
#RUN chown -R yarn:hadoop .
# Configure core-site.xml
#RUN cd /opt/hadoop-2.8.5-src  && mkdir etc && cd etc && mkdir hadoop
#RUN cd etc
#RUN mkdir hadoop
#RUN cd hadoop
# Add core-site.xml file
ADD core-site.xml /opt/hadoop-2.6.0/etc/hadoop
ADD hdfs-site.xml /opt/hadoop-2.6.0/etc/hadoop
ADD mapred-site.xml /opt/hadoop-2.6.0/etc/hadoop
ADD yarn-site.xml /opt/hadoop-2.6.0/etc/hadoop
ADD hadoop-env.sh /opt/hadoop-2.6.0/etc/hadoop
ADD mapred-env.sh /opt/hadoop-2.6.0/etc/hadoop
ADD yarn-env.sh /opt/hadoop-2.6.0/etc/hadoop
# Format HDFS
#RUN su - hdfs && cd /opt/hadoop-2.6.0/bin && ./hdfs namenode -format
#RUN export HADOOP_LIBEXEC_DIR=${HADOOP_HOME}/libexec > ~/.bashrc



#CMD ["/bin/bash"]
