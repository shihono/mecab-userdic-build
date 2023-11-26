import pytest

from mecab_userdic_build.create_userdic import generate_mecab_entry

@pytest.mark.parametrize("abbr,original,entry",[
    ("テスト", "テスト", "テスト,,,,名詞,固有名詞,組織,*,*,*,テスト,テスト,テスト,abbr_company"),
    ("東京特許許可局", "東京特許許可局", "東京特許許可局,,,,名詞,固有名詞,組織,*,*,*,東京特許許可局,トウキョウトッキョキョカキョク,トーキョートッキョキョカキョク,abbr_company"),
    ("みずほ銀", "みずほ銀行", "みずほ銀,,,,名詞,固有名詞,組織,*,*,*,みずほ銀行,ミズホギンコウ,ミズホギンコー,abbr_company"),
    ("ZHD", "Zホールディングス", "ZHD,,,,名詞,固有名詞,組織,*,*,*,Zホールディングス,*,*,abbr_company"),
    ("Ｇｉｔｈｕｂ", "Ｇｉｔｈｕｂ", "Github,,,,名詞,固有名詞,組織,*,*,*,Github,*,*,abbr_company")
    ]
)
def test_generate_mecab_entry(abbr,original,entry):
    assert generate_mecab_entry(abbr, original) == entry
