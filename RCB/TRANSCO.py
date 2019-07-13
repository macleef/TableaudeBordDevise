import csv

def transco (table, champ_old, champ_new, attribut,espace):
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
                grouping=item[5]
                if old_value not in transco_fields and (grouping=='ZPFP' or grouping=='ZPFG') and old_value != new_value:
                        transco_fields[old_value] = new_value

        productid=[]
        miss_value=[]
        transco_file = open ("transco_"+attribut+".csv", "w")
        value_miss_file = open("value_miss_"+attribut+".csv", "w")
        write_space='|'
        i=0
        while i < espace :
                write_space=write_space+'|'
                i+=1
        transco_file.write('PRODUCTID'+write_space+attribut+'\n')
        for items in table:
                value=items[index_champ]
                if value in transco_fields:
                        #productid.append('"'+items[0]+'"'+ +'"'+transco_fields[value]+'"')
                        transco_file.write('"'+items[0]+'"'+ write_space +'"'+transco_fields[value]+'"\n')
                """ else:
                        if value not in miss_value:
                                miss_value.append(value)
                                value_miss_file.write(value+'\n') """
        transco_file.close()
        value_miss_file.close()

transco('TIERS', 'TIERS_LEGACY','PARTNER','ERP_ID_TIERS',1)


def transco_TIERS_FACTURATION():
        import csv
        f_transco=open("Transco.csv", encoding="utf8")
        f_table=open("REL_CLIENT_ADR_ranq.csv",  encoding="utf8")
        transco = list(csv.reader(f_transco))
        table=list(csv.reader(f_table))

        index_old = transco[0].index('TIERS_LEGACY')
        index_new = transco[0].index('PARTNER')
        index_adresse_leg = transco[0].index('ADRESSE_LEGACY')
        index_champ = table[0].index('TIERS_FACTURATION')
        transco_fields={}
        transco_file = open ("TRANSCO_REL_CLIENT_ADR.csv", "w")
        tiers_manquant_file = open ("TIERS_MANQUANT.csv", "w")

        tiers_manquant=[]
        for item in transco:
                tier_value = item[index_old]
                adresse_value = item[index_adresse_leg]
                key=tier_value+','+adresse_value
                partner_value = item[index_new]
                if tier_value not in transco_fields and tier_value!=partner_value:
                        transco_fields[key] = partner_value
        
        transco_file.write('ID_PONT_TIERS_STE_COM|IDEXT_PONT_TIERS_STE_COM|ID_ADRESSE|LEGALE|COMP_ADR_1_LEGALE|COMP_ADR_2_LEGALE|NOM_LEGALE|NUM_ADR_LEGALE|TIERS_LEGALE|ETAT_LEGALE|STATUT_LEGALE|FACTURATION|COMP_ADR_1_FACTURATION|COMP_ADR_2_FACTURATION|NOM_FACTURATION|NUM_ADR_FACTURATION|TIERS_FACTURATION|ETAT_FACTURATION|STATUT_FACTURATION|LIVRAISON|COMP_ADR_1_LIVRAISON|COMP_ADR_2_LIVRAISON|NOM_LIVRAISON|NUM_ADR_LIVRAISON|TIERS_LIVRAISON|ETAT_LIVRAISON|STATUT_LIVRAISON|PAIEMENT|COMP_ADR_1_PAIEMENT|COMP_ADR_2_PAIEMENT|NOM_PAIEMENT|NUM_ADR_PAIEMENT|TIERS_PAIEMENT|ETAT_PAIEMENT|STATUT_PAIEMENT|COMMANDE|COMP_ADR_1_COMMANDE|COMP_ADR_2_COMMANDE|NOM_COMMANDE|NUM_ADR_COMMANDE|TIERS_COMMANDE|ETAT_COMMANDE|STATUT_COMMANDE|TIERS_FACT_QUALIAC|TIERS_LIV_QUALIAC|TIERS_PAIE_QUALIAC|TIERS_COMM_QUALIAC|COMP_ADD_3_FACT|COMP_ADD_3_LIV|COMP_ADR_3_PAIE|COMP_ADR_3_COMM|LIVRAISON2|COMP_ADR_1_LIVRAIS2|COMP_ADR_2_LIVRAI2|COMP_ADR_3_LIVRAI2|NOM_LIVRA|TIERS_LIVRA2|TYPE_LIVRAI|TYPE_LIVRAI2\n')
        for data in table:
                ids='"'+data[0]+'"|"'+data[1]+'"|"'+data[2]+'"'
                legacy_fact=data[4]+','+data[5]
                legacy_comm=data[6]+','+data[7]
                legacy_paie=data[8]+','+data[9]
                legacy_livr=data[10]+','+data[11]

                partner_fact=''
                partner_comm=''
                partner_paie=''
                partner_livr=''

                if legacy_fact in transco_fields:
                        partner_fact=transco_fields[legacy_fact]
                if legacy_comm in transco_fields:
                        partner_comm=transco_fields[legacy_comm]
                if legacy_paie in transco_fields:
                        partner_paie=transco_fields[legacy_paie]
                if legacy_livr in transco_fields:
                        partner_livr=transco_fields[legacy_livr]

                if partner_fact+partner_comm+partner_paie+partner_livr!='':
                        transco_file.write(ids+'||||||||||||||"'+partner_fact+'"||||||||"'+partner_livr+'"||||||||"'+partner_paie+'"||||||||"'+partner_comm+'"||\n')
                #else:
                #        if legacy_fact not in tiers_manquant:
                #                tiers_manquant.append(legacy_fact)
                #                tiers_manquant_file.write(legacy_fact+'\n')

        transco_file.close()
        tiers_manquant_file.close()
