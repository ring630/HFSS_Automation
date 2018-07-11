import numpy as np
from util.hfss_script import HFSS
from util.stackup_manager import Stackup

design_name = "new_design"
model_dx = "2mm"
model_dy = "2mm"
model_x = "-1mm"
model_y = "-1mm"

class SingleVia:
    def __init__(self, stackup_fname):
        self.stackup = Stackup(stackup_fname)


    def run(self):
        self.hfss = HFSS(design_name)

    def create_planes(self):
        for i in np.arange(len(self.stackup.layers)):
            layer = self.stackup.layers[i]
            z = layer.vertical_location
            dz = layer.thickness
            layer = layer.layer
            self.hfss.create_conductor(model_x, model_y, z, model_dx, model_dy, dz, layer)

def debug():
    fname = "stackup.csv"
    SingleVia(fname)


if __name__=="__main__":
    debug()

