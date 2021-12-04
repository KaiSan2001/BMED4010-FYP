#This is the sample code for Workshop2 of PyRosetta tutorial
#Created on 2021/12/04 by ZenC2001

from pyrosetta import *
init()
p = pose_from_pdb("1yy8.clean.pdb") #import the pdb file
pymol = PyMOLMover()
pymol.apply(p) #visualize the protein on pymol
for i in range(1,p.total_residue() + 1):
	print(i, "phi =", p.phi(i), "psi =", p.psi(i)) #iterate the parameters
	
