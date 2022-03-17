"""
Code Developed by AlbertDaYoungYT
Github: https://github.com/AlbertDaYoungYT

Code Version = 0.0.1
"""
import bpy
import time
from math import *
from random import *
startTime = time.time()




baseScale = 250
scaleToRange = 2
subdivitions = 3
gridStep = 5
defaultMaxLength = 5



center = floor(baseScale * 0.5)
offset = baseScale / subdivitions

subLocations = []
for x in range(0, subdivitions):
    for y in range(0, subdivitions):
        subLocations.append([offset * x, offset * y])
        


class CreateBiome:
    def __init__(self, sub, baseScale, scaleToRange, location, gridStep, offset, defaultMaxLength):
        self.sub = sub
        self.baseScale = baseScale
        self.scaleToRange = scaleToRange
        self.location = location
        self.gridStep = gridStep
        self.offset = offset
        self.defaultMaxLength = defaultMaxLength

    def OpenSpaceBiome(self):
        biomeLocations = []
        rang = floor(self.baseScale * self.scaleToRange)
        floor0 = floor(self.location[0] + self.offset)
        floor1 = floor(self.location[1] + self.offset)
        for x in range(rang):
            x = randrange(floor(self.location[0]), floor0, self.gridStep)
            y = randrange(floor(self.location[1]), floor1, self.gridStep)
            z = 1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                c1 = choice([0.1, self.defaultMaxLength]) * 0.5
                c2 = choice([0.1, self.defaultMaxLength]) * 0.5
                if c1 == self.defaultMaxLength * 0.5 and c2 == self.defaultMaxLength * 0.5:
                    rang += 1
                else:
                    biomeLocations.append([x, y, z])
                    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(c1, c2, 2 * 0.5))
                    ob = bpy.context.active_object
                    mat = bpy.data.materials.get("Wall")
                    if ob.data.materials:
                        # assign to 1st material slot
                        ob.data.materials[0] = mat
                    else:
                        # no slots
                        ob.data.materials.append(mat)

    def LargeOpenSpaceBiome(self):
        biomeLocations = []
        rang = floor(self.baseScale / 4)
        floor0 = floor(self.location[0] + self.offset)
        floor1 = floor(self.location[1] + self.offset)
        for x in range(rang):
            x = randrange(floor(self.location[0]), floor0, self.gridStep)
            y = randrange(floor(self.location[1]), floor1, self.gridStep)
            z = 1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                c1 = choice([0.1, self.defaultMaxLength]) * 0.5
                c2 = choice([0.1, self.defaultMaxLength]) * 0.5
                if c1 == self.defaultMaxLength * 0.5 and c2 == self.defaultMaxLength * 0.5:
                    rang += 1
                else:
                    biomeLocations.append([x, y, z])
                    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(c1, c2, 2 * 0.5))
                    ob = bpy.context.active_object
                    mat = bpy.data.materials.get("Wall")
                    if ob.data.materials:
                        # assign to 1st material slot
                        ob.data.materials[0] = mat
                    else:
                        # no slots
                        ob.data.materials.append(mat)

    def SingleObjectBiome(self):
        biomeLocations = []
        rang = self.baseScale
        floor0 = floor(self.location[0] + self.offset)
        floor1 = floor(self.location[1] + self.offset)
        for x in range(rang):
            x = randrange(floor(self.location[0]), floor0, self.gridStep)
            y = randrange(floor(self.location[1]), floor1, self.gridStep)
            z = 1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                c1 = choice([0.1, self.defaultMaxLength]) * 0.5
                c2 = choice([0.1, self.defaultMaxLength]) * 0.5
                if c1 == self.defaultMaxLength * 0.5 and c2 == self.defaultMaxLength * 0.5 or c1 == 0.05 and c2 == 0.05:
                    rang += 1
                else:
                    biomeLocations.append([x, y, z])
                    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(c1, c2, 2 * 0.5))
                    ob = bpy.context.active_object
                    mat = bpy.data.materials.get("Wall")
                    if ob.data.materials:
                        # assign to 1st material slot
                        ob.data.materials[0] = mat
                    else:
                        # no slots
                        ob.data.materials.append(mat)

    def RandomObjectBiome(self):
        biomeLocations = []
        rang = self.baseScale
        floor0 = floor(self.location[0] + self.offset)
        floor1 = floor(self.location[1] + self.offset)
        for x in range(rang):
            x = randrange(floor(self.location[0]), floor0)
            y = randrange(floor(self.location[1]), floor1)
            z = 1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                c1 = choice([0.1, self.defaultMaxLength * 2]) * 0.5
                c2 = choice([0.1, self.defaultMaxLength * 2]) * 0.5
                if c1 == (self.defaultMaxLength * 2) * 0.5 and c2 == (self.defaultMaxLength * 2) * 0.5:
                    rang += 1
                else:
                    biomeLocations.append([x, y, z])
                    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(c1, c2, 2 * 0.5))
                    ob = bpy.context.active_object
                    mat = bpy.data.materials.get("Wall")
                    if ob.data.materials:
                        # assign to 1st material slot
                        ob.data.materials[0] = mat
                    else:
                        # no slots
                        ob.data.materials.append(mat)
    
    def GenerateLights(self, amount):
        biomeLocations = []
        rang = amount
        floor0 = floor(self.location[0] + self.offset)
        floor1 = floor(self.location[1] + self.offset)
        for x in range(rang):
            x = randrange(floor(self.location[0]), floor0, 2)
            y = randrange(floor(self.location[1]), floor1, 2)
            z = 2 + 0.1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                biomeLocations.append([x, y, z])
                bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(0.5, 0.5, 0.1 * 0.5))
                ob = bpy.context.active_object
                mat = bpy.data.materials.get("Light")
                if ob.data.materials:
                    # assign to 1st material slot
                    ob.data.materials[0] = mat
                else:
                    # no slots
                    ob.data.materials.append(mat)
        
    

