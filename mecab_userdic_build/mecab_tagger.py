import MeCab
import unidic_lite

def parse(text, dictdir=None, output_format = ""):
    if dictdir is None: 
        dictdir = unidic_lite.DICDIR
    option = f"-r /dev/null -d {dictdir} {output_format}".strip()
    tagger = MeCab.Tagger(option)
    return tagger.parse(text).splitlines()
