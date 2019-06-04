# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH, LEMMA, TAG, NORM, PRON_LEMMA


_exc = {}


for orth in [
    "co.",
    "Co.",
    "Dr.",
    "Inc.",
    "Ing.",
    "Mgr."
    "Mr.",
    "Mrs.",
    "Ms.",
    "Ph.D.",
]:
    _exc[orth] = [{ORTH: orth}]


for exc_data in [
    {ORTH: "a.s.", LEMMA: "akciová spoločnosť", NORM: "akciová spoločnosť"},
    {ORTH: "al.", LEMMA: "alebo", NORM: "alebo"},
    {ORTH: "angl.", LEMMA: "anglický", NORM: "anglický"},
    {ORTH: "ap.", LEMMA: "a podobný", NORM: "a podobný"},
    {ORTH: "Apr.", LEMMA: "Apríl", NORM: "Apríl"},
    {ORTH: "atď.", LEMMA: "a tak ďalej", NORM: "a tak ďalej"},
    {ORTH: "Aug.", LEMMA: "August", NORM: "August"},
    {ORTH: "č.", LEMMA: "číslo", NORM: "číslo"},
    {ORTH: "čísl.", LEMMA: "číslo", NORM: "číslo"},
    {ORTH: "Dec.", LEMMA: "December", NORM: "December"},
    {ORTH: "dipl.", LEMMA: "diplomatický", NORM: "diplomatický"},
    {ORTH: "E.Ú.", LEMMA: "Európska Únia", NORM: "Európska Únia"},
    {ORTH: "elektr.", LEMMA: "elektrický", NORM: "elektrický"},
    {ORTH: "eur.", LEMMA: "európsky", NORM: "európsky"},
    {ORTH: "expr.", LEMMA: "expresívny výraz", NORM: "expresívny výraz"},
    {ORTH: "Feb.", LEMMA: "Február", NORM: "Február"},
    {ORTH: "hl.", LEMMA: "hlavný", NORM: "hlavný"},
    {ORTH: "hod.", LEMMA: "hodina", NORM: "hodina"},
    {ORTH: "hovor.", LEMMA: "hovorovo", NORM: "hovorovo"},
    {ORTH: "i.", LEMMA: "iný", NORM: "iný"},
    {ORTH: "inf.", LEMMA: "informácie", NORM: "informácie"},
    {ORTH: "info.", LEMMA: "informácie", NORM: "informácie"},
    {ORTH: "inform.", LEMMA: "informácie", NORM: "informácie"},
    {ORTH: "Jan.", LEMMA: "Január", NORM: "Január"},
    {ORTH: "jedn.", LEMMA: "jednotné číslo", NORM: "jednotné číslo"},
    {ORTH: "kniž.", LEMMA: "knižný výraz", NORM: "knižný výraz"},
    {ORTH: "kpt.", LEMMA: "kapitán", NORM: "kapitán"},
    {ORTH: "kt.", LEMMA: "ktorý", NORM: "ktorý"},
    {ORTH: "lat.", LEMMA: "latinský", NORM: "latinský"},
    {ORTH: "Mar.", LEMMA: "Marec", NORM: "Marec"},
    {ORTH: "mat.", LEMMA: "matematický", NORM: "matematický"},
    {ORTH: "max.", LEMMA: "maximum", NORM: "maximum"},
    {ORTH: "min.", LEMMA: "minimum", NORM: "minimum"},
    {ORTH: "mn.č.", LEMMA: "množné číslo", NORM: "množné číslo"},
    {ORTH: "n.l.", LEMMA: "nášho letopočtu", NORM: "nášho letopočtu"},
    {ORTH: "napr.", LEMMA: "napríklad", NORM: "napríklad"},
    {ORTH: "Ne.", LEMMA: "Nedela", NORM: "Nedela"},
    {ORTH: "niekt.", LEMMA: "niektorý", NORM: "niektorý"},
    {ORTH: "Nov.", LEMMA: "November", NORM: "November"},
    {ORTH: "Okt.", LEMMA: "Október", NORM: "Október"},
    {ORTH: "org.", LEMMA: "organický", NORM: "organický"},
    {ORTH: "os.", LEMMA: "osoba", NORM: "osoba"},
    {ORTH: "označ.", LEMMA: "označenie", NORM: "označenie"},
    {ORTH: "Pia.", LEMMA: "Piatok", NORM: "Piatok"},
    {ORTH: "pl.", LEMMA: "plurál", NORM: "plurál"},
    {ORTH: "Po.", LEMMA: "Pondelok", NORM: "Pondelok"},
    {ORTH: "pod.", LEMMA: "a podobný", NORM: "a podobný"},
    {ORTH: "pod.", LEMMA: "podobne", NORM: "podobne"},
    {ORTH: "pr.", LEMMA: "príklad", NORM: "príklad"},
    {ORTH: "r.", LEMMA: "rok", NORM: "rok"},
    {ORTH: "r.o.", LEMMA: "ručením obmedzeným", NORM: "ručením obmedzeným"},
    {ORTH: "resp.", LEMMA: "respektíve", NORM: "respektíve"},
    {ORTH: "s.r.o.", LEMMA: "spoločnosť s ručením obmedzeným", NORM: "spoločnosť s ručením obmedzeným"},
    {ORTH: "Sep.", LEMMA: "September", NORM: "September"},
    {ORTH: "sg.", LEMMA: "singulár", NORM: "singulár"},
    {ORTH: "skr.", LEMMA: "skratka", NORM: "skratka"},
    {ORTH: "Sob.", LEMMA: "Sobota", NORM: "Sobota"},
    {ORTH: "soc.", LEMMA: "socializmus", NORM: "socializmus"},
    {ORTH: "st.", LEMMA: "stupeň", NORM: "stupeň"},
    {ORTH: "Str.", LEMMA: "Streda", NORM: "Streda"},
    {ORTH: "sv.", LEMMA: "svätý", NORM: "svätý"},
    {ORTH: "Štv.", LEMMA: "Štvrtok", NORM: "Štvrtok"},
    {ORTH: "t.j.", LEMMA: "to jest", NORM: "to jest"},
    {ORTH: "tel.", LEMMA: "telefónne", NORM: "telefónne"},
    {ORTH: "tel.", LEMMA: "telefón", NORM: "telefón"},
    {ORTH: "tel.č.", LEMMA: "telefónne číslo", NORM: "telefónne číslo"},
    {ORTH: "tzv.", LEMMA: "takzvaný", NORM: "takzvaný"},
    {ORTH: "úr.", LEMMA: "úrok", NORM: "úrok"},
    {ORTH: "Ut.", LEMMA: "Utorok", NORM: "Utorok"},
    {ORTH: "zn.", LEMMA: "značka", NORM: "značka"},
    {ORTH: "zv.", LEMMA: "zväzok", NORM: "zväzok"},
]:
    _exc[exc_data[ORTH]] = [exc_data]


TOKENIZER_EXCEPTIONS = _exc