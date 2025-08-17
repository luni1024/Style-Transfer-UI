# How to install Aitviewer and Troubleshooting



We assume you use Linux or WSL



Step 1: Pyenv

1\. install pyenv

Install the required sudo packages:
sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \\

libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \\

libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git



Hint: If it says that one package doesn't exist, execute it again without that package - If you don't, no package gets installed!



curl https://pyenv.run | bash



Follow the instruction in the output or append to the end in .bashrc the following block:

export PYENV\_ROOT="$HOME/.pyenv"

\[\[ -d $PYENV\_ROOT/bin ]] \&\& export PATH="$PYENV\_ROOT/bin:$PATH"

eval "$(pyenv init - bash)"

eval "$(pyenv virtualenv-init -)"



Restart Shell/Terminal



pyenv --version to test,

pyenv versions to show all installed python versions



2\. With pyenv, install a python version between 3.7 and 3.10 (We use 3.9)

pyenv install -v <Python-Version>



3\. Create a pyenv virtual environment using the installed python version

pyenv virtualenv <python\_version> <environment\_name>



4\. Create a new directory and execute:

pyenv local <environment\_name>



This activates the pyenv-virtualenv, whenever you are inside the directory and deactivates it, once you leave the directory



Step 2 (optional): PyTorch

You only need to do this step, if you use a system with cuda support. That's because you can only install the GPU version of pytorch in that case

If you skip this step, the normal pytorch version will be installed automatically in step 3



(Possibly you will need to install a CUDA-toolkit first)



Follow the instructions on this site to install torch with cuda support: https://pytorch.org/get-started/locally/#supported-linux-distributions

Pay attention to choose the right configuration (Linux for WSL/Linux, Pip, Python, <Your CUDA-Version>)



Step 3: Style-Transfer-UI

To clone into our repository (forked from eth-ait/aitviewer) and install everything:

git clone git@github.com:luni1024/Style-Transfer-UI.git

cd Style-Transfer-UI

pip install -e .



You might need to install these packages for the viewer to work:

sudo apt install libegl1 libgl1 libgl1-mesa-dev libegl-dev mesa-utils libxcb-xinerama0 ffmpeg



If it still doesnt work, try also installing these sudo packages: libgles2-mesa-dev, pkgconf or pkg-config, g++, libfontconfig1-dev, libxkbcommon-x11-0,

libxcb-packages



Go to the examples Directory and test, if you can start quickstart.py



If a ctx error occurs, downgrade moderngl-window to 2.4.4 (pip install moderngl-window==2.4.4)

