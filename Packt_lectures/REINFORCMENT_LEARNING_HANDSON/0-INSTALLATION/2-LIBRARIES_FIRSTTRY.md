# PAssing the pip command inside the python's virtual environment
```bash
(PACKTRL) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT$ cd Deep-Reinforcement-Learning-Hands-On-Third-Edition/
(PACKTRL) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT/Deep-Reinforcement-Learning-Hands-On-Third-Edition$ python3 -m pip install -r requirements.txt 2>&1 | tee requirements.log
```
## I need to work on the requirements.txt
* So I create a copy
```bash
(PACKTRL) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT/Deep-Reinforcement-Learning-Hands-On-Third-Edition$ cp -pv requirements.txt ~/CONSULTANT/technical_reviewing/Packt_lectures/REINFORCMENT_LEARNING_HANDSON/0-INSTALLATION
```
- my python version
```bash
(PACKTRL) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT/Deep-Reinforcement-Learning-Hands-On-Third-Edition$ python3 --version
Python 3.14.4 # The book has been written for python 3.12.X
```
# We start again the try
```bash
(PACKTRL) jpmena@jpmena-HP-OmniBook-X-Flip-Laptop-14-fm0xxx:~/CONSULTANT/Deep-Reinforcement-Learning-Hands-On-Third-Edition$ python3 -m pip install -r ~/CONSULTANT/technical_reviewing/Packt_lectures/REINFORCMENT_LEARNING_HANDSON/0-INSTALLATION/requirements.txt 2>&1 | tee requirements.log
```
* I still need numpy < 2 for ptan
* [versions compatibilities between torch and torchvision](https://pytorch.org/get-started/previous-versions/)
## I have a ptan problem
```
The conflict is caused by:
    The user requested torch==2.9.1
    torchvision 0.24.1 depends on torch==2.9.1
    pytorch-ignite 0.5.1 depends on torch<3 and >=1.3
    ptan 0.8.1 depends on torch==2.5.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict
```
