# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
import os
import numpy as np
from aitviewer.configuration import CONFIG as C
from aitviewer.renderables.point_clouds import PointClouds

from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

global dirlist

def mapdirhelper(dir: str, prefix: str, depthlim: int, depthcur: int):
    global dirlist

    dirlist = os.listdir(dir)
    direnum = enumerate(dirlist)
    
    for index, file in direnum:
        print(prefix + "[" + str(index) + "]" + file)

def mapdir(dir: str, depth: int):
    print(dir)
    mapdirhelper(dir, "", depth, 1)

file_dir = os.path.realpath(os.path.dirname(__file__))
Styletransfer_dir = os.path.split(file_dir)[0]
export_dir = os.path.join(Styletransfer_dir, "export")   # this approach ensures one does not need to be in the `examples`-directory to open this file
examples_dir = os.path.join(Styletransfer_dir, "examples")
#print("file_dir: " + file_dir)                    # <- useful for debugging
#print("Styletransfer_dir: " + Styletransfer_dir)  # <- useful for debugging
#print("export_dir: " + export_dir)                # <- useful for debugging
#print("examples_dir: " + examples_dir)            # <- useful for debugging
os.chdir(examples_dir)

directory = os.path.join(export_dir, "AMASS")
mapdir(directory, 1)
filenäim = dirlist[int(input("Please enter the index of the file you'd like to open: "))]


print( "\n" + "Opening " + filenäim)
#print("\n" + "from: " + os.path.join(Styletransfer_dir, filenäim))     # <- useful for debugging

c = (149 / 255, 85 / 255, 149 / 255, 0.5)

seq_export = SMPLSequence.from_amass(
    npz_data_path=os.path.join(
        Styletransfer_dir,
        filenäim
        ),
    fps_out=60.0,
    color=c,
    name="AMASS Running",
    show_joint_angles=True
    )

ptc_export = PointClouds(
    seq_export.vertices,
    position=np.array([1.0, 0.0, 0.0]),
    color=c,
    z_up=True
    )

v = Viewer()
v.run_animations = True
v.scene.camera.position = np.array([10.0, 2.5, 0.0])
v.scene.add(seq_export, ptc_export)
v.run()