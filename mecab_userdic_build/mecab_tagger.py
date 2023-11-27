import subprocess
import re

import MeCab
import unidic_lite

KATAKANA_PAT = re.compile(r"[\u30A1-\u30FF]+")

def get_mecab_dir():
    """mecabの辞書ディレクトリの取得"""
    res = subprocess.run("mecab-config --dicdir", shell=True, capture_output=True)
    return res.stdout.decode().strip()


def parse(text, dictdir=None, output_format = ""):
    if dictdir is None: 
        dictdir = unidic_lite.DICDIR
    option = f"-r /dev/null -d {dictdir} {output_format}".strip()
    tagger = MeCab.Tagger(option)
    return tagger.parse(text).splitlines()


def get_reading_pronun(word):
    """分かち書き結果から読みと発音のペアを取得する"""
    morphs = parse(word, dictdir=f"{get_mecab_dir()}/ipadic")
    reading = []
    pronounce = []
    for morph in morphs[:-1]:
        surface, features = morph.split("\t")
        feature_list = features.split(",")
        if feature_list[0] == "記号":
            continue
        if feature_list[-1] != "*" and feature_list[-2] != "*":
            pronounce.append(feature_list[-1])
            reading.append(feature_list[-2])
        elif KATAKANA_PAT.fullmatch(surface):
            # カタカナはそのまま読み・発音として利用
            pronounce.append(surface)
            reading.append(surface)
        else:
            # 未知語が含まれる場合
            return ["*", "*"]
    return ("".join(reading), "".join(pronounce))