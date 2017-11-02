from ivisual import scene, sphere

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)
color = (0.1, 0.1, 0.9) # mostly blue
sphere(pos=scene.center, radius=128, color=color)