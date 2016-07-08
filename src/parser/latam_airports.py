#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

airports = ["BSB", "CNF", "RIO", "SAO", "AJU", "AUX", "BEL", "BHZ", "BPS",
            "BRA", "BVB", "CAC", "CGB", "CGH", "CGR", "CWB", "DOU", "FLN",
            "FOR", "GIG", "GRU", "GYN", "IGU", "IMP", "IOS", "JOI", "JPA",
            "LDB", "MAB", "MAO", "MCP", "MCZ", "NAT", "NVT", "OPS", "PLU",
            "PMW", "POA", "PVH", "RAO", "RBR", "REC", "SDU", "SGH", "SJP",
            "SLZ", "SSA", "STM", "THE", "TJL", "UBA", "UDI", "VCP", "VDC",
            "VIX"]

# Avianca parsing
d = {}
for airport in airports:
    d[airport] = airport

a = open("../data/airlines/latam/airports.data", "w")
a.write(json.dumps(d).encode('utf8'))
a.close()
