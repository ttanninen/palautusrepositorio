### TDD-ostokorin agenttinen ohjelmointi

Mielestäni agentin toteutukset olivat kautta linjan hyviä ja testit testasivat sitä, mitä pitikin. Yhtä testiä (tyhjä ostoskori) minun piti tarkentaa, että mitä kaikkea tyhjä ostoskori tarkoittaa.
Agentti ei koskenut testeihin A osassa ollenkaan. Mielestäni agentti pysyi kyllä minimitoteutuksessa, mutta silti A-kohdan viimeiset askeleet tulivat toteutetuksi jo etukäteen. En oikein tiedä miten toiminnallisuuden olisi voinut toteuttaa minimaalisemmin, enkä katsonut järkeväksi muuttaa toimivaa toteutusta vain sen vuoksi että testit saisi rikkoutumaan. 
Aivan ensimmäisen tekemäni testin agentti "huijasi" valmiiksi, siten, että se kovakoodasi metodin palauttamaan arvon 0, ilman mitään toiminnallisuutta.
Kumpi työnjako, A vai B, tuntui paremmalta, ja miksi?
Minulle B työnjako tuntui paremmalta, sillä oli helpompi sanoittaa tahtomani toiminnallisuus, kuin testin kirjoittaminen ja sitä kautta agentille kommunikoiminen. Voi olla että mikäli kaikki koodi olisi alunperin itse tuottamaani ja tätä kautta ohjelman toiminnallisuus olisi kirkkaana mielessä, testien kirjoittaminen olisi helpompaa, kun ei tarvitsisi arvailla, että mitä minkäkin metodin olisi hyvä palauttaa.
