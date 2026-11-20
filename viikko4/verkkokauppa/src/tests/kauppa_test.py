import unittest
from unittest.mock import Mock, call, ANY
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "kalja", 3),
        }
        saldot = {1: 10, 2: 10}

        self.varasto_mock.saldo.side_effect = lambda tuote_id: saldot.get(tuote_id, 0)
        self.varasto_mock.hae_tuote.side_effect = lambda tuote_id: tuotteet.get(tuote_id)
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock,
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_tilisiirto_metodia_kutsutaan_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_maksettaessa_kaksi_eri_ostosta_pankin_tilisiirto_metodia_kutsutaan_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_maksettaessa_kaksi_samaa_ostosta_pankin_tilisiirto_metodia_kutsutaan_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 6)

    def test_maksettaessa_kaksi_eri_ostosta_toinen_loppu_pankin_tilisiirto_metodia_kutsutaan_oikein(self):
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 0 if tuote_id == 1 else 10

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)

    def test_asioinnin_aloittaminen_nollaa_ostoskorin(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)

        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call(ANY, ANY, ANY, ANY, 3)
            ],
        )

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksulle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.kauppa.aloita_asiointi()
        
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call(ANY, 1, ANY, ANY, ANY),
                call(ANY, 2, ANY, ANY, ANY),
                call(ANY, 3, ANY, ANY, ANY)
            ],
        )

    def test_poista_tuote_korista(self):
        self.kauppa.aloita_asiointi()

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 8)

