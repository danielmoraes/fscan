#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    print "Error importing BeautifulSoup Library"
import json

html = '''<option value="AJU">Aracaju (AJU)</option>
            <option value="AUX">Araguaina (AUX)</option>
            <option value="AUA">Aruba (AUA)</option>
            <option value="ASU">Asunci&#243;n (ASU)</option>
            <option value="ATL">Atlanta (ATL)</option>
            <option value="AUS">Austin (AUS)</option>
            <option value="BGI">Barbados (Bridgetown) (BGI)</option>
            <option value="BRA">Barreiras (BRA)</option>
            <option value="JTC">Bauru (JTC)</option>
            <option value="BEL">Bel&#233;m (BEL)</option>
            <option value="CNF">Belo Horizonte - Confins (CNF)</option>
            <option value="PLU">Belo Horizonte - Pampulha (PLU)</option>
            <option value="BHZ">Belo Horizonte - Todos os Aeroportos (BHZ)</option>
            <option value="BVB">Boa Vista (BVB)</option>
            <option value="BOS">Boston (BOS)</option>
            <option value="BSB">Brasilia (BSB)</option>
            <option value="AEP">Buenos Aires - Aeroparque (AEP)</option>
            <option value="EZE">Buenos Aires - Ezeiza (EZE)</option>
            <option value="BUE">Buenos Aires - Todos os Aeroportos (BUE)</option>
            <option value="CPV">Campina Grande (CPV)</option>
            <option value="CGR">Campo Grande  (CGR)</option>
            <option value="CCS">Caracas (CCS)</option>
            <option value="CAC">Cascavel (CAC)</option>
            <option value="CXJ">Caxias do Sul (CXJ)</option>
            <option value="XAP">Chapec&#243; (XAP)</option>
            <option value="CLT">Charlotte (CLT)</option>
            <option value="CHI">Chicago (CHI)</option>
            <option value="CVG">Cincinnati (CVG)</option>
            <option value="COR">Cordoba (COR)</option>
            <option value="CZS">Cruzeiro do Sul (CZS)</option>
            <option value="CGB">Cuiaba (CGB)</option>
            <option value="CWB">Curitiba (CWB)</option>
            <option value="DFW">Dallas (DFW)</option>
            <option value="DEN">Denver (DEN)</option>
            <option value="DTW">Detroit (DTW)</option>
            <option value="DOU">Dourados (DOU)</option>
            <option value="FEN">Fernando de Noronha (FEN)</option>
            <option value="PHL">Filad&#233;lfia (PHL)</option>
            <option value="FLN">Florian&#243;polis (FLN)</option>
            <option value="FOR">Fortaleza (FOR)</option>
            <option value="IGU">Foz do Iguacu (IGU)</option>
            <option value="GYN">Goiania (GYN)</option>
            <option value="IAH">Houston (IAH)</option>
            <option value="IOS">Ilheus (IOS)</option>
            <option value="IMP">Imperatriz  (IMP)</option>
            <option value="JPR">Ji-Paran&#225; (JPR)</option>
            <option value="JPA">Joao Pessoa (JPA)</option>
            <option value="JOI">Joinville (JOI)</option>
            <option value="JDO">Juazeiro do Norte (JDO)</option>
            <option value="LAS">Las Vegas (LAS)</option>
            <option value="LDB">Londrina (LDB)</option>
            <option value="LAX">Los Angeles (LAX)</option>
            <option value="MCP">Macapa (MCP)</option>
            <option value="MCZ">Maceio (MCZ)</option>
            <option value="MAO">Manaus (MAO)</option>
            <option value="MAB">Maraba (MAB)</option>
            <option value="MGF">Maringa (MGF)</option>
            <option value="MIA">Miami (MIA)</option>
            <option value="MSP">Minneapolis (MSP)</option>
            <option value="MOC">Montes Claros (MOC)</option>
            <option value="MVD">Montevideu  (MVD)</option>
            <option value="NAT">Natal (NAT)</option>
            <option value="LGA">Nova Iorque (LGA)</option>
            <option value="EWR">Nova Iorque (EWR)</option>
            <option value="NVT">Navegantes  (NVT)</option>
            <option value="JFK">Nova Iorque (JFK)</option>
            <option value="MCO">Orlando (MCO)</option>
            <option value="PMW">Palmas (PMW)</option>
            <option value="PTY">Panama (PTY)</option>
            <option value="PNZ">Petrolina (PNZ)</option>
            <option value="PHX">Phoenix (PHX)</option>
            <option value="PDX">Portland (PDX)</option>
            <option value="POA">Porto Alegre (POA)</option>
            <option value="BPS">Porto Seguro (BPS)</option>
            <option value="PVH">Porto Velho (PVH)</option>
            <option value="PPB">Presidente Prudente (PPB)</option>
            <option value="PUJ">Punta Cana  (PUJ)</option>
            <option value="RDU">Raleigh/Durhan (RDU)</option>
            <option value="REC">Recife (REC)</option>
            <option value="RAO">Ribeirao Preto (RAO)</option>
            <option value="RBR">Rio Branco  (RBR)</option>
            <option value="GIG">Rio de Janeiro - Gale&#227;o (GIG)</option>
            <option value="SDU">Rio de Janeiro - Santos Dumont (SDU)</option>
            <option value="RIO">Rio de Janeiro - Todos os Aeroportos (RIO)</option>
            <option value="ROS">Rosario (ROS)</option>
            <option value="SLC">Salt Lake City (SLC)</option>
            <option value="SSA">Salvador (SSA)</option>
            <option value="SAN">San Diego (SAN)</option>
            <option value="STM">Santarem (STM)</option>
            <option value="SDQ">Santo Domingo (SDQ)</option>
            <option value="SFO">S&#227;o Francisco (SFO)</option>
            <option value="SJP">S&#227;o Jos&#233; do Rio Preto (SJP)</option>
            <option value="SLZ">S&#227;o Luis (SLZ)</option>
            <option value="VCP">S&#227;o Paulo - Campinas (VCP)</option>
            <option value="CGH">S&#227;o Paulo - Congonhas (CGH)</option>
            <option value="GRU">S&#227;o Paulo - Guarulhos (GRU)</option>
            <option value="SAO">S&#227;o Paulo - Todos os Aeroportos (SAO)</option>
            <option value="SEA">Seattle (SEA)</option>
            <option value="OPS">Sinop (OPS)</option>
            <option value="STL">St. Louis (STL)</option>
            <option value="VVI">Sta Cruz de la Sierra (VVI)</option>
            <option value="TPA">Tampa (TPA)</option>
            <option value="THE">Teresina (THE)</option>
            <option value="TJL">Tr&#234;s Lagoas (TJL)</option>
            <option value="UBA">Uberaba (UBA)</option>
            <option value="UDI">Uberlandia  (UDI)</option>
            <option value="VAL">Valen&#231;a (VAL)</option>
            <option value="VIX">Vit&#243;ria (VIX)</option>
            <option value="VDC ">Vit&#243;ria da Conquista  (VDC )</option>
            <option value="IAD">Washington - Dulles (IAD)</option>
            <option value="DCA">Washington - Reagan (DCA)</option>
'''

#Gol parsing
l = []
soup = BeautifulSoup(html)
d = {}
for li in soup.findAll("option"):
    d[li["value"]] = li["value"]


a = open("../data/airlines/gol/airports.data", "w")
a.write(json.dumps(d).encode('utf8'))
a.close()
