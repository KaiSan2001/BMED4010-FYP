'''
Starting Date: 2022.01.31
Ending Date: Still Processing
Last Editing Date: 2022.02.13 --Fix the bug that cannot perform multiple mutation
                              --Fix some textual description errors
Coder: Chan Kai San
E-mail: u3556373@connect.hku.hk
Description: This script is designed to calculate the delta-delta G for protein mutation via PyRosetta, the input protein file will be firstly cleaned
             and go through the cartesian fast relax, the relaxed file will be used to perform mutation.

Reference: -

'''

#Initialization#
Reminder = 'The PyRosetta is initializing, Please Wait!!!'
print('-'*len(Reminder));print(Reminder);print('-'*len(Reminder));print('\n')
from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.teaching import *
from pyrosetta.toolbox import *
from rosetta.core.kinematics import MoveMap
from rosetta.core.kinematics import FoldTree
from rosetta.core.pack.task import TaskFactory
from rosetta.core.pack.task import operation
from rosetta.core.simple_metrics import metrics
from rosetta.core.select import residue_selector as selections
from rosetta.core import select
from rosetta.core.select.movemap import *
from rosetta.protocols import minimization_packing as pack_min
from rosetta.protocols import relax as rel
from rosetta.protocols.antibody.residue_selector import CDRResidueSelector
from rosetta.protocols.antibody import *
from rosetta.protocols.loops import *
from rosetta.protocols.relax import FastRelax
import os
import sys
import time
import xlwt
init('-use_input_sc -ignore_unrecognized_res -ignore_zero_occupancy false -relax:default_repeats 5 -ex1 -ex2 -fa_max_dis 9.0')
print('\n')

Reminder = 'PyRosetta had been initilizaed successfully!!! '
print('-'*len(Reminder));print(Reminder);print('Please Enjoy!');print('-'*len(Reminder))

#----CopyRight Warning----#
print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
print("#","PyRosetta ddG Calculator".center(50),"#")
print("#"," ".center(50),"#")
print("#","No CopyRight at this stage".ljust(50),"#")
print("#","Coding hater from BME".ljust(50),"#")
print("#","Lab of Combinatorial Genetics & Synthetic Biology".ljust(50),"#")
print("#","Schoold of Biomedical Sciences".ljust(50),"#")
print("#","The University of Hong Kong".ljust(50),"#")
print("#"*54) 
print("User Manual");print("-----")
print("o To download the pdb file from RCSB directly, you can input: ");print("DownloadPDB")
print("\n")
print("o To clean the pdb file you already have, you can input: ");print("CleanPDB")
print("\n")
print("o To Relax the file you cleaned already, you can input: ");print("RelaxPDB")
print("\n")
print("o To Mutate the pdb file and calculate ddG, you can input: ");print("MutatePDB")
print("\n")
print("o To Delete the Mutant file you created before, you can input: ");print("RemoveFile")
print("\n")
print("o To get help, you can input: ");print("Help")
print("\n")
print("o To Quite the pipeline, you can input: ");print("Quit")
print("\n")
Working=True

