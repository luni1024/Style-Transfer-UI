# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
import os
import numpy as np
from aitviewer.configuration import CONFIG as C
from aitviewer.renderables.point_clouds import PointClouds

from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer


v = Viewer()
v.scene.camera.position = np.array([10.0, 2.5, 0.0])
seq_export = SMPLSequence.from_npz(file=os.path.join(C.export_dir, "SMPL/AMASS Running.npz"), z_up=True)
ptc_export = PointClouds(seq_export.vertices, position=np.array([1.0, 0.0, 0.0]), z_up=True)
v.scene.add(seq_export, ptc_export)
v.run()