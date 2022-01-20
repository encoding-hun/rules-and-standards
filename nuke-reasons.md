## 1) Általános
  - 1.1) A szabályzatok nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
  - 1.2) NUKE requestet bárki kérhet, a jogosság megvizsgálása a NUKE Council feladata.
  - 1.3) A Council döntése nem felülbírálható. A hiba azonos csapat által való elhárítása után a release `unnuked` flaget kap.
  - 1.4) Több ok `_` (underscore) karakterrel fűzendő össze. pl. `bad.res_bad.crop`.
  - 1.5) A NUKE reason kizárólag kisbetűket tartalmazhat.
  - 1.6) A szabályzattól notorikusan eltérő csapatok permanens bant kapnak.
  - 1.7) Egyéb értelmező tagek kizárólag angol nyelven használhatóak: pl. `wrong.format_mono.audio.should.be.aac`
  - 1.8) Nuke indoknak használhatóak a szabályzatban található pontok említése is. Ekkor az említett pont sérül valamely módon.
  - 1.9) A szabályzat adott pontjának létrejötte/módosítása előtt készült release nem NUKE-olható, ha csak a változtatott pontban hibás és a változtatást megelőző szabályzat szerint rendben volt. Kérdés esetén a commit history ad támpontot.
  - 1.10) `PROPER` kizárólag technikai hiba (technical flaw) esetén adható ki másik csapat munkájára.
  - 1.11) `READ.NFO` akkor adható ki, ha a korábbi release nem technikailag hibás, de minőségben gyengébb, vagy valami apróság hiányzik (pl. chapterlist), ami még nem indokol `PROPER`-t. 
  - 1.12) A `PROPER` és `READ.NFO` megjelölésű release-ekhez kötelező `proof`. Jobb kép esetén összehasonlítás (comparison), hangcsúszás (`oos`) esetén kép a csúszásról. Apróságok esetén elég ezt az `NFO`-ban jelezni, pl. hiányzó felirat, hiányzó chapterlist, stb. Kivétel, ha az ok egyértelmű (pl. egyértelműen jobb forrású hang).
    - 1.12.1) Kérdésesség esetén a Council utólag is bekérhet `proof`-ot. Ennek pótlásának elmulasztása nuke-ot eredményez `dupe` reasonnal.
  - 1.13) Saját release javítása esetén a korábbi release `unnuke`-ot kap, jelölve a javítást.
  - 1.14) Komolyabb képi problémák javítására a `RERiP` tag használata, minden egyébre a `REPACK` tag használata javasolt, kivéve ha a probléma egyszerűen javítható (pl. `bad.dirname`, `NFO` hibák), amikor elég ezt egyszerűen átírni.

