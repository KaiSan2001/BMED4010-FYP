'''
Starting Date: 2022.01.11
Ending Date: 2022.01.12
Coder: Chan Kai San
E-mail: u3556373@connect.hku.hk
Description: This pipeline is designed to automate the usage of EvoEF, by simply input the sematic command, high-throughput mutation can
             realized and the corresponding ddG can be calculated and stored. The ddG data can then be tested by Pearson Coefficient test
             and other statistical analysis
'''



#----Initialization----#
import os
import xlwt


#----User Manual----#
print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
print("#","EvoEF Automation Pipeline".center(50),"#")
print("#"," ".center(50),"#")
print("#","No CopyRight at this stage".ljust(50),"#")
print("#","Coding hater from BME".ljust(50),"#")
print("#","Lab of Combinatorial Genetics & Synthetic Biology".ljust(50),"#")
print("#","Schoold of Biomedical Sciences".ljust(50),"#")
print("#","The University of Hong Kong".ljust(50),"#")
print("#"*54) 
print("\n") # Adjust the space to show the user manual
print("Usage");print("-----")
print("o To Repair the pdb file, you can input: ");print("RepairStructure")
print("\n")
print("o To Mutate the pdb file, you can input: ");print("MutatePDB")
print("\n")
print("o To Calculate the ddG, you can input: ");print("CalculateDDG")
print("\n")
print("o To Analyse the heat map, you can input: ");print("DDGAnalyse")
print("\n")
print("o To Quite the pipeline, you can input: ");print("Quit")
print("\n")
pipe=True

#----Function Operation----#
while pipe:
    #----Check the validity of command#
    command_check=["RepairStructure","MutatePDB","CalculateDDG","DDGAnalyse","Quit"]
    command=str(input("Please input the function you want to use: "))
    
    if command not in command_check:
        content=("There are something wrong with your input '%s', Please check!"%command)
        print('-'*len(content));print(content);print('-'*len(content))
        print('\n')
    else:
        #----Function working----#

        #----RepairStructure----#
        if command == "RepairStructure":
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
                mission = ('./EvoEF --command=RepairStructure --pdb=%s' %pdb)
                os.system(mission)
                print('The repairing is under processing......Please wait......')
                model_name=pdb[0:4].upper()
                content = ('Your repaired structure is saved as %s_Repair.pdb' %model_name)
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')
        
        #----MutatePDB----#
        elif command == "MutatePDB":
            print('-----%s is Working-----'%command)
            print('REMINDER: Please use the "RepairStructure" function for your Wild Type protein pdb file, otherwise the accuracy of results will be affected!')
            print('REMINDER: Please Note That Mutant Files Are Required For This Function!!')
            print('For the format of the Mutant Files, please refer to the ReadMe file in Github')
            pdb=str(input("Please input your pdb file (xxxx_Repair.pdb): "))
            mutate_file=str(input("Please input your mutate file (xxxx_mutants.txt): "))
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
                mission = ('./EvoEF --command=BuildMutant --pdb=%s --mutant_file=%s' %(pdb,mutate_file))
                os.system(mission)
                print('The mutation is under processing......Please wait......')
                path = os.path.abspath('.')
                content='Your mutant models had been saved in to %s' %path
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')
        
        elif command == "CalculateDDG":
            print('-----%s is Working-----'%command)
            print('REMINDER: This Function Can Only Be Used After The "MutatePDB" Function')
            print('Please Note That Mutant Files Are Required For This Function!!')
            print('\n')
            WT = str(input('Please input your Wild Type protein pdb file (xxxx_Repair.pdb): '))
            mutate_file=str(input("Please input your mutate file (xxxx_mutants.txt): "))
           
            ddG=[]#Construct an empty list to store the computed DDG, the 0th element is the energy of WildType protein
            try:
                fh = open(WT)
                fh2= open(mutate_file)
            except IOError:
                content = ("Error!! File cannot be opened at pdb:'%s' and mutant_file:'%s' " %(WT,mutate_file))
                print('-'*len(content))
                print(content)
                print("Please check the file name and retry!")
                print('-'*len(content))
                print('\n')
            else:
                #Calculate the WildType Energy#
                print('The ddG is being calculated......Please wait......')
                mutant_number=len(open(mutate_file,'r').readlines())
                mission = ('./EvoEF --command=ComputeStability --pdb=%s' %WT)
                result=os.popen(mission).readlines(); score=result[-3];WT_score = score[37:-1]; ddG.append(WT_score); WT_score = float(WT_score)

                #Calculate the Mutant Energy#
                for i in range(mutant_number):
                    x=str(i+1).zfill(4)
                    pdbid = WT[0:4]
                    pdb_name = str(pdbid+'_Repair_Model_%s.pdb'%x) #Formatting the file name of mutant
                    mission = ('./EvoEF --command=ComputeStability --pdb=%s' %pdb_name)
                    result=os.popen(mission).readlines(); score=result[-3]; MT_score = float(score[37:-1])
                    ddG_sample = str(MT_score - WT_score)
                    ddG.append(ddG_sample)
                #Output the ddG corresponding to their Mutation#
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
                    sh.write(j,1,ddG[j])
                file_name=('DDG_of_%s'%pdbid)
                wb.save(file_name)
                path = os.path.abspath('.')
                content='The ddG file "%s" has been saved in to %s' %(file_name,path)
                print('-'*len(content));print(content);print('-'*len(content))
                print('\n')


        elif command == "Quit":
            print("#"*54) #space before and after the information --> total 1+1+50+1+1=54
            print("#","EvoEF Automation Pipeline".center(50),"#")
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




