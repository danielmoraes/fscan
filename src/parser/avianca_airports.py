#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    print("Error importing BeautifulSoup Library")
import json

html = '''<ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content" id="ui-id-4" tabindex="0" style="display: none; top: 239.75px; left: 812.375px; width: 222px;"><li class="ui-menu-item" id="ui-id-44" tabindex="-1">Abu Dhabi - AUH</li><li class="ui-menu-item" id="ui-id-45" tabindex="-1">Adis Abeba - ADD</li><li class="ui-menu-item" id="ui-id-46" tabindex="-1">Aracaju - AJU</li><li class="ui-menu-item" id="ui-id-47" tabindex="-1">Barranquilla - BAQ</li><li class="ui-menu-item" id="ui-id-48" tabindex="-1">Bogotá - BOG</li><li class="ui-menu-item" id="ui-id-49" tabindex="-1">Brasília - BSB</li><li class="ui-menu-item" id="ui-id-50" tabindex="-1">Bucaramanga - BGA</li><li class="ui-menu-item" id="ui-id-51" tabindex="-1">Cali - CLO</li><li class="ui-menu-item" id="ui-id-52" tabindex="-1">Campo Grande - CGR</li><li class="ui-menu-item" id="ui-id-53" tabindex="-1">Cartagena - CTG</li><li class="ui-menu-item" id="ui-id-54" tabindex="-1">Chapecó - XAP</li><li class="ui-menu-item" id="ui-id-55" tabindex="-1">Cuiabá - CGB</li><li class="ui-menu-item" id="ui-id-56" tabindex="-1">Curitiba - CWB</li><li class="ui-menu-item" id="ui-id-57" tabindex="-1">Florianópolis - FLN</li><li class="ui-menu-item" id="ui-id-58" tabindex="-1">Fortaleza - FOR</li><li class="ui-menu-item" id="ui-id-59" tabindex="-1">Goiânia - GYN</li><li class="ui-menu-item" id="ui-id-60" tabindex="-1">Ilhéus - IOS</li><li class="ui-menu-item" id="ui-id-61" tabindex="-1">Istanbul - IST</li><li class="ui-menu-item" id="ui-id-62" tabindex="-1">Joanesburgo - JNB</li><li class="ui-menu-item" id="ui-id-63" tabindex="-1">João Pessoa - JPA</li><li class="ui-menu-item" id="ui-id-64" tabindex="-1">Juazeiro do Norte - JDO</li><li class="ui-menu-item" id="ui-id-65" tabindex="-1">Maceió - MCZ</li><li class="ui-menu-item" id="ui-id-66" tabindex="-1">Madrid - MAD</li><li class="ui-menu-item" id="ui-id-67" tabindex="-1">Medellin - MDE</li><li class="ui-menu-item" id="ui-id-68" tabindex="-1">Natal - NAT</li><li class="ui-menu-item" id="ui-id-69" tabindex="-1">Passo Fundo - PFB</li><li class="ui-menu-item" id="ui-id-70" tabindex="-1">Pereira - PEI</li><li class="ui-menu-item" id="ui-id-71" tabindex="-1">Petrolina - PNZ</li><li class="ui-menu-item" id="ui-id-72" tabindex="-1">Porto Alegre - POA</li><li class="ui-menu-item" id="ui-id-73" tabindex="-1">RJ - Galeão - GIG</li><li class="ui-menu-item" id="ui-id-74" tabindex="-1">RJ - Santos Dumont - SDU</li><li class="ui-menu-item" id="ui-id-75" tabindex="-1">Recife - REC</li><li class="ui-menu-item" id="ui-id-76" tabindex="-1">Rio de Janeiro - RIO</li><li class="ui-menu-item" id="ui-id-77" tabindex="-1">SP - Congonhas - CGH</li><li class="ui-menu-item" id="ui-id-78" tabindex="-1">SP - Guarulhos - GRU</li><li class="ui-menu-item" id="ui-id-79" tabindex="-1">Salvador - SSA</li><li class="ui-menu-item" id="ui-id-80" tabindex="-1">Santa Marta - SMR</li><li class="ui-menu-item" id="ui-id-81" tabindex="-1">São Paulo - SAO</li></ul>'''

# Avianca parsing
l = []
soup = BeautifulSoup(html)
d = {}
for li in soup.findAll("li"):
    v = li.text.split(" - ")[-1]
    d[v] = v

a = open("../data/airlines/avianca/airports.data", "w")
a.write(json.dumps(d).encode('utf8'))
a.close()
