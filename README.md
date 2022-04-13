# LabCraft
![screenshot](https://raw.githubusercontent.com/uncleBlobby/labcraft/cannon/screenshots/labcraft-screen1.png)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

A Digital Physics Lab in a Blocky Voxel World

Forked from: [https://github.com/trevortomesh/labcraft](https://github.com/trevortomesh/labcraft)

A research project undertaken in partial fulfillment of the requirements for CS290 at the [University of Regina](www.uregina.ca)

## Description

LabCraft is a tool for the development of virtual physics simulations.  It is a Minecraft clone using the Ursina Engine written in Python.  The tool is intended to be a framework useful for the exploration of online lab development, with physics taken as an example.  The intent is not to be limited to physics alone, and the framework is free to use for anyone interested in exploring the subject matter -- or just noodling around.  It has been a particularly interesting study project, not because I am particularly interested in rudimentary physics demonstrations, but rather for the computer science angle.  It is a fun way to learn to use Python and the Ursina Engine, and explore the interdisciplinary connection between software, education, and video games.

Be warned, the code in this repo and the documentation along with it is amateur and hacky at best.  My educational background is in philosophy, not software.  So there.

## Manifest

```
/.vscode/           -> config file to disable linting
/__pycache__/       -> should've been ignored, whoops
/assets/            -> contains models, textures, and object files for various entities
/screenshots/       -> screenshot file for cash money repo purposes
.gitignore          -> self-explanatory
README.md           -> YOU ARE HERE
assetTest.py        -> contains tests for ensuring compatibility of new assets
forces.py           -> currently unused (TODO: generalize gravity force in newton experiment and move here)
labcraft-master.py  -> main LabCraft file.  Contains all entities and simulations, used as development playground
labcraft-newton.py  -> stripped down LabCraft instance for running the newton gravity simulation
labcraft-wave.py    -> currently unused (TODO: implement wave function generator for illustrative purposes)
sims.py             -> contains code that is used to control the simulation parameters
util.py             -> contains code for LabCraft utilities (ie: UI sliders to control simulation parameters, data output functions, etc.)
```

## Installation (Linux)

Windows instructions coming soon!

## Dependencies:
Labcraft uses python 3.6:
```bash
sudo apt-get install python3
```

Labcraft is built on the Ursina engine (https://www.ursinaengine.org)
To install Ursina use pip:
``` bash
pip install ursina

```

## Running:
To run the playground mode with all models and features accessible:
```bash
python3 labcraft-master.py
```

To run a particular simulation instance (currently only newtonian gravity simulation):
```bash
python3 labcraft-newton.py
```

## Controls:
The controls are relatively straightforward first-person controls, typical of Minecraft and other games:
```
w -> move forward
a -> move left
s -> move backward
d -> move right

mouse axis y -> look up and down
mouse axis x -> look left and right

numbers 1 through 8 (with the exception of 4, for reasons) will "pick a block" to lay... like minecraft creative mode.
1 -> grass block
2 -> stone block
3 -> brick block
5 -> solar system simulation block (middle click on solar system block to bring up slider controls, esc to close them)
6 -> pendulum simulation block (sliders TODO)
7 -> projectile simulation (it's fun to launch projectiles, who are you to judge until you try for yourself)
8 -> cannon simulation block (very much a work in progress.  middle click for slider to control cannon angle)

right mouse click -> destroy targeted block
left mouse click -> place chosen block
```

At present, you don't really know what block you're "holding" unless you know what number you've pressed most recently.  This seems like a bug, but really it is a feature because this is educational content and it is tailored specifically this way to help improve your memory and recollection.  However, there are rumours that a UI inventory system is in the works.  Stay Tuned!

## Project Status:

LabCraft is currently under active development, with updates likely to come in the spring/summer 2022.  Contributions are welcome, so feel free to take it for a spin.  At present, the project is in an early alpha state and users should keep that in mind--that being said, we welcome your expertise.

For a more "polished" product with a different spin, check out [PhysLab](https://colin-price.wbs.uni.worc.ac.uk/PhysLab/PhysLab.htm).

## Support and Issues:

If you have any problems, please feel free to reach out.  Send me an [email](mailto:dc.christianson@gmail.com)!

## Acknowledgements:

Thanks to Peter Amland, aka [pokepetter](https://github.com/pokepetter/ursina) for working on developing the Ursina Engine!  Awesome framework, would recommend 10/10.  Join the Ursina Engine [discord](https://discord.gg/C8aaC4jSCd), say hi, and follow the development LIVE.

Thanks to [Dr. T](https://github.com/trevortomesh) for taking me on as a research candidate and facilitating the ongoing development of this project.  Without your help, none of this would have come to be.  Also appreciate the insights that have helped lead me back to some philosophical readings I haven't touched in almost a decade.  I hope I can continue to pursue them, and I could sure use some more of your help.  Oh yeah I've read almost 3/4 of your thesis by now! 🤓

Thanks to Earl aka Edge-Guard aka [quickMaffs44](https://github.com/quickMaffs44) for building out the Windows implementation of LabCraft, and working out some brilliant user-interface features.  Also thank you for being there and making sure I didn't have to be alone with Dr. T!


