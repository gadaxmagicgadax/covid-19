Di seguito la procedura per l'utilizzo del codice python per il ricalcolo dei dati della protezione civile.

Il codice e lo scripting utilizzato sono stati scritti su MAC OS ma dovrebbero funzionare su qualsiasi Linux

Prima di tutto bisogna scaricare il file della protezione civile delle regioni nello stesso folder del codice python. Io utilizzo :

$ wget https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv

Lanciare il codice con :

$ python readalldata.py

Verranno creati tanti file quante sono le regioni nel file regioni.txt

Il seguente script prende tutti i file delle regioni e ricostruisce un unico file : alldatanormalised.csv

$ ./prepare.sh

Il file alldatanormalised.csv puo' essere a questo punto utilizzato con qualsiasi software di analisi




