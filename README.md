# LabCraft
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
A Digital Physics Lab in a Blocky Voxel World
Forked from: [https://github.com/trevortomesh/labcraft](https://github.com/trevortomesh/labcraft)
A research project undertaken to fulfill part of the requirements for CS290 at the [University of Regina](www.uregina.ca)

## Description

LabCraft is a tool for the development of virtual physics simulations.  It is a Minecraft clone using the Ursina Engine written in Python.  The tool is intended to be a framework useful for the exploration of online lab development, with physics taken as an example.  The intent is not to be limited to physics alone, and the framework is free to use for anyone interested in exploring the subject matter -- or just noodling around.  It has been a particularly interesting study project, not because I am particularly interested in rudimentary physics demonstrations, but rather for the computer science angle.  It is a fun way to learn to use Python and the Ursina Engine, and explore the interdisciplinary connection between software, education, and video games.

Be warned, the code in this repo and the documentation along with it is amateur and hacky at best.  My educational background is in philosophy, not software.  So there.

## Manifest

```
/assets/            -> contains models, textures, and object files for various entities
assetTest.py        -> contains tests for ensuring compatibility of new assets
forces.py           -> currently unused (TODO: generalize gravity force in newton experiment and move here)
labcraft-master.py  -> main LabCraft file.  Contains all entities and simulations, used as development playground
labcraft-newton.py  -> stripped down LabCraft instance for running the newton gravity simulation
labcraft-wave.py    -> currently unused (TODO: implement wave function generator for illustrative purposes)
sims.py             -> contains code that is used to control the simulation parameters
util.py             -> contains code for LabCraft utilities (ie: UI sliders to control simulation parameters, data output functions, etc.)
```


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
To run simply:
```bash
python3 labcraft.py
```

## Manifest:
- README.md:
  The file you are currently reading.

- labcrafy.py:
  The main labcraft code.

- assetTest.py:
  A little script to test new models and textures.

- sims.py:
  Methods that control the various simulations in the world. Might change
  this later as there becomes more simulations.

- assets:
  Folder that contains all of the models, textures and audio files.

