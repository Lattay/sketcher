# What is this ?

__sketcher__ is a python module which may be used to quicly create
littles program (sketches) that produce graphical output.
It is obviously deeply inspired by processing and try to get the same feeling
in the python world. It is different from processing.py in that it has no
dependencies to Java environnement and it use a more Pythonic approach of a
sketch. By the way __sketcher__ does not try to stick to the processing API but
a lot of methods names a the same.

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

# About graphical backend

To produce graphical output __sketcher__ will use several possible backends in
the future. For now only tkinter is implemented but it work well.

A pyglet backend is in progress and tkinter will be finalised soon (only text is not implemented).

# Contribute

Any kind of contribution is welcomed. You could propose a new graphical backend
or extend the functionnalities of sketches. Please contact me if you are
intereseted.
