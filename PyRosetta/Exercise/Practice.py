#This is the sample code for Workshops of PyRosetta tutorial
#Created on 2021/12/04 by ZenC2001

from pyrosetta import *
from pyrosetta.toolbox import *
#from pyrosetta.toolbox import get_secstruct
#Can't find this file in my toolbox
init()
pose = pose_from_pdb("1yy8.clean.pdb")

print(pose)

seq = pose.sequence()
print(seq)

total=pose.total_residue()
print(total)

res=pose.residue(500).name()
print(res)

chain=pose.pdb_info().chain(500)
print(chain)

num=pose.pdb_info().number(500)
print(num)

pynum=pose.pdb_info().pdb2pose('C',66)
print(pynum)

#get_secstruct(pose)

phi=pose.phi(500)
print("phi: ",phi)

psi=pose.psi(500)
print("psi: ",psi)

omega=pose.omega(500)
print("omega: ", omega)

res=pose.residue(500).name()
print(res)
mutate_residue(pose, 500, "V")
res=pose.residue(500).name()
print(res)

#Change the phi value#
phi=pose.phi(500)
print(phi)

pose.set_phi(500,90)

phi = pose.phi(500)
print(phi)

'''High energy of protein is not favorable
Easy to collapse or go through other mechanical change
so we have to use the score function to evaluate its energy'''

#score function#
scorefxn = get_fa_scorefxn()
print(scorefxn)

#Empty score function without weight#
scorefxn2 = ScoreFunction()
print(scorefxn2)

ras= pose_from_pdb("6q21.clean.pdb")

scorefxn2.set_weight(pyrosetta.rosetta.core.scoring.ScoreType.fa_atr, 0.005)
print(scorefxn2)

print(scorefxn2(ras))
scoreb4=scorefxn2(ras)
print(scorefxn2.show(ras))
print(ras.energies().show(500))

#relax#
relax=pyrosetta.rosetta.protocols.relax.FastRelax()
relax.set_scorefxn(scorefxn)
relax.apply(pose)
#this will take a long long time to do
print(scorefxn2(ras))
print(scoreb4)
