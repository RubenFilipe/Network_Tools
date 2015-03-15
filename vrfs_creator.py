#!/usr/bin/env python
# -*- coding: utf8 -*-

print("""

	Gerador VRF RIS-DADOS v0.1

	""")
################# Info Base ##################
desc={
	"geral" : "-RISD",
	"pri" : "-P",
	"back" : "-B",
	"con" : "-C",
	"as" : "2860:",
	"palha":"0000"
}

vrfs={
	"1":"VPN_RIS",
	"2":"VPN_RIS_WIFI_UTENTES",
	"3":"VPN_SICAD",
	"4":"VPN_CH_CHLO",
	"5":"VPN_CH_CHTV",
	"6":"VPN_CH_CHBV"
	}

###Options VRF
def fun_opt():	
	site_id=raw_input("Inserir Site ID : ")
	vrf_id = raw_input("Nr VRF : ")
	print("""
	1 - Principal
	2 - Backup
	3 - Contigência
		""")
	tipo= raw_input("Escolhe tipo site : ")
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print("Escolhe tipo de site correcto!")
	tipo_site = "-" + tipo
	mse=raw_input("Inserir Nr MSE:")
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
	site_id=raw_input("Inserir Site ID : ")
	vrf_id = raw_input("Nr VRF : ")
	print("""
	1 - Principal
	2 - Backup
	3 - Contigência
		""")
	tipo= raw_input("Escolhe tipo site : ")
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print("Escolhe tipo de site correcto!")
	tipo_site = "-" + tipo
	erip_one=raw_input("ERIP P:")
	erip_one_id=raw_input("Erip Id : ")
	erip_two=raw_input("ERIP B:")
	erip_two_id=raw_input("Erip2 Id: ")
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
	site_id=raw_input("Inserir Site ID : ")
	vrf_id=raw_input("Nr VRF : ")
	print("""
	1 - Principal
	2 - Backup
	3 - Contigência
		""")
	tipo= raw_input("Escolhe tipo site : ")
	if tipo == '1':
		tipo="P"
	elif tipo == '2':
		tipo="B"
	elif tipo == '3':
		tipo="C"
	else:
		print("Escolhe tipo de site correcto!")
	tipo_site = "-" + tipo
	erip_one=raw_input("ERIP P:")
	erip_one_id=raw_input("Erip Id : ")
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
	print("Escolher VRF adequada ao Circuito!\n")
	for linha in vrfs:
		for num in linha:
			print(num + " - " + vrfs[linha])
	vrf=raw_input("Escolhe VRF --> ")
	if vrf == '1' :
		vrf=vrfs['1']
		code="11268"
	elif vrf == '2' :
		vrf=vrfs['2']
		code="11422"
	elif vrf == '3' :
		vrf=vrfs['3']
		code=""
	elif vrf == '4' :
		vrf=vrfs['4']
		code=""
	elif vrf == '5' :
		vrf=vrfs['5']
		code=""
	elif vrf == '6' :
		vrf=vrfs['6']
		code=""
	else :
		print("Escolhe uma VRF da lista.")
		return select_vrf()
	return vrf,code
##Main function
def fun_main():
	print("""
Escolher Operador

1- Optimus
2- ZON
3- NÓS NGN
	""")
	opc=raw_input("ISP-->")
	if opc == '1':
		fun_opt()
	elif opc == '2':
		fun_zon()
	elif opc == '3':
		fun_nos()
##Run Main Function
fun_main()