while Working:
    #----Check the validity of command#
    command_check=["DownloadPDB","CleanPDB","RelaxPDB","MutatePDB","RemoveFile","Help","help","h","Quit","quit","exit",'Energy']
    command=str(input("Please input the function you want to use: "))

    if command not in command_check:
            content=("There are something wrong with your input '%s', Please check!"%command)
            print('-'*len(content));print(content);print('-'*len(content))
            print('\n')
    else:
        #----Function working----#
        if command == "DownloadPDB":
            print('-----%s is Working-----'%command)
            print("REMINDER: Clean the PDB file is very important, the non-canonical amino acids and hetatms may affect the computational results!!!")
            print("REMINDER: This function can help you generate a cleaned PDB file directly")
            pdb_id=str(input("Please input the ID of your PDB file (If you want to download 2GBI.pdb, input 2gbi or 2GBI): ")).upper()
            PDB = pose_from_rcsb(pdb_id)
            pdb_file = pdb_id+'.pdb'         
            cleanATOM(pdb_file)
            path = os.path.abspath('.')
            file = pdb_id+'.clean.pdb'
            content=("Your PDB file had been cleaned and saved in to %s as '%s'" %(path,file))
            mission = ('rm -f %s' %pdb_file)
            os.system(mission)
            print('-'*len(content));print(content);print('-'*len(content))
            print('\n')

        elif command == "CleanPDB":
            print('-----%s is Working-----'%command)
            print("REMINDER: Clean the PDB file is very important, the non-canonical amino acids and hetatms may affect the computational results!!!")
            pdb_file = str(input("Please input the PDB file name that you want to clean (If you want to clean 2GBI.pdb, input 2GBI.pdb)"))
            try:
                f = open(pdb_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s'" %pdb_file)
                print('-'*len(content))
                print(content)
                print("Please check the file name (upper-case or lower-case) and retry!")
                print('-'*len(content))
                print('\n')
            else:
                cleanATOM(pdb_file)
                path = os.path.abspath('.')
                file = pdb_file[0:4]+'clean.pdb'
                content=("Your PDB file had been cleaned and saved in to %s as '%s'" %(path,file))
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')
        
        elif command == "RelaxPDB":
            print('-----%s is Working-----'%command)
            print("REMINDER: Please make sure the file had been cleaned, otherwise the file might not conform to PyRosetta standards and be loaded successfully")
            print("REMINDER: Note that at this stage, only the Cartesian_Fast_Relax is supported")
            pdb_file = str(input("Please input the PDB file that you want to relax (If you want to relax 2GBI.clean.pdb, input 2GBI.clean.pdb): "))
            
            #Input File#
            try:
                f = open(pdb_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s'" %pdb_file)
                print('-'*len(content))
                print(content)
                print("Please check the file name (upper-case or lower-case) and retry!")
                print('-'*len(content))
                print('\n')
            else:
                #Pose Preparation#
                pose = pose_from_pdb(pdb_file)
                processingPose = Pose () #Create a pose object to hold the pdb information
                processingPose.assign(pose)

                #Cartesian Relax Initilization#
                scorefxn = pyrosetta.create_score_function("ref2015_cart")
                SF = get_score_function()
                relax = pyrosetta.rosetta.protocols.relax.FastRelax()
                relax.constrain_relax_to_start_coords(True)
                relax.coord_constrain_sidechains(True)
                relax.ramp_down_constraints(False)
                relax.cartesian(True)
                relax.min_type("lbfgs_armijo_nonmonotone") #for non-Cartesian scorefunctions, 'dfpmin_armijo_nonmonotone' should be used instead
                relax.set_scorefxn(scorefxn)

                #Relaxation Apply#
                Energyb4Relax = SF(processingPose)
                ST = time.time() #Record the moment of starting point
                relax.apply(processingPose)
                ID = pdb_file[0:4]
                name = (ID + '_relax.pdb')
                processingPose.dump_pdb(name)
                ET = time.time() #Record the moment of ending point
                EnergyafterRelax = SF(processingPose)
                print('The energy before relax is: ',Energyb4Relax)
                print('The energy after relax is: ',EnergyafterRelax)
                #Output#
                duration = int(ET - ST)
                if duration < 60:
                    path = os.path.abspath('.')
                    content=("Your PDB file had been relaxed and saved in to %s as '%s'" %(path,name))
                    print('-'*len(content));print("Time taken for conducting Cartesian_Fast_Relax is: %ss" %duration);print(content);print('-'*len(content))
                    print('\n')
                    
                else:
                    duration = duration / 60
                    path = os.path.abspath('.')
                    content=("Your PDB file had been relaxed and saved in to %s as '%s'" %(path,name))
                    print('-'*len(content));print("Time taken for conducting Cartesian_Fast_Relax is: %.2fmins"%duration);print(content);print('-'*len(content))
                    print('\n')



        elif command == "Energy":
            SF = get_score_function()
            pdb_file = str(input("Please input the PDB file that you want to calculate (If you want to relax 2GBI.clean.pdb, input 2GBI.clean.pdb): "))
            pose = pose_from_pdb(pdb_file)
            print('The energy is: ',SF(pose))




        elif command == "MutatePDB":
            print('-----%s is Working-----'%command)
            print("REMINDER: Please make sure the input file had been relaxed, otherwise the result might be incorrect!!!")
            print("REMINDER: Please write your mutation file in official format!!!")
            pdb_file = str(input("Please input the PDB file that you want to mutate (If you want to mutate '2GBI_relax.pdb', input '2GBI_relax.pdb'): "))
            mutate_file = str(input("Please input the mutate file that you want to perform (If you want to use 'Mutants.txt', input 'Mutants.txt'): "))
            pdb_id = pdb_file[0:4]
            ST = time.time()
            #Input File#
            try:
                f = open(pdb_file)
                f1= open(mutate_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s' and mutant_file:'%s' " %(pdb_file,mutate_file))
                print('-'*len(content))
                print(content)
                print("Please check the file name and retry!")
                print('-'*len(content))
                print('\n')
            else:
                #Rotamer Optimization Initialization#
                TF = TaskFactory()
                TF.push_back(operation.InitializeFromCommandline())
                TF.push_back(operation.RestrictToRepacking())
                packer = pack_min.PackRotamersMover()
                packer.task_factory(TF)


                #File Preparation#
                relaxPose = pose_from_pdb(pdb_file)
                scorefxn = get_score_function()
                WTEnergy = scorefxn(relaxPose)
                Cartesian_ddG=[] #create a list to store the ddG
                Cartesian_ddG.append(str(WTEnergy))
                Mutation_List=[] #create a list to store the mutation type

                #Mutation#
                
                with open(mutate_file,'r') as Mutantfile:
                    count = 1
                    for Mutations in Mutantfile.readlines():
                        processingPose = relaxPose.clone()
                        Mutations = Mutations.strip()
                        Mutation_List.append(Mutations)
                        Mutations = Mutations.split(',')  #Formulate the mutant file into PyRosetta manner
                        
                        #Mutate the PDB according to the mutants indicated each line#
                        for Pointmutation in Mutations:

                            #Eliminating the ';' in the end of each line
                            if ';' in Pointmutation:
                                Pointmutation = Pointmutation[0:-1] #Eliminate the ';' at the end of each line
                            chainID = Pointmutation[1] #Get the chain ID
                            PDBposition = int(Pointmutation[2:-1]) #Get the mutate position
                            MutantID = Pointmutation[-1] # Get the desired residue
                            Poseposition = processingPose.pdb_info().pdb2pose(chainID,PDBposition) #Convert the pdb number into pose number
                            #print(chainID, PDBposition, Poseposition)
                            mutate_residue(processingPose,Poseposition,MutantID) #Perform the mutation, note that the rotamers are not optimized
                        
                        #Looping selection#
                        compare_pose = processingPose.clone() #record the mutated pose before packing
                        Energy4checking = scorefxn(compare_pose) #record the energy of the most optimized sample
                        for i in range(10):
                            loopPose = processingPose.clone() #Initialize the Pose object
                            if not os.getenv('DEBUG'):
                                packer.apply(loopPose)
                                EnergyafterPacking = scorefxn(loopPose ) #record the energy after packing
                                if EnergyafterPacking < Energy4checking: #if packing makes more optimal then let the latest packing be comparing object
                                    compare_pose = loopPose.clone()
                                    Energy4checking = EnergyafterPacking
                        
                        #File output#
                        EnergyafterPacking = scorefxn(compare_pose) #Get the energy score of the most optimized file
                        ddg = str( EnergyafterPacking - WTEnergy)
                        Cartesian_ddG.append(ddg)
                        MutantFile = ('%s_Mutant_%s.pdb'%(pdb_id,count))
                        compare_pose.dump_pdb(MutantFile)
                        print('\n')
                        count += 1
                
                #Cartesian_DDG storage#
                Cartesian_DDG = xlwt.Workbook()
                sh = Cartesian_DDG.add_sheet('DDG')
                sh.write(0,0,'Mutation')
                sh.write(0,1,'DDG')
                for i in range(len(Mutation_List)):
                    sh.write(i+1,0, Mutation_List[i])
                for j in range (1,len(Mutation_List)+1):
                    sh.write(j,1,Cartesian_ddG[j])
                file_name=('Cartesian_DDG_of_%s'%pdb_id)
                Cartesian_DDG.save(file_name)
                ET = time.time()
                #Output#
                duration = int(ET - ST)
                if duration < 60:
                    path = os.path.abspath('.')
                    content="The PyRosetta Cartesian DDG has been saved in to %s as '%s'"%(path,file_name)
                    print('-'*len(content));print("Time taken for conducting DDG computation is: %ss" %duration);print(content);print('-'*len(content))
                    print('\n')
                    
                else:
                    duration = duration / 60
                    path = os.path.abspath('.')
                    content="The PyRosetta Cartesian DDG has been saved in to %s as '%s'"%(path,file_name)
                    print('-'*len(content));print("Time taken for conducting DDG computation is: %.2fmins"%duration);print(content);print('-'*len(content))
                    print('\n')


        elif command == "RemoveFile":
            print('-----%s is Working-----'%command)
            print('REMINDER: Please Note That Mutant Files Are Required For This Function!!')
            print('For the format of the Mutant Files, please refer to the ReadMe file in Github')
            pdb=str(input("Please input your pdb file you used before (xxxx_relax.pdb): "))
            mutate_file=str(input("Please input your mutate file you used before (xxxx_mutants.txt): "))
            try:
                fh = open(pdb)
                fh2= open(mutate_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s' and mutant_file:'%s' " %(pdb,mutate_file))
                print('-'*len(content))
                print(content)
                print("Please check the file name and retry!")
                print('-'*len(content))
                print('\n')
            else:
                pdb_id=pdb[0:4]
                mutant_number=len(open(mutate_file,'r').readlines())
                print('The files are removing......Please wait......')
                path = os.path.abspath('.')
                for i in range(1,mutant_number+1):
                    
                    pdb_name = str(pdb_id+'_Mutant_%s.pdb'%i) #Formatting the file name of mutant
                    mission = ('rm -f %s'%pdb_name)
                    os.system(mission)
                
                
                content='Your mutant models had been removed from %s' %path
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')




        elif command == "Help" or command == "help" or command == "h":
            print("User Manual");print("-----")
            print("o To download the pdb file from RCSB directly, you can input: ");print("DownloadPDB")
            print("\n")
            print("o To clean the pdb file you already have, you can input: ");print("CleanPDB")
            print("\n")
            print("o To Relax the file you cleaned already, you can input: ");print("RelaxPDB")
            print("\n")
            print("o To Mutate the pdb file and calculate ddG, you can input: ");print("MutatePDB")
            print("\n")
            print("o To Delete the Mutant file you created before, you can input: ");print("RemoveFile")
            print("\n")
            print("o To get help, you can input: ");print("Help")
            print("\n")
            print("o To Quite the pipeline, you can input: ");print("Quit")
            print("\n")



        elif command == "Quit" or command == "quit" or command == "exit":
            print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
            print("#","PyRosetta ddG Calculator".center(50),"#")
            print("#"," ".center(50),"#")
            print("#","No CopyRight at this stage".ljust(50),"#")
            print("#","Coding hater from BME".ljust(50),"#")
            print("#","Lab of Combinatorial Genetics & Synthetic Biology".ljust(50),"#")
            print("#","Schoold of Biomedical Sciences".ljust(50),"#")
            print("#","The University of Hong Kong".ljust(50),"#")
            print("#"*54) 
            content='Thank you for your using!'
            print('-'*len(content));print(content);print('-'*len(content))
            Working = False