## 2) Indokok
  - 2.1) Technikai hibák (technical flaws) -- ezek `PROPER`-elhetőek.
    - 2.1.1) Video:
      - `bad.res` = hibás felbontás
      - `bad.crop` = hibás cropolás
      - `bad.colorimetry = bad.colormatrix` = `--colormatrix` hibás használata
      - `bad.primaries` = `--primaries` hibás használata
      - `bad.transfer` = `--transfer` hibás használata
      - `bad.deinterlace` = hibás deinterlace-elés, általában sávozódó videó és/vagy egyéb képi artifactek
      - `bad.ivtc` = vegyes félképek hibás eltávolítása
      - `dupe.frames` = duplázott képkockák, általában hibás deinterlace-elés/IVTC eredménye (kivétel, ha a forrás is ilyen és nem érhető el jobb, pl. BBC iPlayer; ilyen esetekben javasolt egy újrakódolt release készítése `READ.NFO` tag használata mellett)
      - `bitstarved = undersized` = szükségesnél jelentősen alacsonyabb bitráta
      - `bloated = oversized` = szükségesnél jelentősen magasabb bitráta
      - `upscaled` = felskálázott kép (forrás és kész encode is) példák kép felskálázottság ellenőrzésére:\
      `Interleave(last, last.AutoResize("720").AutoResize("1080").Subtitle("1080 -> 720 -> 1080"))` (720p upscale)\
      `Interleave(last, last.AutoResize("480").AutoResize("1080").Subtitle("1080 -> 480 -> 1080"))` (480p upscale)\
      (AutoResize z_Spline36Resize-t használ alapértelmezetten)
      - `tonemapped` = UHD forrásból tonemapping (HDR->SDR) segítségével készített 8 bites videó
      - `forbidden.encoder` = tiltott encoder használata
      - `compressed.src` = már tömörített forrás használata
      - `bad.video` = a kész encode tömörítési hibákat tartalmaz; nem YUV420 formátumú
      - `abr.forbidden` = 1 pass ABR encode tiltott
      - `interlaced` = deinterlacing elmulasztása
      - `wrong.fps = bad.fps` = hibás FPS használata
      - `wrong.resizer` = nem megfelelő resizer használata (pl. `Nearest Neighbor`, `Bilinear`, `Bicubic`)
      - `wrong.ref = insufficient.ref` = kevés referenciakép használata
      - `wrong.bframes = insufficient.bframes` = 5 (HD)/8 (SD)-nál kevesebb egymás utána B frame
      - `not.dxva` = nem DXVA kompatibilis videó
      - `wrong.level` = nem megfelelő Level használata encode esetén (x264: SD = L4.1; HD < 60 fps = L4.1; HD >= 60 fps = L4.2; x265: L5.1)
      - `no.8x8dct` = 8x8-as DCT transzformáció kikapcsolása
      - `wrong.partitions` = kevés partíció használata
      - `wrong.me` = `umh`-nál rosszabb mozgáskereső algoritmus használata
      - `wrong.merange = insufficient.merange` = túl kicsi mozgáskeresési vektor használata (20 (HD)/24 (SD)-nél kevesebb)
      - `wrong.sar` = nem négyzet alakú pixelek használata
      - `wrong.range` = nem Limited color range használata
      - `no.deblock` = deblock filter kikapcsolása
      - `no.aq` = adaptív kvantálás kikapcsolása
      - `invalid.vbv` = túl magas VBV értékek használata
      - `shifted.video` = bizonyos forrásfilterek (pl. régi FFMS2) beszúrt/eldobott egy frame-et a kép elejéről, ezáltal eltolva azt a hanghoz képest (min. 100 ms csúszás)
      - `extra.frames`/`missing.frames` = videóhoz hozzáadott, hiányzott frame-ek (kivéve ha videó végéről hiányzik `1` frame és az fekete)

    - 2.1.2) Audio:
      - `wrong.audio.format` = nem megfelelő formátumú hang használata
      - `oversized.audio` = indokolatlanul nagy méretű hang használata
      - `upscaled = upconverted.audio` = a kész encode bitrátája/csatornaszáma/bitmélysége indokolatlanul magasabb, mint a forrásé
      - `starved.audio` = a kész encode bitrátája nagyon alacsony, azaz hallható minőségromlást okoz a tömörítés
      - `audio.oos` = hang csúszik a képhez képest
      - `upsampled` = az eredeti hangnál magasabb mintavételezés használata
      - `downsampled` = az eredeti hangnál alacsonyabb mintavételezés használata
      - `forbidden.audio.encoder` = tiltott hang encoder használata (pl. FFmpeg használata nem compatibility `AC3` és `E-AC3` hangokhoz)
      - `wrong.stretching.algo` = nem megfelelő hangnyújtás használata
      - `missing.compatibility.track` = hiányzó compatibility track

    - 2.1.3) Felirat:
      - `sub.oos` = felirat csúszik a képhez képest
      - `missing.forced.subs` = hiányzó forced felirat
      - `hardsubbed` = kódolás során égetett felirat
      - `wrong.character.coding` = hibásan beállított karakterkódolás

    - 2.1.4) Egyéb:
      - `watermarked` = bármilyen módon vízjelzett release (részletezhető, pl. `audio.watermarked`)
      - `bad.container` = MP4 (kivétel Dolby Vision esetén) és hasonló vicces konténer használata
      - `incomplete` = a forrással nem azonos hosszúságú, vágott tartalom (részletezhető, pl. hiányos hang esetén `incomplete.audio`)
      - `no.nfo` = hiányzó NFO
      - `compressed` = tömörített formátum
      - `password.protected` = bármilyen módon jelszavazott állomány
      - `drm.not.removed` = bármilyen jellegű DRM maradt a release-en

  - 2.2) Kevésbé súlyos, nem technikai hibák -- ezek nem `PROPER`-elhetőek. Indokolt esetben `READ.NFO` kiadható rá.
    - 2.2.1) Video:
      - `obsolete.encoder` = túl régi encoder használata
      - `delayed.video` = MKV-ban flagelt video delay

    - 2.2.2) Audio:
      - `audio.longer.than.video` = a hangsáv több, mint 1 másodperccel túlnyúlik a videón
      - `delayed.audio` = MKV-ban flagelt audio delay (`PROPER`-elhető, ha hossza meghaladja az 500 ms-t és/vagy lejátszási problémákat okoz)
      - `missing.audio.lang.tag` = hiányzó audionyelv tag MKV-ban és/vagy dirname-ben

    - 2.2.3) Felirat:
      - `invalid.sub.entries` = olyan sorok, melyek átfednek másokkal, a film után játszódnának le, hosszuk 5 ms-nél rövidebb, vagy nem tartozik a filmhez (utóbbi alól kivétel a gyárilag bennelévő `Fordított: XY` és a fansuboknál a forrásoldal, fordító neve)
      - `missing.subs.lang.tag` = hiányzó feliratnyelv tag MKV-ban

    - 2.2.4) Egyéb:
      - `dupe` = DUPE release, azaz egy korábbival megegyezik, vagy közel azonos
      - `grp.req` = csapat kérése (`PROPER`-elhető, ha technical flaw-t is tartalmaz)
      - `get.repack`, `get.rerip` = van új, javított változat azonos csapattól (az eredeti release `unnuked` flag-et kap)
      - `get.proper` = van javított változat másik csapattól
      - `invalid.proper` = indokolatlan proper
      - `invalid.repack` = indokolatlan repack
      - `invalid.int` = dupe elkerülésére használt `iNT` tag
      - `better.source.available` = gyengébb forrás felhasználása, amikor elérhető jobb minőségű; ilyen esetben másik csapat `READ.NFO`-val jelölje a sajátját (konkretizálható, pl. `better.audio.source.available`)
      - `missing.proof` = hiányzó proof
      - `missing.chapterlist` = hiányzó chapterlist
      - `invalid.character` = tiltott karaktert tartalmazó könyvtár és/vagy filenevek (`PROPER`-elhető, ha a lejátszásban gondot okoz, pl. Windows-on tiltott mappanevek, lásd 2.4)-es pontja a szabályzatnak)
      - `invalid.dirname`, `bad.dirname` = nem eredeti vagy angol nyelvű könyvtárnév használata; hiányzó adatok; 255 karakternél hosszabb könyvtárnév
      - `missing.source` = forrás nincs feltüntetve (pontosítható, pl. `missing.audio.source`)
      - `mislabeled` = hibás tag (pl. forrás nem a megjelölt)
      - `nfo.wtf` = NFO érthetetlen vagy értelmezhetetlen

  - 2.3) Nem önálló tagek
    - `poor.quality` = gyatra minőség, több technikai hiba esetén jelezhető, hogy abszolút rossz a release
    - `p2p.shit` = bottom feeder csapatok jelölésére, több bármilyen nuke reason mellé adható
    - `banned.grp` = folyamatosan silány munkát végző csapatok, akik kitiltásban részesültek
