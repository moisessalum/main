# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

export DOWNLOAD_DIR=/downloads
export JAVA_HOME=/usr/java/default
export PATH=$PATH:$JAVA_HOME/bin
