from asyncore import read
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sims import *
from util import * 
from forces import *

window.borderless = False

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
tree_texture  = load_texture('assets/trunk_block2.png')
leaf_texture  = load_texture('assets/leaf_block.png')


punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    
    # escape keypress will breakout mouse control from first person view
    if held_keys['escape']: mouse.locked = False
    # ` keypress will return first person mouse lock
    if held_keys['`']: mouse.locked = True
 
    # if player falls through the map, return to starting point.
    if player.position.y < -10:
        
        player.y = 1
        player.x = 1
        player.z = 1

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5)


    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)

# Ball served as the template class for the 'apple' object used in the
# Newton Gravity Simulation
class Ball(Entity):
    def __init__(self, position = (0, 0, 0), yOffset = (0, 10, 0), direction = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position + yOffset,
            direction = direction,
            model = 'sphere',
            collider = 'sphere',
            color = color.red,
            scale = 1.0)
        
    
    def update(self):
        #if held_keys['g']:
        applyGravity(self)

class Apple(Entity):
    def __init__(self, position = (0, 0, 0), yOffset = (0, 10, 0), direction = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position + yOffset,
            direction = direction,
            model = 'sphere',
            collider = 'sphere',
            color = color.red,
            scale = 0.65,
            dataFrameCounter = 0)
        
    
    def update(self):
        # TODO: Reorganize architecture s.t. experiment doesn't stop
        #       prematurely.  Currently, if you let go of the keypress
        #       partway through the drop, it will stop and the sim.
        #       will not run to completion.
        # Fix:  Likely can use a sentinel variable to run a while loop
        #       for the intended duration of the simulation by initializing
        #       the loop and then escaping the loop when the apple height 
        #       reaches the y value of the ground (0).
        # Currently:
        #   On each update, the apple listens for a keypress.
        #   Key: g will trigger the gravity simulation and write the
        #   experiment data to an output file.
        # Status: Not yet implemented.
        if held_keys['g']:
            # TODO: Third argument passed should be frameCounter * deltaTime.
            # Fix:  Multiply the deltaTime each frame by the total number of 
            #       frames that pass since the start of the experiment.
            #       This shows the total time taken over the course of the sim.
            # Currently:
            #   On each update, the data written to the file is as follows:
            #   {simTime}      {apple y position}
            #   simTime is rounded to 4 decimal places.
            # Status: DONE.
            simTime = round((self.dataFrameCounter * time.dt), 4)
            writeExpDataToFile(outputFile, self.position.y, simTime)
            applyGravity(self)
            self.dataFrameCounter += 1

# terrainGen function generates the platform.
def terrainGen():
    for z in range(20):
        for x in range(20):
            voxel = Voxel(position = (x,0,z))
    
    treeGen()

# treeGen function generates the tree.
def treeGen():
    # TODO: Condense these loops to reduce some repitition in the codebase.
    # Currently:
    #   Functions but is hella ugly.  The tree should be shorter, perhaps.
    for y in range(8):
        voxel = Voxel(position = (5, y, 5), texture = tree_texture)
    
    for z in range(4, 7):
        for x in range(4, 7):
            voxel = Voxel(position = (x, 8, z), texture = leaf_texture)
    
    for z in range(3, 8):
        for x in range(3, 8):
            voxel = Voxel(position = (x, 9, z), texture = leaf_texture)
    for z in range(3, 8):
        for x in range(3, 8):
            voxel = Voxel(position = (x, 10, z), texture = leaf_texture)
    
    for z in range(4, 7):
        for x in range(4, 7):
            voxel = Voxel(position = (x, 11, z), texture = leaf_texture)
    
    apple = Apple((7, 8, 3), (0, 0, 0))



terrainGen()

player = FirstPersonController()
sky = Sky()
hand = Hand()

# Creates the output data file and opens it, or opens it and
# overwrites existing data.
outputFile = createOrOpenDataFile()

app.run()