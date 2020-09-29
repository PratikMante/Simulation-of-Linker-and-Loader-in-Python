import os 
f=os.stat("prawns.c")
eblocks=200
size=10
filesize=f.st_size
blocks=filesize/size 
if filesize%size != 0:
    blocks=blocks+1 
if eblocks==0:
    print("Memory Full")
if eblocks<blocks:
    print("Insufficient Memory"+"\nAvailable Blocks:"+str(eblocks)+"\nRequired Blocks:"+str(blocks))
else:
    eblocks=eblocks-blocks
    print("Blocks used:"+str(blocks)+"\nBlocks Remaining:"+str(eblocks))