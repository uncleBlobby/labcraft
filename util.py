from ursina import *
from sims import *
import json

# draws slider UI component for variables in solar system model
def initSolarSystemSliders(self):
    self.sliders = list()
    sliderX = ThinSlider(text="X Position", max=5, default=1, x=-.65, y=(0.4*.75), step=0.1)
    self.sliders.append(sliderX)
    sliderX2 = ThinSlider(text="X MOD", max=25, default=1, x=-.65, y=(0.4*.75) - 0.025, step=0.1)
    self.sliders.append(sliderX2)
    sliderY = ThinSlider(text="Y Position", max=5, default=1, x=-.65, y=(0.4*.75) - .05, step=0.1)
    self.sliders.append(sliderY)
    sliderY2 = ThinSlider(text="Y MOD", max=5, default=1, x=-.65, y=(0.4*.75) - .075, step=0.1)
    self.sliders.append(sliderY2)
    sliderZ = ThinSlider(text="Z Position", max=5, default=1, x=-.65, y=(0.4*.75) - .1, step=0.1)
    self.sliders.append(sliderZ)
    sliderZ2 = ThinSlider(text="Z MOD", max=25, default=1, x=-.65, y=(0.4*.75) - .125, step=0.1)
    self.sliders.append(sliderZ2)
    sliderA = ThinSlider(text="SPEED", max=100, default=1, x=-.65, y=(0.4*.75) - .15, step=1)
    self.sliders.append(sliderA)

    for slider in self.sliders:
        slider.min = 0
        slider.dynamic = True
        slider.bg.color = color.black
        slider.label.color = color.black
        slider.scale *= .75
        slider.visible = False

def initCannonSliders(self):
    self.sliders = list()
    sliderX = ThinSlider(text="Launch Angle", max=90, default=45, x=-.65, y=(0.4*.75), step = 1)
    self.sliders.append(sliderX)
    
    for slider in self.sliders:
        slider.visible = False
        slider.dynamic = True
    

def rotateCannon(self):
    self.rotation_z = self.sliders[0].value
    print(self.rotation.z)

def showSliders(self):
    for slider in self.sliders:
        slider.visible = True

def hideSliders(self):
    for slider in self.sliders:
        slider.visible = False

def destroySliders(self):
    for slider in self.sliders:
        destroy(slider)


def save(data):
    print('attempting to save game')
    try:
        os.mkdir("./save")
    except OSError as error:
        print(error)

    file = open("./save/saveFile.json", "w")
    #file.write(json.dumps(dict(data), indent=4, separators=(",", " = ")))
    print('Data is type: ' + str(type(data)))
    print(data)
    file.write(json.dumps(data, indent=0))
    file.close()


def readSceneData():
    itemID = 0
    save_data = {}
    for e in scene.entities:
        save_data[str(itemID) + e.name] = e.__dict__
        print(e.name)
        print(e.__dict__)
        itemID += 1
        #print('\n')
    print(save_data)
    print(type(save_data))
    return save_data

# called once to open output data file, creates it if necessary.
# should rewrite all existing data if it already exists (?) - need test
def createOrOpenDataFile():
    print('writing data to file...')
    try:
        os.mkdir("./data")
    except OSError as error:
        print(error)
    
    file = open("./data/output.txt", "w")
    return file


# called each frame to write the experiment data to output file.
def writeExpDataToFile(outputFile, applePos, deltaT):

    # Should write the position of the apple and the delta time each frame
    # Currently, writes a frame counter instead of delta time.
    # TODO: Fix caller s.t. third argument is frameCounter * deltaT.
    outputFile.write(str(deltaT) + "\t" + str(applePos) + "\n")

# called once experiment is completed, to clean up file IO
def closeExpDataFile(outputFile):

    outputFile.close()
