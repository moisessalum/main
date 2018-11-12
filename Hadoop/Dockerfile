FROM centos:latest

# Update package manager
RUN yum -y update
# Install wget
RUN yum -y install wget
# Change to /root
RUN cd /root
# Download Hadoop
RUN wget https://www-eu.apache.org/dist/hadoop/common/hadoop-2.8.5/hadoop-2.8.5-src.tar.gz
# Change to opt directory
RUN cd /opt
# Extract Hadoop
RUN tar xvzf /root/hadoop-2.8.5-src.tar.gz
# Install Java Open JDK
RUN yum -y install java-1.8.0-openjdk
# Make JAVA_HOME available to all users
RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk.x86_64/' > /etc/profile.d/java.sh
# Add HADOOP_HOME
RUN echo 'export HADOOP_HOME=/opt/hadoop-2.8.5;export PATH=$HADOOP_HOME/bin:$PATH' > /etc/profile.d/hadoop.sh
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
RUN cd /opt/hadoop-2.8.5-src
RUN mkdir logs
RUN chmod g+w logs
RUN chown -R yarn:hadoop .
# Configure core-site.xml
RUN mkdir etc
RUN cd etc
RUN mkdir hadoop
RUN cd hadoop
# Add core-site.xml file TODO


CMD ["/bin/bash"]