bpy.ops.mesh.primitive_cube_add(location=(center, center, -0.25), scale=(baseScale * 0.5, baseScale * 0.5, 0.5 * 0.5))
ob = bpy.context.active_object
mat = bpy.data.materials.get("Floor")
if ob.data.materials:
    # assign to 1st material slot
    ob.data.materials[0] = mat
else:
    # no slots
    ob.data.materials.append(mat)
print("Base Created.")
print("Generating Borders...")

pos = [[center + center, center, baseScale * 0.5, 0.1 * 0.5],
       [center - center, center, baseScale * 0.5, 0.1 * 0.5],
       [center, center + center, 0.1 * 0.5, baseScale * 0.5],
       [center, center - center, 0.1 * 0.5, baseScale * 0.5]]
       
for cord in pos:
    bpy.ops.mesh.primitive_cube_add(location=(cord[0], cord[1], 0.5), scale=(cord[3], cord[2], 2 * 0.5))
    ob = bpy.context.active_object
    mat = bpy.data.materials.get("Wall")
    if ob.data.materials:
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

print("Borders Generated")

print("")

print("Starting Generation of {} Chunks, approx {} Objects".format(subdivitions * subdivitions, ((baseScale * scaleToRange) * len(subLocations)) * 0.5))

locations = []
rang = floor(baseScale * scaleToRange)

for subs in subLocations:
    Biome = CreateBiome(subdivitions, baseScale, scaleToRange, subs, gridStep, offset, defaultMaxLength)
    biome = choice([1, 2, 3, 4])
    print("Generating Biome id:{}".format(biome))
    if biome == 1:
        Biome.OpenSpaceBiome()
    elif biome == 2:
        Biome.LargeOpenSpaceBiome()
    elif biome == 3:
        Biome.SingleObjectBiome()
    elif biome == 4:
        Biome.RandomObjectBiome()
    print("Generating Lights for Biome id:{}".format(biome))
    Biome.GenerateLights(200)
    print("Chunk {} with Biome id:{} Created. {} Remaning".format(subLocations.index(subs), biome, len(subLocations) - subLocations.index(subs) - 1))
    print("")


print("Done ;)")
endTime = time.time()
print("Generation took {} Seconds".format(endTime - startTime))
