"""
Code Developed by AlbertDaYoungYT
Github: https://github.com/AlbertDaYoungYT

Code Version = 0.0.3

Changes:
- Map Spawns now at world center
- Simplified Functions
- Objects get put in Collections
- Live Updates
"""
import bpy
import time
from math import *
from random import *
from threading import *




baseScale = 100
scaleToRange = 1.5
subdivitions = 2
gridStep = 5
defaultMaxLength = 5
        







def recurLayerCollection(layerColl, collName):
    found = None
    if (layerColl.name == collName):
        return layerColl
    for layer in layerColl.children:
        found = recurLayerCollection(layer, collName)
        if found:
            return found

class CreateBiome:

    def __init__(self, subdivitions, baseScale, scaleToRange, gridStep, defaultMaxLength):
        self.subdivitions = subdivitions
        self.baseScale = baseScale
        self.scaleToRange = scaleToRange
        self.gridStep = gridStep
        self.defaultMaxLength = defaultMaxLength
        
        self.location = []



        self.offset = self.baseScale / self.subdivitions
        self.center = floor(self.baseScale * 0.5)
        


        self.subLocations = []
        for x in range(0, self.subdivitions):
            for y in range(0, self.subdivitions):
                self.subLocations.append([self.offset * x, self.offset * y])

        myColl = bpy.data.collections.new('Base')
        bpy.context.scene.collection.children.link(myColl)
        myColl = bpy.data.collections.new('Walls')
        bpy.context.scene.collection.children.link(myColl)
        myColl = bpy.data.collections.new('Lights')
        bpy.context.scene.collection.children.link(myColl)

        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Base')
        bpy.context.view_layer.active_layer_collection = layerColl
        
        self.master_coll = bpy.context.view_layer.layer_collection
        self.current_coll = recurLayerCollection(self.master_coll, bpy.context.collection.name)

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
                    try:
                        bpy.ops.mesh.primitive_cube_add(location=(x - self.center,y - self.center,z), scale=(c1, c2, 2 * 0.5))
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    except Exception:
                        rang += 1

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
                    try:
                        bpy.ops.mesh.primitive_cube_add(location=(x - self.center,y - self.center,z), scale=(c1, c2, 2 * 0.5))
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    except Exception:
                        rang += 1

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
                    try:
                        bpy.ops.mesh.primitive_cube_add(location=(x - self.center,y - self.center,z), scale=(c1, c2, 2 * 0.5))
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    except Exception:
                        rang += 1

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
                    try:
                        bpy.ops.mesh.primitive_cube_add(location=(x - self.center,y - self.center,z), scale=(c1, c2, 2 * 0.5))
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                    except Exception:
                        rang += 1
    
    def GenerateLights(self, amount):
        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Lights')
        bpy.context.view_layer.active_layer_collection = layerColl
        biomeLocations = []
        rang = amount
        for x in range(rang):
            x = randrange(0 - (floor(self.baseScale * 0.5)), floor(self.baseScale * 0.5), 2)
            y = randrange(0 - (floor(self.baseScale * 0.5)), floor(self.baseScale * 0.5), 2)
            z = 2 + 0.1
            if [x, y, z] in biomeLocations:
                rang += 1
            else:
                biomeLocations.append([x, y, z])
                bpy.ops.mesh.primitive_cube_add(location=(x,y,z), scale=(0.5, 0.5, 0.1 * 0.5))
    
    def GenerationThread(self):
        for subs in self.subLocations:
            self.location = subs
            biome = choice([1, 2, 3, 4])
            print("Generating Biome id:{}".format(biome))
            if biome == 1:
                self.OpenSpaceBiome()
            elif biome == 2:
                self.LargeOpenSpaceBiome()
            elif biome == 3:
                self.SingleObjectBiome()
            elif biome == 4:
                self.RandomObjectBiome()
            print("Chunk {} with Biome id:{} Created. {} Remaning".format(self.subLocations.index(subs), biome, len(self.subLocations) - self.subLocations.index(subs) - 1))
            print("")
        
        for obj in bpy.data.collections["Walls"].all_objects:
            mat = bpy.data.materials.get("Wall")
            if obj.data.materials:
                # assign to 1st material slot
                obj.data.materials[0] = mat
            else:
                # no slots
                obj.data.materials.append(mat)
        
        self.GenerateLights(200)
        
        for obj in bpy.data.collections["Lights"].all_objects:
            mat = bpy.data.materials.get("Light")
            if obj.data.materials:
                # assign to 1st material slot
                obj.data.materials[0] = mat
            else:
                # no slots
                obj.data.materials.append(mat)
        
        for obj in bpy.data.collections["Base"].all_objects:
            mat = bpy.data.materials.get("Floor")
            if obj.data.materials:
                # assign to 1st material slot
                obj.data.materials[0] = mat
            else:
                # no slots
                obj.data.materials.append(mat)
        
        for obj in bpy.data.collections["Walls"].all_objects:
            mat = bpy.data.materials.get("Wall")
            if obj.data.materials:
                # assign to 1st material slot
                obj.data.materials[0] = mat
            else:
                # no slots
                obj.data.materials.append(mat)
    
    def run(self):
        startTime = time.time()
               
        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Base')
        bpy.context.view_layer.active_layer_collection = layerColl
        
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -0.25), scale=(self.baseScale * 0.5, self.baseScale * 0.5, 0.5 * 0.5))
        print("Base Created.")
        print("Generating Borders...")

        pos = [[self.center + self.center, self.center, self.baseScale * 0.5, 0.1 * 0.5],
               [self.center - self.center, self.center, self.baseScale * 0.5, 0.1 * 0.5],
               [self.center, self.center + self.center, 0.1 * 0.5, self.baseScale * 0.5],
               [self.center, self.center - self.center, 0.1 * 0.5, self.baseScale * 0.5]]
               
        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Walls')
        bpy.context.view_layer.active_layer_collection = layerColl
               
        for cord in pos:
            bpy.ops.mesh.primitive_cube_add(location=(cord[0] - self.center, cord[1] - self.center, 0.5), scale=(cord[3], cord[2], 2 * 0.5))
        
        print("Borders Generated")

        print("")

        print("Starting Generation of {} Chunks, approx {} Objects".format(self.subdivitions * self.subdivitions, ((self.baseScale * self.scaleToRange) * len(self.subLocations)) * 0.5))
        
        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Walls')
        bpy.context.view_layer.active_layer_collection = layerColl
        
        self.GenerationThread()


        print("Done ;)")
        endTime = time.time()
        print("Generation took {} Seconds".format(endTime - startTime))

Biomes = CreateBiome(subdivitions, baseScale, scaleToRange, gridStep, defaultMaxLength)
Biomes.run()
