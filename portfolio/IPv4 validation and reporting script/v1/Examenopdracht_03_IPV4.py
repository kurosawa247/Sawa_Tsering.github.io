import os

def count_fout():
    DataExamen_Dirs= r"..\resultaten.txt"
    resultaten = open(DataExamen_Dirs,"a")
    cwd=os.getcwd()
    alle_dir=cwd.split("\\")
    laast_dir=alle_dir[-1]
    titel="Bij de map "+laast_dir+" :\n\n"
    resultaten.writelines(titel)
    lijst_dirs = os.listdir()
    laste_fout_nummer=0

    for Data_teller in range(len(lijst_dirs)-1):
        Data_Dirs= "DATA_"+str(Data_teller)
        if Data_teller >=1:
            os.chdir(r"..")
            os.chdir(Data_Dirs)
        else:   
            os.chdir(Data_Dirs)
        lijst_files = os.listdir()
        for Files_teller in range(1):
            for IP_Files_teller in range(len(lijst_files)):
                file_naam="IPV4_"+str(IP_Files_teller)+".txt"
                file_ip= open(file_naam)
                lijst_ip_Add=file_ip.readlines()
                lijn_nummer=0
                einde_fout_nummer=0
                for ip_add in lijst_ip_Add :   
                    lijn_nummer+=1
                    ip_add = ip_add.rstrip('\n')  
                    delen= ip_add.split(".")                         
                    fout_nummer=0               
                    for IP_delen_teller in range(len(delen)):
                        if int(delen[IP_delen_teller]) > 255:
                            fout_nummer+=1
                        if fout_nummer>=1:
                            einde_fout_nummer+=fout_nummer
                            fout="Foute nummer in stuk "+str(IP_delen_teller+1)+" op lijn "+str(lijn_nummer) + " in bestand "+file_naam+" in map "+Data_Dirs+".\n"
                            resultaten.writelines(fout)
                            fout_nummer=0 
                file_ip.close()
                if einde_fout_nummer>=1:
                    laste_fout_nummer+=einde_fout_nummer
    if laste_fout_nummer>1:
        conclusie="\nEr zijn in totaal "+str(laste_fout_nummer)+" fouten gevonden.\n\n"
        resultaten.writelines(conclusie)
    elif laste_fout_nummer==1:
        conclusie="\nEr is slechts "+str(laste_fout_nummer)+" fout gevonden.\n\n"
        resultaten.writelines(conclusie)
    else:
        no_fout_conclusie="Er zijn geen fouten gevonden.\n\n"
        resultaten.writelines(no_fout_conclusie)

    resultaten.close()

os.chdir(r"DATA_EXAMEN_60")
count_fout()

os.chdir(r"..\..\..\Examenopdracht_03_IPV4\DATA_EXAMEN_81")
count_fout()

os.chdir(r"..\..\..\Examenopdracht_03_IPV4\DATA_EXAMEN_7")
count_fout()

os.chdir(r"..\..\..\Examenopdracht_03_IPV4\DATA_EXAMEN")
count_fout()