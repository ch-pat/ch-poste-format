INSTALLAZIONE:
Per far funzionare il programma occorre avere Python installato sul proprio computer.
Seguire questo link: https://www.anaconda.com/download/
e scaricare la versione 3.7 (o superiore) e installarla.

Una volta installato Python, associare l'eseguibile di Python ai file .py
Per farlo, cliccare col tasto destro sul file .py (es: poste_csv_format.py) > Propriet� > apri con:
A questo punto occorre sfogliare le cartelle fino a trovare il percorso del proprio eseguibile di python, python.exe. 
Se si � installato anaconda seguendo le modalit� predefinite, il percorso sar� C:\Users\"nomeutente"\Anaconda3\python.exe

Fatto ci�, sar� possibile lanciare il programma con un semplice doppio clic.



MODALIT� D'USO:
Creare una cartella apposita per l'utilizzo del programma.
Scaricare da bancoposta gli estratti conto periodici trovati in "Funzioni Generali > Esporta Movimenti > Estratto conto periodico" in formato testo per excel
Estrarre i file .txt e spostare tutti gli estratti scaricati nella stessa cartella in cui si trova poste_csv_format.py e lanciare il programma, che li convertir� tutti in un formato accettato da CH.



OPZIONALE:
� possibile creare un file "ibandiz.csv" da mettere nella stessa cartella del programma. La presenza di questo "dizionario" consentir� al programma di salvare i file col nome del condominio invece che con l'IBAN.
Tale file DEVE essere impostato nella seguente maniera per funzionare:

IBAN1,NOMECONDOMINIO1
IBAN2,NOMECONDOMINIO2

Ed � NECESSARIO che non ci siano altre virgole oltre a quella separatrice. In ogni caso, il file non � necessario per il funzionamento del programma.