from rosetta import *
rosetta.init()

def calc_ddG(pose,sfxn,resnum,aa):
    native_score=sfxn(pose)
    mutate_pose=mutate_residue(pose,resnum,aa,sfxn)
    pack_rot=PackRotamersMover()
    pack_rot.apply(pose)

    mutant_score=sfxn(mutated_pose)

    return mutant_score - native_score


pose = pose_from_pdb("3gp6.pdb")
add_memb=AddMembraneMover()
add_memb.apply(pose)
init_mem_pos=MembranePositionFromTopology()
init_mem_pos.apply(pose)

sfxn=create_score_function("mpframework_fa_smooth_2014")
ala_mut_ddG=calc_ddG(pose,sfxn,181,'A')
print (ala_mut_ddG)