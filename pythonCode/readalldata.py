
import csv

# get the file with all regions

file_reg = open("regioni.txt","r");

for regione in file_reg:
    fn_regione = regione.strip('\n') + '_out.csv'
    with open(fn_regione,'w') as file_regione:
        regione_writer = csv.writer(file_regione, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('dpc-covid19-ita-regioni.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rcs = 0
            ti = 0
            id = 0
            nap = 0
            dg = 0
            dec = 0
            tamp = 0
            rcs_d = 0
            line_count = 0
            line_reg = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    line_count += 1
                    if row[3] == regione.strip('\n'):
                        print({row[3]},' is the region and ',regione,'is from the list\n')
                        print(f'Processed {line_count} lines.')
                        if line_reg == 0:
                            regione_writer.writerow(row);
                            rcs = row[6]
                            ti  = row[7]
                            id = row[9]
                            nap = row[11]
                            dg = row[12]
                            dec = row[13]
                            tamp = row[15]
                            line_reg += 1
                        else:
                            line2print = []
                            line2print.append(row[0])
                            line2print.append(row[1])
                            line2print.append(row[2])
                            line2print.append(row[3])
                            line2print.append(row[4])
                            line2print.append(row[5])
                            # ricoverati_con_sintomi
                            rcs_d = int(row[6]) - int(rcs)
                            line2print.append(rcs_d)
                            # terapia_intensiva
                            ti_d = int(row[7]) - int(ti) 
                            line2print.append(ti_d)
                            # totale_ospedalizzati
                            to = rcs_d + ti_d
                            line2print.append(to)
                            # isolamento_domiciliare
                            id_d = int(row[9]) - int(id)
                            line2print.append(id_d)
                            # totale attualmente positivi
                            tap = rcs_d + ti_d + id_d
                            line2print.append(tap)
                            # nuovi_attualmente_positivi
                            nap = to + id_d
                            line2print.append(nap)
                            # dimessi_guariti
                            dg_d = int(row[12]) - int(dg)
                            line2print.append(dg_d)
                            # deceduti
                            dec_d = int(row[13]) - int(dec)
                            line2print.append(dec_d)
                            # totale casi
                            tc = tap + dg_d + dec_d
                            line2print.append(tc)
                            # tamponi
                            tamp_d = int(row[15]) - int(tamp)
                            line2print.append(tamp_d)
                            # print(line2print)
                            regione_writer.writerow(line2print)
                            rcs = row[6]
                            ti  = row[7]
                            id = row[9]
                            #nap = row[11]
                            dg = row[12]
                            dec = row[13]
                            tamp = row[15]
                            line_reg += 1
                                
            file_regione.close()
        csv_file.close()
            
