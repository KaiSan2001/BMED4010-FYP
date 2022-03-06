'''
Starting Date: 2022.01.11
Ending Date: Still Processing
Last Editing Date: 2022.03.06
Coder: Chan Kai San
E-mail: u3556373@connect.hku.hk
Description: This programme is designed to construct a pipeline for high-throughput ddG_stability and ddG_binding calculation
             The core kernels of this programme are EvoEF and UniDesign which are developed by Dr. Huang Xiaoqiang in Umich
             Since EvoEF has more accurate predicting power in ddG_stability, EvoEF is employed for the ddG_stability computation
             Since UniDesign is capable for protein <---> nucleic acids binding analysis, UniDesign is harnnessed for the ddG_binding computation
             The result can be used to generate the corresponding Heat Map, and can also be used to perform Correlation Test such as Pearson and Spearman
Reference: 
'''


#----Initialization----#
from copy import copy
import os
import xlwt
import time


#----CopyRight Warning----#
print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
print("#","BaoMi loves Eating WeiLong".center(50),"#")
print("#"," ".center(50),"#")
print("#","No CopyRight at this stage".ljust(50),"#")
print("#","Coding hater from BME".ljust(50),"#")
print("#","Lab of Combinatorial Genetics & Synthetic Biology".ljust(50),"#")
print("#","Schoold of Biomedical Sciences".ljust(50),"#")
print("#","The University of Hong Kong".ljust(50),"#")
print("#"*54) 
print("-----  Usage  -----")
print("o To Optimze the pdb file, you can input: ");print("  OptimizePDB")
print("o To Mutate the pdb file, you can input: ");print("  MutatePDB")
print("o To Predict the ddG_stability, you can input: ");print("  PredictStability")
print("o To Predict the ddG_binding, you can input: ");print("  PredictBinding")
print("o To Analyse the heat map, you can input: ");print("  DDGAnalyse")
#print("o To Delete the Mutant file you created before, you can input: ");print("  RemoveFile")
print("o To get help, you can input: ");print("  Help")
print("o To Quit the programme you can input: ");print("  Quit")
print('-------------------')
pipe=True