transco_TIERS_FACTURATION()

def transco_erp_id_adresse():
        import csv
        f_table=open("ADRESSE_NO_ID_ADD.csv", encoding="utf8")
        table=list(csv.reader(f_table))

        adress_file=open("ADRESS_ADD_ERP_ADRESS.csv","w")

        for item in table:
                adresse=item[0]
                erp_id=item[1]+'_001'
                adress_file.write(adresse+'|||||||||||||||||||'+erp_id+'\n')

        adress_file.close()

transco_erp_id_adresse()

def transco_tiers_comm():
        import csv
        f_transco=open("Transco.csv", encoding="utf8")
        transco = list(csv.reader(f_transco))
        f_tiers_ste=open("REL_TIERS_STE_COMM.csv", encoding="utf8")
        tiers_ste = list(csv.reader(f_tiers_ste))

        transco_legacy={}
        for data in transco:
                tiers_legacy=data[3]
                partner=data[0]
                grouping=data[5]
                if grouping=='ZPFP' or grouping=='ZPFG':
                        if tiers_legacy not in transco_legacy:
                                transco_legacy[tiers_legacy]=partner

        transco_tiers_ste_com=open('transco_PONT_TIERS_STE_COM.csv','w')
        transco_tiers_ste_com.write('ID|IDEXT|erp_id_client||||||||||||||||||||||||||||||||erp_id_tiers\n')
        for item in tiers_ste:
                ids=item[0]+'|'+item[1]
                erp_id_client_old=item[2]
                erp_id_tiers_old=item[3]
                len_client=len(erp_id_client_old)
                erp_id_client_6=erp_id_client_old[len_client-6:len_client]

                if erp_id_client_6 in transco_legacy:
                        erp_id_tiers=transco_legacy[erp_id_client_6]
                        erp_id_client=erp_id_client_old[:3]+transco_legacy[erp_id_client_6]
                        transco_tiers_ste_com.write(ids+'|'+erp_id_client+'||||||||||||||||||||||||||||||||'+erp_id_tiers+'\n')

        transco_tiers_ste_com.close()

transco_tiers_comm()

