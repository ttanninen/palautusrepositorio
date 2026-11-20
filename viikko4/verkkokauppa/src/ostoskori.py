class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        for index, korissa_oleva_tuote in enumerate(self._tuotteet):
            if korissa_oleva_tuote.id == tuote.id:
                del self._tuotteet[index]
                break

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