#----Function Operation----#
while pipe:
    #----Check the validity of command#
    command_check=["OptimizePDB","MutatePDB","PredictStability","PredictBinding","DDGAnalyse","RemoveFile","Help","help","h","Quit","quit","exit"]
    command=str(input("Please input the function you want to use: "))
    
    if command not in command_check:
        content=("There are something wrong with your input '%s', Please check!"%command)
        print('-'*len(content));print(content);print('-'*len(content))
        print('\n')
    else:
        #----Function working----#

        #----RepairStructure----#
        if command == "OptimizePDB":
            print('-----%s is Working-----'%command)
            pdb=str(input("Please input your pdb file (xxxx.pdb): "))
            try:
                fh = open(pdb)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s'" %pdb)
                print('-'*len(content))
                print(content)
                print("Please check the file name and retry!")
                print('-'*len(content))
                print('\n')
            else:
                #Library File preparation and operation#
                ST = time.time()
                path = os.path.abspath('.')#Recording the absolute path of Pipeline directory
                model_name=pdb[0:4].upper() #Formatting the file name
                Library_name = "%s_Library"%model_name
                path_to_Library = path +"/"+ Library_name
                create_new_Library = ("mkdir %s"%Library_name) #command
                os.system(create_new_Library)
                cp_command = "cp %s %s"%(pdb,path_to_Library)
                os.system(cp_command)
                os.chdir(path_to_Library) #Move to the target sub-directory
                
                #EvoEF RepairStructure#
                mission = ('%s/EvoEF-master/EvoEF --command=RepairStructure --pdb=%s' %(path,pdb))
                print('The Optimization is under processing......Please wait......')
                os.system(mission)
                ET = time.time()
                Current_path = os.path.abspath('.')

                #Output#
                duration = int(ET - ST)
                if duration < 60:
                    content = ('Your optimized structure is saved to %s as %s_Repair.pdb ' %(Current_path,model_name))
                    print('-'*len(content));print("Time taken for optimization is: %ss" %duration);print(content);print('-'*len(content))
                    print('\n')
                    os.chdir(path) #Back to the parental Pipeline directory
                    #print(os.path.abspath('.'))
                    
                else:
                    duration = duration/60
                    content = ('Your optimized structure is saved to %s as %s_Repair.pdb ' %(Current_path,model_name))
                    print('-'*len(content));print("Time taken for optimization is: %.2fmins" %duration);print(content);print('-'*len(content))
                    print('\n')
                    os.chdir(path) #Back to the parental Pipeline directory
                    #print(os.path.abspath('.'))
        

        #----MutatePDB----#
        elif command == "MutatePDB":
            print('-----%s is Working-----'%command)
            print('REMINDER: Optimization MUST be conducted to your WildType pdb file, otherwise the accuracy of results will be affected!')
            print('REMINDER: Please Note That Mutant Files Are Required For This Function!!')
            print('For the format of the Mutant Files, please refer to the ReadMe file in Github')
            pdb=str(input("Please input your pdb file (xxxx_Repair.pdb): "))
            mutate_file=str(input("Please input your mutate file (xxxx_mutants.txt): "))

            #Library File preparation and operation#
            path = os.path.abspath('.')#Recording the absolute path of Pipeline directory
            model_name=pdb[0:4].upper() #Formatting the file name
            Library_name = "%s_Library"%model_name
            path_to_Library = path +"/"+ Library_name

            #Determine whether a sub-directory is existed or not#
            if os.path.exists(path_to_Library) == False:
                print("You haven't Optimized your file yet, please use the 'OptimizePDB' function first")

            else:
                cp_command = "cp %s %s"%(mutate_file,path_to_Library)
                os.system(cp_command)
                os.chdir(path_to_Library) #Move to the target sub-directory
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
                    ST = time.time()
                    mission = ('%s/EvoEF-master/EvoEF --command=BuildMutant --pdb=%s --mutant_file=%s' %(path,pdb,mutate_file))
                    print('The mutation is under processing......Please wait......')
                    os.system(mission)
                    ET = time.time()
                    Current_path = os.path.abspath('.')
                    #Output#
                    duration = int(ET - ST)
                    if duration < 60:
                        content='Your mutant models had been saved in to %s' %Current_path
                        print('-'*len(content));print("Time taken for optimization is: %ss" %duration);print(content);print('-'*len(content))
                        print('\n')
                        os.chdir(path) #Back to the parental Pipeline directory
                        
                    else:
                        duration = duration/60
                        content='Your mutant models had been saved in to %s' %Current_path
                        print('-'*len(content));print("Time taken for optimization is: %.2fmins" %duration);print(content);print('-'*len(content))
                        print('\n')
                        os.chdir(path) #Back to the parental Pipeline directory


        #ddG_Stability Computation#
        elif command == "PredictStability":
            print('-----%s is Working-----'%command)
            print('REMINDER: This Function Can Only Be Used After The "MutatePDB" Function')
            print('Please Note That Mutant Files Are Required For This Function!!')
            print('\n')
            pdb = str(input('Please input your Wild Type protein pdb file (xxxx_Repair.pdb): '))
            mutate_file=str(input("Please input your mutate file (xxxx_mutants.txt): "))
           
            ddG=[]#Construct an empty list to store the computed DDG, the 0th element is the energy of WildType protein
            #Library File preparation and operation#
            path = os.path.abspath('.')#Recording the absolute path of Pipeline directory
            model_name=pdb[0:4].upper() #Formatting the file name
            Library_name = "%s_Library"%model_name
            path_to_Library = path +"/"+ Library_name

            #Determine whether a sub-directory is existed or not#
            if os.path.exists(path_to_Library) == False:
                print("You haven't Optimized your file yet, please use the 'OptimizePDB' function first")

            else:
                cp_command = "cp %s %s"%(mutate_file,path_to_Library)
                os.system(cp_command)
                os.chdir(path_to_Library) #Move to the target sub-directory
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
                    #Calculate the WildType Energy#
                    ST = time.time()
                    print('The ddG is being calculated......Please wait......')
                    mutant_number=len(open(mutate_file,'r').readlines())
                    mission = ('%s/EvoEF-master/EvoEF --command=ComputeStability --pdb=%s' %(path,pdb))
                    result=os.popen(mission).readlines(); score=result[-3];WT_score = score[37:-1]; ddG.append(WT_score); WT_score = float(WT_score)

                    #Calculate the difference in Folding Energy#
                    for i in range(mutant_number):
                        t1=time.time()
                        x=str(i+1).zfill(4)
                        pdbid = pdb[0:4]
                        #Calculate the dG of Mutant#
                        mutant_name = str(pdbid+'_Repair_Model_%s.pdb'%x) #Formatting the file name of mutant
                        mission = ('%s/EvoEF-master/EvoEF --command=ComputeStability --pdb=%s' %(path,mutant_name))
                        result=os.popen(mission).readlines(); score=result[-3]; MT_score = float(score[37:-1])
                        #Calculate the dG of the corresponding wildType#
                        WT_name = str(pdbid+'_Repair_Model_%s_WT.pdb'%x) #Formatting the file name of the mutant's corresponding WT
                        mission = ('%s/EvoEF-master/EvoEF --command=ComputeStability --pdb=%s' %(path,WT_name))
                        result=os.popen(mission).readlines(); score=result[-3]; WTC_score = float(score[37:-1])
                        ddG_sample = str(MT_score - WTC_score)
                        ddG.append(ddG_sample)
                        t2=time.time()
                        print("ddG for %s is calculated and stored! Time cost: %.2f"%(mutant_name,t2-t1))

                    #Output the ddG corresponding to their Mutation#
                    print("Processing the storage file!")
                    wb = xlwt.Workbook()
                    sh = wb.add_sheet('DDG')
                    sh.write(0,0,'Mutation')
                    sh.write(0,1,'DDG')
                    mutation_list = []
                    with open(mutate_file,'r') as f:
                        for mutation in f.readlines():
                            mutation = mutation.strip('\n')
                            mutation_list.append(mutation)
                    for i in range(mutant_number):
                        sh.write(i+1,0, mutation_list[i])
                    for j in range (1,mutant_number+1):
                        sh.write(j,1,float(ddG[j]))
                    file_name=('ddG_Stability_of_%s'%pdbid)
                    wb.save(file_name)
                    ET = time.time()
                    #Output#
                    duration = int(ET - ST)
                    Current_path = os.path.abspath('.')
                    
                    if duration < 60:
                        content='The ddG file "%s" has been saved in to %s' %(file_name,Current_path)
                        print('-'*len(content));print("Time taken for calculating ddG_stability is: %.2fs" %duration);print(content);print('-'*len(content))
                        print('\n')
                        os.chdir(path) #Back to the parental Pipeline directory
                        
                    else:
                        duration = duration/60
                        content='The ddG file "%s" has been saved in to %s' %(file_name,Current_path)
                        print('-'*len(content));print("Time taken for calculating ddG_stability is: %.2fmins" %duration);print(content);print('-'*len(content))
                        print('\n')
                        os.chdir(path) #Back to the parental Pipeline directory




