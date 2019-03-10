## Install Python 3
__sketcher__ is written in Python 3. You have to install a Python 3 distribution
to make it working.
For linux system use you package manager. For example in Ubuntu and friens:
```
$ sudo apt install python3
```
For windows users, I am not sure that sketcher work since I did not tested however
I think that their shouldn't be any problems as far as you have one of the backend
available. The simplest way to install Python on Windows is to use Miniconda or
Anaconda. Internet will explain this better than me.

Mac users can use
```
$ brew install python
```

## Install sketcher
__sketcher__ is a pure python module which means that to use it you just
have to make sure that your python interpreter can find the source files.

The two next sections explain two possible methods.

### Use pip

This method is the recommended because it allow you to have sketcher available from
any directory is is the best way to install python package anyway.

Make sure you have pip installed by running the command `$ pip3 -V`.
If not install it the way you want. Google will tell you how better than me.

Then run `$ pip3 install sketcher`. Finally you have to install a backend for
graphical output. In version 1.0 the supported backend are tkinter and pyglet.
You can install pyglet with `$ pip3 install pyglet`. Tkinter is often provided 
by default on linux distributions and is also available as a conda package.

### Install from sources

If you want sketcher to be accecible only from one directory you can simply copy the whole
_sketcher_ directory from the gihub repository and put it into you working directory. Then
all python files in this directory would be able to do `from sketcher import sketch`.
