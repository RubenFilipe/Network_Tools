
#!/usr/bin/env python
# -*- coding: utf8 -*-

from settings import *

print("""

	Gerador VRF RIS-DADOS v0.1

	""")


###Options VRF
def fun_opt():	
	site_id=raw_input(text["sid"])
	vrf_id = raw_input(text["vnr"])
	print(text["menu2"])
	tipo= raw_input(text["tps"])
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print(vrf_texts["site_text"])
	tipo_site = "-" + tipo
	mse=raw_input(text["c_mse"])
	vrf,code = select_vrf()
	print_vrf_opt(site_id,vrf_id,tipo_site,mse,vrf,code)
##Print VRF
def print_vrf_opt(site_id,vrf_id,tipo_site,mse,vrf,code):	
	print("\n\n")
	print(desc["as"] + code + vrf_id + " [" + vrf + "] (" + vrf +  desc["geral"] + site_id + tipo_site + ")")
	print("	" + desc["as"] + code + mse + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RD)")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTe)")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTi)")
##Print VRF
def fun_zon():	
	site_id=raw_input(text["sid"])
	vrf_id = raw_input(text["vnr"])
	print(text["menu2"])
	tipo= raw_input(text["tps"])
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print(vrf_texts["site_text"])
	tipo_site = "-" + tipo
	erip_one=raw_input(erips_text["ep"])
	erip_one_id=raw_input(erips_text["epid"])
	erip_two=raw_input(erips_text["ep2"])
	erip_two_id=raw_input(erips_text["ep2id"])
	vrf,code = select_vrf()
	print_vrf_zon(site_id,vrf_id,tipo_site,vrf,code,erip_one_id,erip_two_id,erip_one,erip_two)
##Print VRF
def print_vrf_zon(site_id,vrf_id,tipo_site,vrf,code,erip_one_id,erip_two_id,erip_one,erip_two):
	print("\n\n")
	print(desc["as"] + code + vrf_id + " [" + vrf + "] (" + vrf +  desc["geral"] + site_id + tipo_site + ")")
	print("	" + desc["as"] + code + "00" + erip_one_id + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RD, " + erip_one + ")")
	print("	" + desc["as"] + code + "00" + erip_two_id + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RD, " + erip_two + ")")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTe)")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTi)")
## VRF Options
def fun_nos():	
	site_id=raw_input(text["sid"])
	vrf_id=raw_input(text["vnr"])
	print(text["menu2"])
	tipo= raw_input(text["tps"])
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print(vrf_texts["site_text"])
	tipo_site = "-" + tipo
	erip_one=raw_input(erips_text["ep"])
	erip_one_id=raw_input(erips_text["epid"])
	vrf,code = select_vrf()
	print_vrf_nos(site_id,vrf_id,tipo_site,vrf,code,erip_one_id,erip_one)
##Print VRF
def print_vrf_nos(site_id,vrf_id,tipo_site,vrf,code,erip_one_id,erip_one):	
	print("\n\n")
	print(desc["as"] + code + vrf_id + " [" + vrf + "] (" + vrf +  desc["geral"] + site_id + tipo_site + ")")
	print("	" + desc["as"] + code + "00" + erip_one_id + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RD, " + erip_one + ")")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTe)")
	print("	" + desc["as"] + code + desc["palha"] + " (" + vrf + desc["geral"] + site_id + tipo_site + ", RTi)")
############# FIM NGN ###################
def select_vrf():
	print(vrf_texts["cir_text"])
	for linha in vrfs:
		for num in linha:
			print(num + " - " + vrfs[linha])
	vrf=raw_input(text["c_vrf"])
	if vrf == '1' :
		vrf=vrfs['1']
		code=vrfs_rds["VPN_RIS"]
	elif vrf == '2' :
		vrf=vrfs['2']
		code=vrfs_rds["VPN_RIS_WIFI_UTENTES"]
	elif vrf == '3' :
		vrf=vrfs['3']
		code=vrfs_rds["VPN_SICAD"]
	elif vrf == '4' :
		vrf=vrfs['4']
		code=vrfs_rds["VPN_CH_CHLO"]
	elif vrf == '5' :
		vrf=vrfs['5']
		code=vrfs_rds["VPN_CH_CHTV"]
	elif vrf == '6' :
		vrf=vrfs['6']
		code=vrfs_rds["VPN_CH_CHBV"]
	else :
		print(vrf_texts["list_text"])
		return select_vrf()
	return vrf,code
##Main function
def fun_main():
	print(text["menu1"])
	opc=raw_input(text["isp"])
	if opc == '1':
		fun_opt()
	elif opc == '2':
		fun_zon()
	elif opc == '3':
		fun_nos()

##Run Main Function
fun_main()