def transco_erp_adresse():
        import csv
        transco_erp_id_adresse()
        f_transco=open("Transco.csv", encoding="utf8")
        transco = list(csv.reader(f_transco))
        f_table=open("ERP_ID_ADRESSE.csv", encoding="utf8")
        table=list(csv.reader(f_table))
        f_table_new=open("ADRESS_ADD_ERP_ADRESS.csv", encoding="utf8")
        table_new=list(csv.reader(f_table_new,delimiter="|"))

        transco_erp_adress={}
        for item in transco:
                adress_legacy=item[3]+'_'+item[4]
                if adress_legacy not in transco_erp_adress:
                        transco_erp_adress[adress_legacy] = item[7]
        erp_adress_file=open('TRANSCO_ERP_ID_ADRESS.csv','w')
        erp_adress_file.write('ADRESSE_ID|||||||||||||||||||ERP_ID_ADRESSE\n')
        for data in table:
                old_erp_adress=data[1]
                if old_erp_adress in transco_erp_adress:
                        new_erp_adress = transco_erp_adress[old_erp_adress]
                        erp_adress_file.write(data[0]+'|||||||||||||||||||'+new_erp_adress+'\n')

        for data_new in table_new:
                old_erp_adress_new=data_new[19]
                if old_erp_adress_new in transco_erp_adress:
                        new_erp_adress_new = transco_erp_adress[old_erp_adress_new]
                        erp_adress_file.write(data_new[0]+'|||||||||||||||||||'+new_erp_adress_new+'\n')

        erp_adress_file.close()
        f_transco.close()
        f_table.close()
        f_table_new.close()

transco_erp_adresse()

#ef transco_erp_categories():
import csv
f_transco_cat=open("TRANSCO.CAT.csv", encoding="utf8")
transco_cat = list(csv.reader(f_transco_cat,delimiter="|"))
f_table = open("TIERS_CAT.csv", encoding="utf8")
table = list(csv.reader(f_table,delimiter=","))
f_categorie = open('export_CATEGORIE_ERP.csv', encoding="utf8")
categories=list(csv.reader(f_categorie,delimiter=","))

transco={}
for item in transco_cat:
        cat_qualiac=item[0]
        cat_sap=item[7]
        if cat_qualiac not in transco:
                transco[cat_qualiac] = cat_sap

categorie_erp={}
categorie_qualiac={}
for categorie in categories:
        cat_id=categorie[0]
        cat_qualiac=categorie[3]
        cat_erp=categorie[6]
        if cat_qualiac not in categorie_qualiac:
                categorie_qualiac[cat_qualiac]=cat_id
        if cat_erp not in categorie_erp:
                categorie_erp[cat_erp]=cat_id

tiers_cat_file=open('TRANSCO_TIERS_CATEGORIES.csv','w')
tiers_cat_file.write('tiers_id||||||||||||||||||new_code\n')
for data in table:
        tiers_id=data[0]
        old_code=data[1]
        if old_code in transco:
                new_code=transco[old_code]
                tiers_cat_file.write(tiers_id+'||||||||||||||||||'+categorie_erp[new_code]+'\n')


#transco_erp_categories()

def transco_param_categorie():
        import csv
        f_param=open("export_PARAM_CAT.csv", encoding="utf-8")
        f_transco=open("Transco_categories.csv", encoding="utf-8")
        params=list(csv.reader(f_param, delimiter=';'))
        transco=list(csv.reader(f_transco, delimiter=';'))

        transco_dic={}
        erf_qualiac={}

        for data in transco:
                code_qualiac=data[0]
                code_erf=data[1]
                if code_qualiac not in transco:
                        transco_dic[code_qualiac]=code_erf
                
                for qualiac, erf in transco_dic.items():
                        if qualiac == erf and erf not in erf_qualiac.values():
                                erf_qualiac[qualiac]=erf
                        
                for qualiac, erf in transco_dic.items():
                        if erf not in erf_qualiac.values():
                                erf_qualiac[qualiac]=erf
        tiers_cat_file=open('TRANSCO_PARAM_CATEGORIES.csv','w')
        tiers_cat_file.write("CODE_LISTE|||||||CODE_ERF|||PRODUCTID|\n")
        param_qualiac={}
        for item in params:
                id_param=item[0]
                qualiac_param=item[1]
                if qualiac_param in erf_qualiac:
                        tiers_cat_file.write("|||||||"+erf_qualiac[qualiac_param]+"|||"+id_param+"|\n")
                        param_qualiac[id_param]=erf_qualiac[qualiac_param]
                elif qualiac_param in transco_dic:
                        tiers_cat_file.write("|I|||||||||"+id_param+"|\n")
