"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""
#from os import name

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Object two is a cylinder and cone to be a skyscraper with an antenna at the top.
# ---------------------------------------------------------------------------

# These are my descriptive variables that establish the skyscrapers dimensions and location as well as
# the antennas dimensions.
skyscraper_radius = 3
skyscraper_height = 15
skyscraper_x = 11
skyscraper_z = -12
antenna_radius = 1
antenna_height = 10

#These create the actual geometry and make its values my established variables.
skyscraper = cmds.polyCylinder(
    name="skyscraper",
    radius=skyscraper_radius,
    height=skyscraper_height,
)[0]

#This moves my skyscraper so it isn't clipping through the floor and is sitting on the ground.
cmds.move(skyscraper_x, skyscraper_height / 2.0, skyscraper_z, skyscraper)

#These create the actual geometry and make its values my established variables.
antenna = cmds.polyCone(
    name="antenna",
    radius=antenna_radius,
    height=antenna_height,
)[0]

#This makes my antennas y value the appropriate value to sit flush atop my skyscraper and moves it to
#the appropriate location.
antenna_y = skyscraper_height + antenna_height * 0.5
cmds.move(skyscraper_x, antenna_y, skyscraper_z, antenna)
# ---------------------------------------------------------------------------
# TODO: Add Object 3
#Object 3 is just another building, a midsized one.
# ---------------------------------------------------------------------------

# These are my descriptive variables that establish everything's dimensions and locations.
building_width = 4
building_height = 8
building_depth = 5
building_x = -8
building_z = -1

#These create the actual geometry and make its values my established variables.
building = cmds.polyCube(
    name="building_02",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]

#This moves my building so that it sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 4
# ---------------------------------------------------------------------------
#Object 4 is just another building, a taller one.
# ---------------------------------------------------------------------------

# These are my descriptive variables that establish everything's dimensions and locations.
building_width = 5
building_height = 10
building_depth = 5
building_x = -8
building_z = -8

#These create the actual geometry and assign its values as my established variables.
building = cmds.polyCube(
    name="building_03",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]

#This moves my building so that it sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 5
# ---------------------------------------------------------------------------
#Object 5 is a house with a roof.
# ---------------------------------------------------------------------------

# These are my descriptive variables that establish everything's dimensions and locations.
house_width = 6
house_height = 6
house_depth = 6
house_x = 18
house_z = 12
roof_height = 5
roof_radius = 4.5

#These create the actual geometry and assign its values as my established variables.
house = cmds.polyCube(
    name="house_01",
    width=house_width,
    height=house_height,
    depth=house_depth,
)[0]

#This moves my building so that it sits on the ground plane.
cmds.move(house_x, house_height / 2.0, house_z, house)

#These create the actual geometry and assign its values as my established variables.
roof = cmds.polyCone(
    name="roof_01",
    radius=roof_radius,
    height=roof_height,
)[0]

#This makes my roofs y value the appropriate value to sit flush atop my house and moves it to
#the appropriate location.
roof_y = house_height + roof_height * 0.5
cmds.move(house_x, roof_y, house_z, roof)

# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