#Note that Since EvoEF doesn't support the analysis for nucleic acid molecules, UniDesign, which is an extension platform of EvoEF2, is employed to do the binding affinity analysis
#This part aims to automate the operation of UniDesign for highthroughput data analysis
        elif command == "PredictBinding":
            print('\n')
            print('-----%s is Working-----'%command)
            print('REMINDER: Please Note That Mutant Files Are Required For This Function!!')
            pdb = str(input('Please input your Wild Type protein pdb file (xxxx.pdb): '))
            mutate_file=str(input("Please input your mutate file (xxxx_mutants.txt): "))
            try:
                fh = open(pdb)
                fh2 = open(mutate_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s' and mutant file: '%s'" %(pdb,mutate_file))
                print('-'*len(content))
                print(content)
                print("Please check the file name and retry!")
                print('-'*len(content))
                print('\n')
            else:
                #Library File preparation and operation#
                ST = time.time()
                path = os.path.abspath('.')#Recording the absolute path of Pipeline directory
                model_name=pdb[0:4].upper() #Formatting the file name
                Library_name = "%s_Binding"%model_name
                path_to_Library = path +"/"+ Library_name
                create_new_Library = ("mkdir %s"%Library_name) #command
                os.system(create_new_Library)
                cp_command = "cp %s %s"%(pdb,path_to_Library) #copy the original pdb into the target directory
                os.system(cp_command)
                cp_command = "cp %s %s"%(mutate_file,path_to_Library) #copy the mutant into the target directory
                os.system(cp_command)
                os.chdir(path_to_Library) #Move to the target sub-directory
                print("To analyse the binding interaction energy between partner pairs, you need to indicate which two partners you are investigating in")
                print("For example, if you want to predict the binding interaction energy between partners 'Cas9-gRNA complex(chain ID A and B)' and 'DNA(chain ID C)', your Partner I is 'AB' and your Partner II is 'C'")
                Partner_I = str(input("Please input the chain/chains ID of the Partner I: "))
                Partner_II = str(input("Please input the chain/chains ID of the Partner II: "))


                #Pre-optimization of the pdb file#
                pdbid = pdb[0:4]
                Repair_command = ('%s/UniDesign-master/UniDesign --command=RepairStructure --pdb=%s'%(path,pdb))
                print("Your file now is being Repaired!")
                os.system(Repair_command) #A file named "xxxx_Repaired.pdb" will occur, it is the structure where only the AA side chains with missing non-hydrogen atoms were repaired and optimized
                Minimize_command = ('%s/UniDesign-master/UniDesign --command=Minimize --pdb=%s_Repaired.pdb'%(path,pdbid))
                os.system(Minimize_command) #A file named "xxx_Repaired_Minimized.pdb" will occur, it is the structure that stays in minimal energy state without steric clashes while its backbone was kept fixed

                #Performing mutation#
                WT_pdb = pdbid+'_Repaired_Minimized.pdb'
                mission = ('%s/UniDesign-master/UniDesign --command=BuildMutant --pdb=%s --mutant_file=%s' %(path,WT_pdb,mutate_file))
                print('The mutation is under processing......Please wait......')
                os.system(mission)

                #Calculate the WildType Binding Energy#
                ddG_binding=[]#Construct an empty list to store the computed ddG_binding, the 0th element is the binding energy of WildType protein
                mission = ('%s/UniDesign-master/UniDesign --command=ComputeBinding --pdb=%s --split_chains=%s,%s' %(path,WT_pdb,Partner_I,Partner_II))
                result=os.popen(mission).readlines(); score=result[-3];WT_score = score[37:-1]; ddG_binding.append(WT_score); WT_score = float(WT_score)

                #Calculate the difference in Binding Energy#
                mutant_number=len(open(mutate_file,'r').readlines())
                for i in range(mutant_number):
                    x=str(i+1).zfill(4)
                    #Calculate the dG of Mutant#
                    mutant_name = str(pdbid+'_Repaired_Minimized_Model_%s.pdb'%x) #Formatting the file name of mutant
                    mission = ('%s/UniDesign-master/UniDesign --command=ComputeBinding --pdb=%s --split_chains=%s,%s' %(path,mutant_name,Partner_I,Partner_II))
                    result=os.popen(mission).readlines(); score=result[-3]; MT_score = float(score[37:-1])
                    ddG_sample = str(MT_score - WT_score)
                    ddG_binding.append(ddG_sample)

                #Output the ddG corresponding to their Mutation#
                wb = xlwt.Workbook()
                sh = wb.add_sheet('ddG')
                sh.write(0,0,'Mutation')
                sh.write(0,1,'ddG_Binding')
                mutation_list = []
                with open(mutate_file,'r') as f:
                    for mutation in f.readlines():
                        mutation = mutation.strip('\n')
                        mutation_list.append(mutation)
                for i in range(mutant_number):
                    sh.write(i+1,0, mutation_list[i])
                for j in range (1,mutant_number+1):
                    sh.write(j,1,float(ddG_binding[j]))
                file_name=('ddG_binding_of_%s'%pdbid)
                wb.save(file_name)
                ET = time.time()
                #Output#
                duration = int(ET - ST)
                Current_path = os.path.abspath('.')
                
                if duration < 60:
                    content='The ddG file "%s" has been saved in to %s' %(file_name,Current_path)
                    print('-'*len(content));print("Time taken for predicting ddG_binding is: %.2fs" %duration);print(content);print('-'*len(content))
                    print('\n')
                    os.chdir(path) #Back to the parental Pipeline directory
                    
                else:
                    duration = duration/60
                    content='The ddG file "%s" has been saved in to %s' %(file_name,Current_path)
                    print('-'*len(content));print("Time taken for predicting ddG_binding is: %.2fmins" %duration);print(content);print('-'*len(content))
                    print('\n')
                    os.chdir(path) #Back to the parental Pipeline directory


        #Call the Help Page#
        elif command == "Help" or command == "help" or command == "h":
            print('-----Help Page-----')
            print("o To Optimze the pdb file, you can input: ");print("  OptimizePDB")
            print("o To Mutate the pdb file, you can input: ");print("  MutatePDB")
            print("o To Predict the ddG_stability, you can input: ");print("  PredictStability")
            print("o To Predict the ddG_binding, you can input: ");print("  PredictBinding")
            print("o To Analyse the heat map, you can input: ");print("  DDGAnalyse")
            #print("o To Delete the Mutant file you created before, you can input: ");print("  RemoveFile")
            print("o To get help, you can input: ");print("  Help")
            print("o To Quit the programme you can input: ");print("  Quit")
            print('-------------------')


        #Quit the programme#
        elif command == "Quit" or command == "quit" or command == "exit":
            print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
            print("#","BaoMi loves Eating WeiLong".center(50),"#")
            print("#"," ".center(50),"#")
            print("#","No CopyRight at this stage".ljust(50),"#")
            print("#","Coding hater from BME".ljust(50),"#")
            print("#","Lab of Combinatorial Genetics & Synthetic Biology".ljust(50),"#")
            print("#","Schoold of Biomedical Sciences".ljust(50),"#")
            print("#","The University of Hong Kong".ljust(50),"#")
            print("#"*54) 
            content='Thank you for your using!'
            print('-'*len(content));print(content);print('-'*len(content))
            pipe = False

'''
        elif command == "RemoveFile":
            print('-----%s is Working-----'%command)
            print('REMINDER: Please use the "RepairStructure" function for your Wild Type protein pdb file, otherwise the accuracy of results will be affected!')
            print('REMINDER: Please Note That Mutant Files Are Required For This Function!!')
            print('For the format of the Mutant Files, please refer to the ReadMe file in Github')
            pdb=str(input("Please input your pdb file you used before (xxxx_Repair.pdb): "))
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
                print('The mutation is under processing......Please wait......')
                path = os.path.abspath('.')
                for i in range(mutant_number):
                    x=str(i+1).zfill(4)
                    pdb_name = str(pdb_id+'_Repair_Model_%s.pdb'%x) #Formatting the file name of mutant
                    mission = ('rm -f %s'%pdb_name)
                    os.system(mission)
                
                
                content='Your mutant models had been removed from %s' %path
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')
'''
