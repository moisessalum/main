# https://gist.github.com/tsabat/1498393
sudo apt-get install zsh
sudo apt-get install git-core
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
# First create a password for the user to then change to ZSH
# https://aws.amazon.com/premiumsupport/knowledge-center/set-change-root-linux/
chsh -s `which zsh`