transco_param_categorie()


def transco_pont_tiers_cat():
        import csv
        f_pont_tiers=open("export_PONT_TIERS_CAT.csv", encoding="utf-8")
        f_transco=open("Transco_categories.csv", encoding="utf-8")
        pont_tiers=list(csv.reader(f_pont_tiers, delimiter=';'))
        transco=list(csv.reader(f_transco, delimiter=';'))

        transco_dic={}

        for data in transco:
                code_qualiac=data[0]
                code_erf=data[1]
                if code_qualiac not in transco:
                        transco_dic[code_qualiac]=code_erf

        pont_tiers_erf_cat=open("TRANSCO_PONT_TIERS_CAT.csv",'w')
        pont_tiers_erf_cat.write("PRODUCTID|PRODUCTIDEXT|||CATEGORIE\n")
        for tier in pont_tiers:
                tier_id=tier[0]
                tier_id_ext=tier[1]
                categorie=tier[2]
                if categorie in transco_dic:
                        categorie_erf=transco_dic[categorie]
                        if categorie != categorie_erf:
                                pont_tiers_erf_cat.write('"'+tier_id+'"|"'+tier_id_ext+'"|||"'+transco_dic[categorie]+'"\n')


transco_pont_tiers_cat()

def transco_param_groupe():
        import csv
        f_tranco=open("Codes Société SL S4 vs SCORE.csv", encoding="utf-8")
        f_param=open("export_RCB_PARAM.csv", encoding="utf-8")
        transco=list(csv.reader(f_tranco, delimiter=';'))
        param=list(csv.reader(f_param, delimiter=';'))

        groupe_no_erp=[]
        liste_qualiac_harm=[data[2] for data in transco]
        param_dict={}
        for line in param:
                if line[0]=='PP_GROUPE':
                        param_qualiac=line[3]
                        param_id=line[8]
                        if param_qualiac not in param_dict:
                                param_dict[param_qualiac]=param_id
                        if param_qualiac not in liste_qualiac_harm:
                                groupe_no_erp.append(param_id)
        
        tiers_cat_file=open('TRANSCO_PARAM_GROUPE.csv','w',encoding="utf-8")
        tiers_cat_file.write("CODE_LISTE|||||||CODE_ERF|LIBELLE||PRODUCTID|\n")

        for id_pp in groupe_no_erp:
                tiers_cat_file.write('PP_GROUPE|I|||||||||'+id_pp+'|\n')
        
        for data in transco:
                erf=data[1]
                qualiac=data[2]
                libelle=data[0]
                new=data[4]
                code_element=''
                actif='A'

                if not new.strip() and qualiac in param_dict:
                        param_id=param_dict[qualiac]                
                else:
                        param_id='GRP_'+erf                                 

                tiers_cat_file.write('PP_GROUPE|'+actif+'||||||'+erf+'|'+ libelle +'||'+param_id+"|\n")

        f_param.close()
        f_tranco.close()
        tiers_cat_file.close()
transco_param_groupe()


import csv

transco_param_groupe()
f_tranco=open("TRANSCO_PARAM_GROUPE.csv", encoding="utf-8")
f_tiers=open("export_TIERS.csv", encoding="utf-8").read()
f_tiers = f_tiers.replace(',', ';')
f_tiersnew = open("export_TIERS.csv",'w', encoding="utf-8")
f_tiersnew.write(f_tiers)
f_tiersnew.close

transco=list(csv.reader(f_tranco, delimiter='|'))
tiers=list(csv.reader(f_tiers, delimiter=','))



transco_data={}
for data in transco:
        groupe_qualiac=data[4]
        groupe_s4=data[7]
        if groupe_qualiac not in transco_data:
                transco_data[groupe_qualiac]=groupe_s4

for tier in tiers:
        id_tier=tier[0]

