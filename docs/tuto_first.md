Let start a new sketch. Open a file and put it the following content:
```
from sketcher import sketch


@sketch
class Sk:
    def setup(self):
        pass  # Here come the initialisation

    def loop(self):
        pass  # Here come the per-frame actions
```

This is an empty sketch. If you run the file with `$ python3 myfile.py`
an empty white window will open.

Let see what this file is made of.
The first line is the import statement of the sketcher module. We import
a single element `sketch`. `sketch` is a special function that take
a class in argument, build a sketch from this class and run the sketch.
To use it we use the _decorator_ syntax. It is a feature from python which
mean that `sketch` is called with the class `Sk` as an argument.
The `Sk` class is the important part of the sketch. It define two methods
`setup` and `loop`. `setup` is ran once at the start of the program. Then
`loop` is ran at each frame. You should not implement the `__init__` method
of `Sk` because you may end up messing with the internals. However you can
use `setup` instead of `__init__` to declare new properties.

# Add some output
Thanks to the `sketch` decorator the self object provide several methods to
draw on the canvas. All those methods are defined in the `sketcher.Sketch`
class. Let's use some of them to make our sketch more interesting.

## Set the canvas parameter

First of all we want to change the default size of the canvas.
Just bellow the import statement declare `w` and `h` the width and the height
you want for the canvas.
```
w, h = 800, 500
```

In the setup method we will use these variables to set the size of the canvas.
```
def setup(self):
    self.size(w, h)
```

Now if you run the script you will see that the window size changed according to
`w` and `h`.

Now we want to set the background color. For this sketch we want a black background.

```
def setup(self):
    self.size(w, h)
    self.background('black')
```

[More about colors](./colors.md)

Now we have a beautiful black window but it so empty !

## Draw primitives

The `self` object provide several methods to draw things.
We can use `self.rectangle(leftx, bottomy, width, heigh)` to draw a rectangle from
its bottom-left corner and its dimensions. If `heigh` is ommited it is assumed to be
equal to `width` and we draw a square.

All self methods are described [here](./sketch.md).

For now we will use the line method:
`self.line(x1, y1, x2, y2)`

## Random walk

We will implement a random walk:
At each frame a cursor will select a random direction and make a little
step in this direction.

We need to keep track of the position of the cursor. We will use setup
to create the cursor initial position.
```
def setup(self):
    self.size(w, h)
    self.background('black')

    self.x = w/2
    self.y = h/2
```

`self.x, self.y` is the position of the cursor, it will start at the center
of the canvas.

Now we want to select a random direction at each frame which means generating
a random angle in radians at each call of `loop`.

```
def loop(self):
    theta = 2*self.m.pi*self.rd.random()
```
Here we use two new properties of self that we didn't initialize ourselves.
`self.m` and `self.rd` are respectively shortcuts to the math and random modules
of python.

Now we want our cursor position to go forward of a little step, let say 10 pixels,
in the direction of `theta`

## Start drawing

First we compute the position of the cursor after the step:

```
def loop(self):
    theta = 2*self.m.pi*self.rd.random()
    x1 = (self.x + 10*self.m.cos(theta)) % w
    y1 = (self.y + 10*self.m.sin(theta)) % h
```

We use sinus and cosine to compute the step in x and in y and we use
the modulo (`%`) operator to wrap coordinates like in old school games.

Now we want to draw the step
```
def loop(self):
    theta = 2*self.m.pi*self.rd.random()
    x1 = (self.x + 10*self.m.cos(theta)) % w
    y1 = (self.y + 10*self.m.sin(theta)) % h

    if abs(x1 - self.x) <= 10 and abs(y1 - self.y) <= 10:
        self.line(self.x, self.y, x1, y1)
    
    self.x, self.y = x1, y1
```

We put a condition to make sure that we do not draw a line across the canvas
time the cursor go through a side. Finally we update the cursor position.

Now if you run the script you will see nothing ! But wait, we did not change
the line color, and it is black by default ! Let's fix this.

## Add some colors.

Since we will change the line color it will be nice to change it at each
frame so the drawing will be full of colors !
Lets start with an initial red.

```
def setup(self):
    self.size(w, h)
    self.background('black')

    self.x = w/2
    self.y = h/2
    self.col = [240, 0, 0]
```

Here we specified the color in the 24 bit RGB format. `(0, 0, 0)` is black,
`(255, 0, 0)` is full red, and `(255, 255, 255)` is white.

Now we will set the color at each frame in the same way we did with the position.

```
def loop(self):
    theta = 2*self.m.pi*self.rd.random()
    x1 = (self.x + 10*self.m.cos(theta)) % w
    y1 = (self.y + 10*self.m.sin(theta)) % h

    self.col = [(x + self.rd.random()) % 255 for x in self.col]
    if abs(x1 - self.x) <= 10 and abs(y1 - self.y) <= 10:
        self.line(self.x, self.y, x1, y1)
    
    self.x, self.y = x1, y1
```

And finally we will use this color to draw the line. The sketch recall three
colors at once:
- background color, you can set it with `self.background(mycolor)`
- fill color, the color used to fill shapes, set it with `self.fill_color(mycolor)`
- stroke color, the color used to draw points, lines and the outlines of shapes,
  set it with `self.stroke_color(mycolor)`

By default background is white, stroke color is black and fill color is red.
If you want to draw a shape without outline you can disable it with `self.stroke(False)`
The same goes for fill.

So lets use stroke color to change our step color:
```
def loop(self):
    theta = 2*self.m.pi*self.rd.random()
    x1 = (self.x + 10*self.m.cos(theta)) % w
    y1 = (self.y + 10*self.m.sin(theta)) % h

    self.col = [(x + self.rd.random()) % 255 for x in self.col]
    self.stroke_color(self.col)
    if abs(x1 - self.x) <= 10 and abs(y1 - self.y) <= 10:
        self.line(self.x, self.y, x1, y1)
    
    self.x, self.y = x1, y1
```

And now when you launch the script you should see a colorful pattern drawing
step after step.
But it is so slow !!

## Framerate

By default the framerate is 10 frame per seconds so the random walk is only
doing 10 steps per second. But we can fix that. __sketcher__ allow you to
set the target frame length easily. `self.frame(dt)` set the target length
of a frame to `dt` seconds. However if you use a `dt` to small the sketch
wont be able to keep up and you will probably freeze the windows.
But this sketch is pretty simple and a rate of 1000 frames per seconds 
should be okay.

```
def setup(self):
    self.size(w, h)
    self.background('black')
    self.frame(0.001)

    self.x = w/2
    self.y = h/2
    self.col = [240, 0, 0]
```

Now run and... beautiful !
