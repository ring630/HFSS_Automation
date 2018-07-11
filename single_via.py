import numpy as np
from util.hfss_script import HFSS
from util.stackup_manager import Stackup

design_name = "new_design"
model_dx = 2000
model_dy = 2000
model_x = -1000
model_y = -1000
VIA_200 = {"FHS": 200, "PLATING_THICKNESS": 25, "ANNULAR_RING":150}
VIA_250 = {"FHS": 250, "PLATING_THICKNESS": 25, "ANNULAR_RING":150}


class ViaStack:

    def __init__(self, via_stack_name, z_loc, dz, ):
        self.radius = via_stack_name["FHS"]/2 + self.PLATING_THICKNESS
        self.pad_size = self.radius*2 - self.PLATING_THICKNESS*2 + 150e-6*2

    def via_stack(self, via_stack_name, from_layer, to_layer):
        pass

class SingleVia:

    def __init__(self, stackup_fname):
        self.stackup = Stackup(stackup_fname)

    def run(self):
        self.hfss = HFSS(design_name)
        self.create_planes()
        self.create_via(0, 0, 1, 16, 1, 14, VIA_200)

    def create_planes(self):
        self.hfss.create_box_dielectric(model_x, model_y, 0, model_dx, model_dy, self.stackup.BOARD_THICKNESS, "DIEL")

        for i in np.arange(len(self.stackup.layers)):
            layer = self.stackup.layers[i]
            z = layer.zloc
            dz = layer.thickness
            layer_name = layer.layer
            usage = layer.usage

            if usage == "PLANE":
                self.hfss.create_box_conductor(model_x, model_y, z, model_dx, model_dy, dz, layer_name)


    def create_via(self, x, y, drill_start_layer, drill_end_layer, sig_in, sig_out, via_stack_name):
        layers = self.stackup.layers
        
        drill_radius = via_stack_name["FHS"]/2 + via_stack_name["PLATING_THICKNESS"]
        pad_radius = via_stack_name["FHS"]/2 + via_stack_name["ANNULAR_RING"]
        drill_start = layers[drill_start_layer*2-2].zloc
        #print(layers[drill_end_layer * 2 - 2].thickness)
        drill_height = layers[drill_end_layer * 2 - 2].zloc - layers[drill_start_layer * 2 - 2].zloc# + layers[drill_end_layer * 2 - 2].thickness
        sig_in_zloc = layers[sig_in * 2 - 2].zloc
        sig_in_thickness = layers[sig_in * 2 - 2].thickness
        sig_out_zloc = layers[sig_out * 2 - 2].zloc
        sig_out_thickness = layers[sig_out * 2 - 2].thickness

        print(drill_radius, pad_radius, drill_start, drill_height)
        self.hfss.create_via(0, 0, drill_start, drill_radius, drill_height, "")
        self.hfss.create_via(0, 0, sig_in_zloc, pad_radius, sig_in_thickness, "")
        self.hfss.create_via(0, 0, sig_out_zloc, pad_radius, sig_out_thickness, "")



def debug():
    fname = "stackup.csv"
    hfss = SingleVia(fname)
    hfss.run()


if __name__=="__main__":
    debug()

