# Copyright (C) 2023  ETH Zurich, Manuel Kaufmann, Velko Vechev, Dario Mylonopoulos
import os

import numpy as np
import json

from aitviewer.configuration import CONFIG as C
from aitviewer.renderables.point_clouds import PointClouds
from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

if __name__ == "__main__":
    # Load an AMASS sequence and make sure it's sampled at 60 fps. This automatically loads the SMPL-H model.
    # We set transparency to 0.5 and render the joint coordinates systems.
    path = "ACCAD/Female1Running_c3d/C2 - Run to stand_poses.npz"
    c = (149 / 255, 85 / 255, 149 / 255, 0.5)

    with open("../babel_humanml3d_kitml_ori.json") as json_data:
        prompts = json.load(json_data)
        prompt = prompts[path[:-4]]
        annotations = prompt["annotations"]
        annotation0 = annotations[0]
        annotation = annotation0["text"]
        print(annotation)

    seq_amass = SMPLSequence.from_amass(
        npz_data_path=os.path.join(C.datasets.amass, path),  # AMASS Running_motion.npz #Female1Running_c3d/C2 - Run to stand_poses.npz #AMASS Stand_poses (2 close frames)_motion
        fps_out=60.0,
        color=c,
        name="AMASS Running",
        show_joint_angles=True,
        annotation=annotation,
    )


    # Instead of displaying the mesh, we can also just display point clouds.
    #
    # Point clouds do not actually draw triangulated spheres (like the `Spheres` class does). They
    # use a more efficient shader, so that a large amount of points can be rendered (at the cost of not having a proper
    # illumination model on the point clouds).
    #
    # Move the point cloud a bit along the x-axis so it doesn't overlap with the mesh data.
    # Amass data need to be rotated to get the z axis up.
    ptc_amass = PointClouds(seq_amass.vertices, position=np.array([1.0, 0.0, 0.0]), color=c, z_up=True)

    # Display in the viewer.
    v = Viewer()
    v.run_animations = True
    v.scene.camera.position = np.array([10.0, 2.5, 0.0])
    v.scene.add(seq_amass, ptc_amass)
    v.run()
