from mcpi.minecraft import Minecraft
import random,time
mc = Minecraft.create()
pos = mc.player.getPos()
while True:
 x=pos.x + random.uniform(-20,20)
 y=pos.y+30
 z=pos.z+random.uniform(-20,20)
 mc.spawnEntity(x,y,z,20)
 time.sleep(0.1)