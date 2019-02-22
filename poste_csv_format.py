import os
import csv

def get_text_files():
    txt_files_list = []
    for textfile in os.listdir():
        filename, ext = os.path.splitext(textfile)
        if ext == ".txt":
            txt_files_list.append(textfile)
    return txt_files_list

def fix_format(textfile):
    ''' riformatta il file csv in input nel formato accettato da cedhouse
        e salva il file con l'iban come nome
        d[5] = spese negative
        d[6] = versamenti positivi
        '''
    try:
        with open(textfile, "rt", encoding = 'utf8') as file_csv:
            csvfile = file_csv.read()
    except IOError:
        print (f"Could not read file {textfile}")
        return
    
    fixed = ["DATA CONTABILE;DATA VALUTA;CODICE CAUSALE;DESCRIZIONE;IMPORTO;DIVISA\n"]
    rows = csvfile.splitlines()
    try:
        iban = rows[0]
        fields = rows[1]
        movimenti = rows[2:-1]
    except:
        print(f"Il file {textfile} non proviene dalle poste, o comunque contiene meno di due righe\n")
        return
    for movimento in movimenti:
        new_row = ""
        d = movimento.split(";")
        for i in (0, 1, 2, 3):
            new_row += d[i] + ";"
        if d[5] == "":
            new_row += d[6] + ";EUR\n"
        else:
            new_row += "-" + d[5] + ";EUR\n"
        fixed += [new_row]
    '''fixed contiene le righe aggiustate, procedi a salvare'''
    iban = iban.split(";")[0]
    if diz_iban:
        filename = diz_iban[iban] + ".csv"
    else:
        filename = iban + ".csv"
    save_csv = "".join(fixed)
    with open(filename, "w") as file:
        file.write(save_csv)
        
    return filename



if __name__ == "__main__":
    print("SCRIPT DA UTILIZZARE NELLA CARTELLA DI LAVORO \nSARANNO FORMATTATI TUTTI I FILE .TXT OTTENUTI DAL SITO DELLE POSTE")
    input("Premere INVIO per procedere, CHIUDERE LA FINESTRA PER ANNULLARE\n")

    ''' todo: scrivi il main che prende tutti i file csv della cartella e li converte
        crea dizionario degli iban e salva col nome del condominio'''
    
    try:
        diz_iban_csv = csv.reader(open("ibandiz.csv"))
        diz_iban = dict(diz_iban_csv)
    except:
        print("Il dizionario degli iban non è presente, i file verranno salvati col numero IBAN associato")
        diz_iban = False
    
    for textfile in get_text_files():
        elaborato = fix_format(textfile)
        print(f"Completata elaborazione di {elaborato}")
        
    input("\nOperazione completata\n\nE' ora possibile cancellare o spostare i file ottenuti dalle poste e caricare i file elaborati in CEDHOUSE utilizzando \"Movimineti CBI > Utilità > Importa tracciato CSV\"")
    
