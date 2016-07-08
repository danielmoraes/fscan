import os
from parser.parser import ParserAzul, ParserGol, ParserAvianca, ParserLatam

project_path = os.path.dirname(os.path.realpath(__file__))[:-5]

locale = "en-us"

main_locale = None

parsers = {
    "azul": ParserAzul,
    "gol": ParserGol,
    "avianca": ParserAvianca,
    "latam": ParserLatam
}
