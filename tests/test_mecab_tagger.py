import pytest

from mecab_userdic_build.mecab_tagger import parse

params = {
     "pythonが大好きです": [
         "python\tpython\tpython\tpython\t名詞-普通名詞-一般\t\t\t0",
         "が\tガ\tガ\tが\t助詞-格助詞\t\t\t",
         "大好き\tダイスキ\tダイスキ\t大好き\t形状詞-一般\t\t\t1",
         "です\tデス\tデス\tです\t助動詞\t助動詞-デス\t終止形-一般\t",
         "EOS"
    ],
     "東京特許許可局": [
         "東京\tトーキョー\tトウキョウ\tトウキョウ\t名詞-固有名詞-地名-一般\t\t\t0",
         "特許\tトッキョ\tトッキョ\t特許\t名詞-普通名詞-一般\t\t\t1,0",
         "許可\tキョカ\tキョカ\t許可\t名詞-普通名詞-サ変可能\t\t\t1",
         "局\tキョク\tキョク\t局\t名詞-普通名詞-助数詞可能\t\t\t1",
         "EOS"
     ]
 }

@pytest.mark.parametrize(
        "text,words",
        list(params.items())
)
def test_parse_unidic(text,words):
    assert parse(text) == words