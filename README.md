# Installation on macOS on macBook Air

Install PyTorch for macOS https://pytorch.org/get-started/locally/#macos-version

Install python3@3.11: 
* brew install python

Via the book's recommendation on p. 254:
> Many scientific computing libraries do not immediately support the newest version of Python. Therefore, when installing PyTorch, it’s advisable to use a version of Python that is one or two releases older. For instance, if the latest version of Python is 3.13, using Python 3.11 or 3.12 is recommended.

At the time, brew installed [python@3.11](https://formulae.brew.sh/formula/python@3.11#default).

According to the cask, a successful installation should install `python3` and `pip3`.

Now, create a virtual environment to install pytorch and torchvision.

python3

Install torch and torchvision; since my version of Python is being managed by brew, I used brew instead of pip3:

* python3 -m venv rc_local_llm

Note: -m: run library module as a script (terminates option list)

* VSCode noticed an environment was made and I approved using this env. for this folder
* rc_local_llm/bin/pip3 install torch==2.4.0 torchvision
OR
* pip3 install torch==2.4.0 torchvision if already inside the venv

NOTE: Consider updating pip by running
* python3 -m pip install --upgrade pip

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