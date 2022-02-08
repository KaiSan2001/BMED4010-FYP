#Python
from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.teaching import *
from pyrosetta.toolbox import *
#Core Includes
from rosetta.core.kinematics import MoveMap
from rosetta.core.kinematics import FoldTree
from rosetta.core.pack.task import TaskFactory
from rosetta.core.pack.task import operation
from rosetta.core.simple_metrics import metrics
from rosetta.core.select import residue_selector as selections
from rosetta.core import select
from rosetta.core.select.movemap import *

#Protocol Includes
from rosetta.protocols import minimization_packing as pack_min
from rosetta.protocols import relax as rel
from rosetta.protocols.antibody.residue_selector import CDRResidueSelector
from rosetta.protocols.antibody import *
from rosetta.protocols.loops import *
from rosetta.protocols.relax import FastRelax

init('-use_input_sc -ignore_unrecognized_res -ignore_zero_occupancy false -relax:default_repeats 5 -ex1 -ex2 -fa_max_dis 9.0')

pose = pose_from_pdb('1BPI.clean.pdb') #Here I used 1BPI for benchmarking

scorefxn = pyrosetta.create_score_function("ref2015_cart")
SF = get_score_function()
relax = pyrosetta.rosetta.protocols.relax.FastRelax()
relax.constrain_relax_to_start_coords(True)
relax.coord_constrain_sidechains(True)
relax.ramp_down_constraints(False)
relax.cartesian(True)
relax.min_type("lbfgs_armijo_nonmonotone") #for non-Cartesian scorefunctions, 'dfpmin_armijo_nonmonotone' should be used instead
relax.set_scorefxn(scorefxn)
WTE = SF(pose)
relax.apply(pose) #Refine the structure of the protein by Cartesian relax
OE = SF(pose)
mutate_residue(pose,44,'G') #Mutate the 44th residue from N to G, the experimental ddG should be -4.7
ME = SF(pose)

tf = TaskFactory()
tf.push_back(operation.InitializeFromCommandline())
tf.push_back(operation.RestrictToRepacking())
packer = pack_min.PackRotamersMover(SF)
packer.task_factory(tf)


if not os.getenv("DEBUG"):
    packer.apply(pose)  #Optimize the rotamer
PE = SF(pose)
print('WT Energy: ', WTE)
print('Relaxed Energy: ',OE)
print('Mutant Energy: ',ME)
print('Packer Energy: ',PE)
print('DDG: ',str(PE-OE))