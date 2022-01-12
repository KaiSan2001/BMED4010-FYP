from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.toolbox import *
init("-ignore_unrecognized_res 1 -ex1 -ex2 -flip_HNQ -relax:cartesian -nstruct 200 -crystal_refine -optimization:default_max_cycles 200")
testPose= Pose()
testPose = pose_from_pdb("1BNI.relax.pdb")

from pyrosetta.rosetta.protocols.relax import FastRelax
scorefxn = pyrosetta.create_score_function("ref2015_cart")
relax = pyrosetta.rosetta.protocols.relax.FastRelax()
relax.constrain_relax_to_start_coords(True)
relax.coord_constrain_sidechains(True)
relax.ramp_down_constraints(False)
relax.cartesian(True)
#relax.min_type("dfpmin_armijo_nonmonotone")
relax.min_type("lbfgs_armijo_nonmonotone")#for non-Cartesian scorefunctions use'dfpmin_armijo_nonmonotone'
relax.set_scorefxn(scorefxn)
s0=scorefxn(testPose)
#relax.apply(testPose)
s1=scorefxn(testPose)
#testPose.dump_pdb('3GB1.relax.pdb')
AA=['G','A','L','M','F','W','K','Q','E','S','P','V','I','C','Y','H','R','N','D','T']
ddG=[]
mp=Pose()
for i in AA:
    mp.assign(testPose)
    mutate_residue(mp,52,i)
    s2=scorefxn(mp)
    dg=s2-s1
    ddG.append(dg)

print(ddG)
