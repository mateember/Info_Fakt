3meret
SELECT nev,terulet
FROM vt 
WHERE kategoria = "TK"
ORDER BY terulet DESC
;
4kicsi
SELECT vt.nev, vt.terulet, igazgatosag.nev
FROM igazgatosag, vt
WHERE igazgatosag.id = vt.igid and kategoria = "TK"
ORDER by terulet LIMIT 1;
;
5arany
SELECT MAX(vt.terulet) / (MIN(vt.terulet) +1) as arány
FROM vt
WHERE vt.kategoria = "TT"
;
6duna
SELECT DISTINCT telepules.nev
FROM igazgatosag, telepules, kapcsolo, vt
WHERE igazgatosag.id = vt.igid AND vt.id = kapcsolo.vtid and kapcsolo.telepid = telepules.id AND igazgatosag.nev="Duna-Ipoly Nemzeti Park Igazgatóság"
ORDER BY telepules.nev
;
7legtobb
SELECT vt.nev,COUNT(telepules.nev) as darabszám
FROM telepules, vt, kapcsolo
WHERE vt.id = kapcsolo.vtid AND kapcsolo.telepid = telepules.id AND vt.kategoria = "NP"
GROUP BY vt.nev  
ORDER BY `darabszám`  DESC
LIMIT 1;
8ujnev
SELECT vt.nev
FROM vt
WHERE vt.nev NOT IN
(SELECT vt.nev
FROM vt, kapcsolo, telepules
WHERE vt.id = kapcsolo.vtid and kapcsolo.telepid = telepules.id and LOCATE(telepules.nev, vt.nev))
;
