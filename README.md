# Installation on macOS

Install PyTorch for macOS https://pytorch.org/get-started/locally/#macos-version

Install python3: 
* brew install python

At the time, brew installed [python@3.13](https://formulae.brew.sh/formula/python@3.13#default).

According to the cask, a successful installation should install `python3` and `pip3`.

Now, create a virtual environment to install pytorch and torchvision.

python3

Install torch and torchvision; since my version of Python is being managed by brew, I used brew instead of pip3:

* python3 -m venv rc_local_llm
* VSCode noticed an environment was made and I approved using this env. for this folder
* rc_local_llm/bin/pip3 install torch torchvision

Verify the installation by running ./verify_installation.py

* rc_local_llm/bin/python3 verify_installation.py

Output should resemble

```
tensor([[0.9258, 0.7378, 0.5676],
        [0.6134, 0.6952, 0.2686],
        [0.9542, 0.6940, 0.4266],
        [0.9273, 0.3701, 0.7406],
        [0.0249, 0.4018, 0.4693]])
```