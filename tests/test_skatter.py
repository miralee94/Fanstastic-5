from treasure import Skatter, Lösa_slantar, Pengapung, Guldsmycket, Liten_skattkista, Ädelsten


def test_skatter():
    skatter = Skatter(10, 10)  # testar huvudklassen
    assert skatter.value == 10
    assert skatter.ordinariness == 10


def test_lösa_slantar():
    skatter = Lösa_slantar()
    assert skatter.value == 2
    assert skatter.ordinariness == 40


def test_pengapung():
    skatter = Pengapung()
    assert skatter.value == 6
    assert skatter.ordinariness == 20


def test_guldsmycket():
    skatter = Guldsmycket()
    assert skatter.value == 10
    assert skatter.ordinariness == 15


def test_ädelsten():
    skatter = Ädelsten()
    assert skatter.value == 14
    assert skatter.ordinariness == 10


def test_Liten_skattkista():
    sk = Liten_skattkista()
    assert sk.value == 20
    assert sk.ordinariness == 5
