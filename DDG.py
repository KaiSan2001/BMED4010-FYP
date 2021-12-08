'''
Predicting the ddG of single point mutations
2021/12/06-2021/12/08
Reference:https://nbviewer.org/github/RosettaCommons/PyRosetta.notebooks/blob/master/notebooks/15.02-Membrane-Protein-ddG-of-mutation.ipynb
'''

#Initialization#
from pyrosetta import *
from pyrosetta.toolbox import cleanATOM
from pyrosetta.rosetta.protocols.membrane import *

from additional_scripts import predict_ddG
init( extra_options="-mp:lipids:has_pore false")

'''
#Loading the interested protein data#
pose = pose_from_pdb("6aeg.pdb")
cleanATOM("6aeg.pdb")
pose=pose_from_pdb("6aeg.clean.pdb")

#Initialize the spanning topology#
add_memb = AddMembraneMover("from_structure")
add_memb.apply(pose)
'''

#Loading#
pose = pose_from_pdb("3gp6.pdb")
sfxn=create_score_function("franklin2017")
reference_pose = predict_ddG.mutate_residue(pose, 104,"A", 8.0,sfxn)
score_All1 = sfxn.score(reference_pose)

pose_W111 = predict_ddG.mutate_residue(pose, 104, "W", 8.0, sfxn)
score_W111 = sfxn.score(pose_W111)
# Compute the ddG of mutation as mutant_score - native_score (final-initial
ddG = score_W111 - score_A111
print(ddG)