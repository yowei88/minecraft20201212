from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x+1,y,z,63,0,'20201212str','我愛MINECRAFT','也愛python')