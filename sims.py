from ursina import *

# Sets a constant value for gravity ( -y ).
# Halved here in order to draw out the simulation.
GRAVITY = (-9.8/2)

def oscSim(self):
    self.t += time.dt * self.sliders[6].value
    self.planet.x = (math.cos(self.t) * self.sliders[1].value + self.position.x) * self.sliders[0].value
    self.planet.y = (self.position.y * self.sliders[2].value) / self.sliders[3].value
    self.planet.z = (math.sin(self.t) * self.sliders[5].value + self.position.z) * self.sliders[4].value


def simple_pendulum(self):
    self.pendulum.x = self.position.x + 0.7
    self.pendulum.y = self.position.y
    self.pendulum.z = self.position.z
    self.pendulum.rotation += Vec3(0.5,0,0)

def applyGravity(entity):
    # Checks if entity is currently colliding with anything below itself, if NOT then it applies gravity
    #   - uses entity.scale as a parameter for the ground collision ... 
    #       - TODO: adjust to entity.height somehow...
    check_for_collision_below = raycast(entity.position, (0, -1 * entity.scale.y, 0), ignore=(entity,), distance=0.5)
    if not check_for_collision_below:
        # TODO: GRAVITY should work by modulating a veloctiy, not a position..
        entity.y += GRAVITY * time.dt

def launch(entity):
    #launchAngle = self.rotation.z
    entity.x += -5 * time.dt
    entity.y += (2 * time.dt)