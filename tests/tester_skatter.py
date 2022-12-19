from treasure import Skatter, Lösa_slantar, Pengapung, Guldsmycket, Liten_skattkista, Ädelsten


def test_skatter():
    skatter = Skatter(10, 10)  # testar huvudklassen
    assert skatter.värde == 10
    assert skatter.vanlighet == 10


def test_lösa_slantar():
    skatter = Lösa_slantar()
    assert skatter.värde == 2
    assert skatter.vanlighet == 40


def test_pengapung():
    skatter = Pengapung()
    assert skatter.värde == 6
    assert skatter.vanlighet == 20


def test_guldsmycket():
    skatter = Guldsmycket()
    assert skatter.värde == 10
    assert skatter.vanlighet == 15


def test_ädelsten():
    skatter = Ädelsten()
    assert skatter.värde == 14
    assert skatter.vanlighet == 10


def test_Liten_skattkista():
    sk = Liten_skattkista()
    assert sk.värde == 20
    assert sk.vanlighet == 5
