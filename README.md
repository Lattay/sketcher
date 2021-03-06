# Warning
This project is deprecated.
Due to bugs and incoherency, as well as a relatively poorly though interface I decided to deprecate this project.
A better scoped, better designed version may come later.

# What is this ?

__sketcher__ is a python module which may be used to quickly create littles
program (sketches) that produce graphical output.  It is obviously deeply
inspired by processing and try to get the same feeling in the python world. It
is different from processing.py in that it has no dependencies to Java
environnement and it use a more Pythonic approach of a sketch. By the way
__sketcher__ does not try to stick to the processing API but a lot of methods
names are the same.

# How to install it ?

The simpliest way to install this is to use __pip__.
Run `$ pip3 install sketcher` and that is all.

You could also copy the sketcher folder from this repository and put it in your
sketches directory.

# How to use it ?

A basic sketch consist in a class of arbitrary name having two methods __setup__
and __loop__. The class have to be decorated by the decorator __sketch__ from
the __sketcher__ module. Here is the default empty sketch :
```python3
from sketcher import sketch


@sketch
class Sk:
    def setup(self):
        pass  # Here come the initialisation

    def loop(self):
        pass  # Here come the per-frame actions
```

In the __loop__ and __setup__ methods you have access to all the useful methods
from the __Sketch__ class (thanks to the decorator) to produce graphical output
and more.

Then you can run a sketch like this :
```
$ python3 path/to/your/sketch.py
```

Further explanations are available [here](https://github.com/Lattay/sketcher/tree/master/docs).

# About graphical backend

To produce graphical output __sketcher__ can use different backends.
For now tkinter and pyglet are implemented. The two backends expose roughly
the same features however some differences remains. If you notice any let me
know so I can improve the compatibility.

# Contribute

Any kind of contribution is welcomed. You could propose a new graphical backend
or extend the functionnalities of sketches. Please contact me if you are
intereseted.
