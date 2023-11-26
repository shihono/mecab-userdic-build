import csv
import os
import re
import argparse
from glob import glob

from jaconv import z2h
from mecab_userdic_build.mecab_tagger import get_reading_pronun

KATAKANA_PAT = re.compile(r"[\u30A1-\u30FF]+")
ORG_POS = "名詞,固有名詞,組織,*"

def load_csv(data_path):
    """略称,正式名称のペアを取得"""
    data_list = []
    with open(data_path, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            data_list.append(line)
    return data_list


def generate_mecab_entry(abbreviation, original):
    """略称,正式名称のペアからmecab ipadic のエントリを作成

    - 英数記号は半角、カタカナは全角に揃える
    - コストとIDは空のまま
    """
    abbreviation = z2h(abbreviation, kana=False, ascii=True, digit=True)
    original = z2h(original, kana=False, ascii=True, digit=True)

    if KATAKANA_PAT.fullmatch(original):
        # カタカナはそのまま読み・発音として利用
        reading, pronounce = original, original
    else:
        reading, pronounce = get_reading_pronun(original)
    
    return f"{abbreviation},,,,{ORG_POS},*,*,{original},{reading},{pronounce},abbr_company"


def main():
    parser = argparse.ArgumentParser(
        description="CSVからユーザー辞書用のCSVを作成。"
    )
    parser.add_argument(
        "input",
        type=str,
        help="Input csv file (略称,正式名称の2カラムで構成)。directoryを指定したい場合は --recursiveを指定",
    )
    parser.add_argument(
        "-O", "--output", type=str, help="Output csv file"
    )
    parser.add_argument(
        "--recursive", action="store_true", help="input directoryのcsvすべてについて実行"
    )
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    is_recursive = args.recursive
    if is_recursive:
        csv_paths = glob(os.path.join(input_path, "*.csv"))
    else:
        csv_paths = [input_path]

    entries = []
    for p in csv_paths:
        data_list = load_csv(p)
        for abbr, orig in data_list:
            entries.append(generate_mecab_entry(abbr, orig))

    with open(output_path, "w")as f:
        for line in entries:
            f.write(line + "\n")
            

if __name__ == "__main__":
    main()