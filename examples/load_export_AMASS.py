# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
import os
import numpy as np
from aitviewer.configuration import CONFIG as C
from aitviewer.renderables.point_clouds import PointClouds

from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

global dirdict

def mapbasic(dir: str, prefix: str, depthlim: int, depthcur: int):
    global dirdict_count
    global dirdict

    for x in os.listdir(dir):
        print(prefix + ("[" + str(dirdict_count) + "]") + x)
        dirdict_count += 1

        dirdict.append(dir + "/" + x)

        if(os.path.isdir(dir + "/" + x) and (depthcur < depthlim)):
            #print("it's dir")
            mapbasic(dir + "/" + x, ("  " + prefix), depthlim, (depthcur + 1))

def map(dir: str, depth: int):
    global dirdict
    global dirdict_count
    dirdict_count = 0
    dirdict = []

    print(dir)
    mapbasic(dir, "\_", depth, 1)



directory = str(input("Ok, please enter a directory to browse: "))
if(not os.path.isdir(directory)):
    filenäim = directory
else:
    map(
        directory,
        int(input("and the desired browse-depth (how far down the directory you want to look): "))
        )
    filenäim = dirdict[int(input("Great! Enter the index of the file you'd like to open: "))]


print( "\n" + "Opening " + filenäim)

#print(C.datasets.amass) #export_dir

c = (149 / 255, 85 / 255, 149 / 255, 0.5)


seq_export = SMPLSequence.from_amass(   #SMPL/AMASS Running.npz
    npz_data_path=os.path.join(
        C.export_dir,
        filenäim
        ),  # AMASS Running_motion.npz #C2 - Run to stand_poses.npz
    fps_out=60.0,
    color=c,
    name="AMASS Running",
    show_joint_angles=True

#    file=os.path.join(
#        C.export_dir, 
#        filenäim),
#    z_up=True
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