# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
import os
import numpy as np
from aitviewer.configuration import CONFIG as C
from aitviewer.renderables.point_clouds import PointClouds

from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

def mapdirhelper(dir: str, prefix: str):
    dirlist = os.listdir(dir)
    direnum = enumerate(dirlist)
    
    for index, file in direnum:
        print(f"{prefix} [ {str(index)} ] {file}")

    return dirlist

def mapdir(dir: str):
    print(dir)
    return mapdirhelper(dir, "")

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
filename = mapdir(directory)[int(input("Please enter the index of the file you'd like to open: "))]


print( "\n" + "Opening " + filename)
dir_to_open = os.path.join(directory, filename)
print("\n" + "from: " + dir_to_open)     # <- useful for debugging

c = (149 / 255, 85 / 255, 149 / 255, 0.5)

seq_export = SMPLSequence.from_amass(
    npz_data_path=dir_to_open,
    fps_out=60.0,
    color=c,
    name="AMASS Running",
    show_joint_angles=True,
    z_up=False
    )

ptc_export = PointClouds(
    seq_export.vertices,
    position=np.array([1.0, 0.0, 0.0]),
    color=c,
    z_up=False
    )

v = Viewer()
v.run_animations = True
v.scene.camera.position = np.array([10.0, 2.5, 0.0])
v.scene.add(seq_export, ptc_export)
v.run()
