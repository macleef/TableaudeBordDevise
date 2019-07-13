import csv
f_transco=open("Transco.csv", encoding="utf8")
f_tiers=open("TIERS.csv", encoding="utf8")
transco = list(csv.reader(f_transco))
#print(transco[0:10])
tiers = list(csv.reader(f_tiers))
#print(tiers[0:5])

tiers_legacy=[]
tiers_tiers_bp={}
for item in transco:
        tier = item[3]
        bp = item[0]
        if tier not in tiers_tiers_bp and tier != bp:
                tiers_tiers_bp[tier] = bp

productid=[]
for items in tiers:
        tier=items[2]
        if tier in tiers_tiers_bp:
                productid.append('"'+items[0]+'"||"'+tiers_tiers_bp[tier]+'"')
        
print(productid[0:5])

list_id = open ("listid.csv", "w")
for data in productid:
        list_id.write(data)
        list_id.write('\n')
list_id.close()

import csv
def transco (table, champ_old, champ_new, attribut):
        f_transco=open("Transco.csv", encoding="utf8")
        f_table=open(table+".csv", encoding="utf8")
        transco = list(csv.reader(f_transco))
        table=list(csv.reader(f_table))

        index_old = transco[0].index(champ_old)
        index_new = transco[0].index(champ_new)
        index_champ = table[0].index(attribut)
        transco_fields={}

        for item in transco:
                old_value = item[index_old]
                new_value = item[index_new]
                if old_value not in tiers_tiers_bp and old_value != new_value:
                        transco_fields[old_value] = new_value

        productid=[]
        transco_file = open ("transco_"+attribut+"".csv", "w")
        for items in table:
                value=items[index_champ]
                if value in transco_fields:
                        productid.append('"'+items[0]+'"||"'+transco_fields[value]+'"')
                        transco_file.write('"'+items[0]+'"||"'+transco_fields[value]+'"\n')
        transco_file.close()

transco('TIERS', 'TIERS_LEGACY','PARTNER')

