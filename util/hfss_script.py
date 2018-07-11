import sys
import win32com.client
import numpy as np

class HFSS:
    def __init__(self, design_name):
        app = win32com.client.Dispatch("Ansoft.ElectronicsDesktop")
        self.oDesktop = app.GetAppDesktop()

        self._oProject = None
        self._oDesign = None

        self._new_project()
        self._new_hfss_design(design_name)

    def _new_project(self):

        self._oProject = self.oDesktop.NewProject()

    def _new_hfss_design(self, name, solution="Terminal"):

        self._oProject.InsertDesign("HFSS", name, solution, "")
        self._oDesign = self._oProject.SetActiveDesign(name)


    def create_box_conductor(self, x, y, z, dx, dy, dz, name):
        """

        :param x: str mm
        :param y: str mm
        :param z: str mm
        :param dx: str mm
        :param dy: str mm
        :param dz: str mm
        :param name:
        :return:
        """
        oEditor = self._oDesign.SetActiveEditor("3D Modeler")
        x = oEditor.CreateBox(
            [
                "NAME:BoxParameters",
                "XPosition:="	, "{:.0f}um".format(x),
                "YPosition:="		, "{:.0f}um".format(y),
                "ZPosition:="		, "{:.0f}um".format(z),
                "XSize:="		, "{:.0f}um".format(dx),
                "YSize:="		, "{:.0f}um".format(dy),
                "ZSize:="		, "{:.0f}um".format(dz)
            ],
            [
                "NAME:Attributes",
                "Name:="	, name,
                "Flags:="		, "",
                "Color:="		, "(255 128 64)",
                "Transparency:="	, 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"pec\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, False,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False

            ])
        return x

    def create_box_dielectric(self, x, y, z, dx, dy, dz, name):
        """

        :param x: str mm
        :param y: str mm
        :param z: str mm
        :param dx: str mm
        :param dy: str mm
        :param dz: str mm
        :param name:
        :return:
        """
        oEditor = self._oDesign.SetActiveEditor("3D Modeler")

        x = oEditor.CreateBox(
            [
                "NAME:BoxParameters",
                "XPosition:="	, "{:.0f}um".format(x),
                "YPosition:="		, "{:.0f}um".format(y),
                "ZPosition:="		, "{:.0f}um".format(z),
                "XSize:="		, "{:.0f}um".format(dx),
                "YSize:="		, "{:.0f}um".format(dy),
                "ZSize:="		, "{:.0f}um".format(dz)
            ],
            [
                "NAME:Attributes",
                "Name:="	, name,
                "Flags:="		, "",
                "Color:="		, "(204 255 204)",
                "Transparency:="	, 0.8,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"FR4_epoxy\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, True,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False

            ])
        return x

    def create_via(self, x, y, z, radius, height, name):
        oEditor = self._oDesign.SetActiveEditor("3D Modeler")
        x = oEditor.CreateCylinder(
            [
                "NAME:CylinderParameters",
                "XCenter:="	, "{:.0f}um".format(x),
                "YCenter:="		, "{:.0f}um".format(y),
                "ZCenter:="		, "{:.0f}um".format(z),
                "Radius:="		, "{:.0f}um".format(radius),
                "Height:="		, "{:.0f}um".format(height),
                "WhichAxis:="		, "z",
                "NumSides:="		, "0"
            ],
            [
                "NAME:Attributes",
                "Name:="		, name,
                "Flags:="		, "",
                "Color:="		, "(255 128 64)",
                "Transparency:="	, 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"pec\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, False,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False
            ])
        return x

class HFSS_DEBUG(HFSS):
    def __init__(self):
        print("init ansys")

    def _new_project(self):
        print("-function :", sys._getframe().f_code.co_name)


    def _new_hfss_design(self, name, solution="Terminal"):
        print("-function :", sys._getframe().f_code.co_name)
        #print("name = {}, solution = {}".format(name, solution))

    def create_box(self, x, y, z, dx, dy, dz, name):
        print("-function :", sys._getframe().f_code.co_name)
        #print("x = {}, y = {}, z = {}, dx = {}, dy = {}, dz = {}, name = {}".format(x, y, z, dx, dy, dz, name))

    def create_dielectric(self, x, y, z, radius, height, axis, name):
        print("-function :", sys._getframe().f_code.co_name, )
        #print("x = {}, y = {}, z = {}, radius = {}, height = {}, axis = {}, name = {}".format(x, y, z, radius, height, axis, name))

def debug():
    app = HFSS_DEBUG()
    app._new_project()
    app._new_hfss_design("test_design")
    app.create_box("0mm", "0mm", "0mm", "1mm", "1mm", "1mm", "testbox")
    app.create_dielectric("0mm", "0mm", "0mm", "1mm", "1mm", "Z", "testbox")

if __name__ == '__main__':
    debug()