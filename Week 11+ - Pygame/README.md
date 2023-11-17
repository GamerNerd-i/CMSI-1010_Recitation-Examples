# Pygame Basics

This is a very brief walkthrough of [how to set up the Pygame library](Installation), and a [list of resources](Resources) that you might find useful for using Pygame to make things.

## Important Concepts

Before you get started even installing Pygame, please check your understanding on the following tools and concepts. They are prevalent across Pygame as a library and its typical use cases, and used often throughout this whole tutorial.

* The terminal (or command-line interface)
* Objects, Classes, and Inheritance
* Functions
* Global and local variables
* Loops

## Installation

Just open your terminal and type one of the following:

```bash
pip install pygame
# OR
pip3 install pygame
```

Once it has finished downloading, make sure it's actually installed by running one of the examples. There are several, but the official Pygame setup tutorial recommends the following:

```bash
python -m pygame.examples.aliens
# OR
python3 -m pygame.examples.aliens
```

If the game starts up, you're good to go!

### Note for Mac Users *Without* Apple Silicon

 ``python3`` and ``python`` (and ``pip``/``pip3``) both refer to some Python version on your computer. If you have a Mac without Apple Silicon, there's a good chance that you have Python 2 *in addition to Python 3* on your computer. ``python`` or ``python2``, and ``pip``, will usually refer to your Python 2 installation, but not always.

You can check which Python is run where with the following commands:

```bash
python --version
python3 --version
```

If ``python --version`` outputs ``Python 3.x.x``, then you're in the clear. Otherwise, you'll have to use ``python3`` to run commands.

### DISCLAIMER

Please note that this is not necessarily how you *should* set up Pygame (or other Python libraries) while coding. Normally, you would use something called a "virtual environment" - but that isn't necessary, and makes things a little bit more complicated than they need to be for now.

If you *really* want to know, ask a TA, or you can try [this tutorial](https://realpython.com/python-virtual-environments-a-primer/). **Please remember, though this is by no means necessary for your final project!**

## Using Pygame

Once you've installed Pygame, bust open your code editor and create a new Python file.

I'll be using [this tutorial code](https://www.pygame.org/docs/) from the official Pygame docs as an introduction to some of the important components of this library.

The first few things you want to put in your document are as following, with explanatory comments:

```python
import pygame # Necessary to use pygame at all

# Set up global variables
## Start all the pygame modules you use in your code.
pygame.init()

## This creates your game window. The tuple inside determines the size, in pixels, of the window. I don't recommend it, but you can leave this blank; it will set your window to the size of your screen.
screen = pygame.display.set_mode((500, 300))

# Not always necessary. pygame.time is used to control framerate and things related to it.
clock = pygame.time.Clock() 

# Typically, all pygame updates are run in a single loop. We use the running variable to maintain and eventually stop it.
running = True 
while running:
    # This loop basically just checks to see if your user exited the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Your code will go here, once you start building!

    # Update the display with any changes you've made.
    pygame.display.flip()

    # limits FPS to 60. Not always necessary.
    clock.tick(60)

# Once your loop is finished (i.e. your game is done), remember to close the pygame modules.
pygame.quit()
```

## Resources

* [Pygame Official Documentation](https://www.pygame.org/docs/)
* [A Newbie Guide to pygame (from the Pygame documentation)](https://www.pygame.org/docs/tut/newbieguide.html)
* [Pygame Official Wiki: Tutorials](https://www.pygame.org/wiki/tutorials)
* Potentially helpful built-in Python modules
  * [math](https://devdocs.io/python/library/math)
  * [random](https://devdocs.io/python/library/random)
* If it's not here, [just Google it!](https://www.google.com/)
