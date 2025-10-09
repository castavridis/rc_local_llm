# Building LLMs from Scratch
## Installing Python3, PyTorch, TorchVision, and TikToken

TBH, I got a little frustrated during my install because I didn't see the recommendation to install  **python@3.11** until much later when I was going through Appendix A. It didn't take long to reinstall things but I was still miffed. You probably could go forward with python@latest which is currently python@3.13 but I decided to use 3.11 instead.

Here's the helpful note from p. 254:

> **NOTE:** Many scientific computing libraries do not immediately support the newest version of Python. Therefore, when installing PyTorch, it’s advisable to use a version of Python that is one or two releases older. For instance, if the latest version of Python is 3.13, using Python 3.11 or 3.12 is recommended.

These installation steps were successful on a device with the following specs:
```
* Model: MacBook Air, 2024
* macOS: Sequoia
* Chip: Apple M3
* Memory: 16 GB
* Shell: zsh
* Editor: VSCode
```

I used Homebrew to install Python3. Installation [instructions for installing Homebrew are here](https://brew.sh). I did not test installing Homebrew as part of this write up.

1. `brew install python@3.11`

Upon a successful installation you'll see

```
Unversioned and major-versioned symlinks `python`, `python3`, `python-config`, `python3-config`, `pip`, `pip3`, etc. pointing to  
`python3.11`, `python3.11-config`, `pip3.11` etc., respectively, are installed into  
    $HOMEBREW_PREFIX/opt/python@3.11/libexec/bin
```

My symlinks were not updated, and I didn't take time to update them so these instructions will use `python3` and `pip3`. I used `rc_local_llm` as the name for my virtual environment. 

2. `python3 -m venv rc_local_llm`
3. `source rc_local_llm/bin/activate`

The flag `-m` runs the library module as a script and terminates option list. TODO: Figure out what that actually means.

> Aside: You may want to update pip3 by running
> `python3 -m pip install --upgrade pip`

Now my shell shows me I'm inside of my venv by prepending `rc_local_llm→`. Inside my venv I install `torch==2.4.0` and `torchvision`. I have to install PyTorch at version 2.4.0 because I'm using an older version of Python3. (':

3. `rc_local_llm→ pip3 install torch==2.4.0 torchvision`

Create a file called `verify_installation.py`

```
import torch
x = torch.rand(5, 3)
print(x)

# For macOS, check if Apple Silicon is available
# There is a version for CUDA
print(torch.backends.mps.is_available())
```

4. `rc_local_llm→ python3 verify_installation.py`

Expected output
```
tensor([[0.3506, 0.7249, 0.6220],
        [0.6687, 0.3183, 0.6792],
        [0.9980, 0.5690, 0.6869],
        [0.5635, 0.7574, 0.7461],
        [0.8516, 0.9433, 0.9584]])
True
```

In Chapter 2.5 you will need `tiktoken`

5. `rc_local_llm→ pip3 install tiktoken`

***

Additional references
* https://formulae.brew.sh/formula/python@3.11#default
* PyTorch for macOS https://pytorch.org/get-started/locally/#macos-version documentation
* VSCode noticed an environment was made and I approved using this env. for this folder