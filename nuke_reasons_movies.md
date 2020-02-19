## Általános
 - A szabályzatok nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
 - NUKE requestet bárki kérhet, a jogosság megvizsgálása a NUKE Council feladata
 - Több ok `_` vagy `,` karakterrel fűzendő össze. pl. `bad.res_bad.crop` vagy `bad.res, bad.crop`.
 - A NUKE reason kizárólag kisbetűket tartalmazhat.
 - A `READ.NFO`-khoz és a `PROPER`-ekhez kötelező proof. Jobb kép esetén comparison, `oos` esetén kép a csúszásról. Kivétel ha az ok egyértelmű (pl. jobb forrású hang).
 - A szabályzattól notorikusan eltérő csapatok permanens bant kapnak.
 - Egyéb értelmező tag-ek kizárólag angol nyelven használhatóak: pl. `wrong.format_mono.audio.should.be.aac`

## Indokok
 - Video:
    - `bad.res` = hibás felbontás
    - `bad.crop` = hibás cropolás
    - `bad.colorimetry` = `--colormatrix` hibás használata
    - `bad.deinterlace` = hibás deinterlace-elés, általában sávozódó videó és/vagy egyéb képi artifactek
    - `bad.ivtc` = vegyes félképek hibás eltávolítása
    - `dupe.frames` = duplázott képkockák, általában hibás deinterlacelés/IVTC eredménye
    - `bitstarved = undersized` = szükségesnél jelentősen alacsonyabb bitráta
    - `bloated = oversized` = szükségesnél jelentősen magasabb bitráta
    - `upscaled` = felskálázott kép (forrás és kész encode is)
       példák kép felskálázottság ellenőrzésére:
      `Interleave(last,last.AutoResize("720").AutoResize("1080").Subtitle("1080 -> 720 -> 1080"))` (720p upscale)
      `Interleave(last,last.AutoResize("480").AutoResize("1080").Subtitle("1080 -> 480 -> 1080"))` (480p upscale)
      (AutoResize z_Spline36Resize-t használ)
    - `tonemapped` = UHD forrásból tonemapping segítségével készített 8 bites videó
    - `obsolete.encoder` = túl régi encoder használata
    - `forbidden.encoder` = tiltott encoder használata
    - `compressed.src` = már tömörített forrás használata
    - `bad.video` = a kész encode tömörítési hibákat tartalmaz; nem YUV420 formátumú; ABR kódolással készült
    - `interlaced` = deinterlacing elmulasztása
    - `wrong.fps` = hibás FPS használata
    - `wrong.resizer` = nem megfelelő resizer használata (pl. `Nearest Neighbor`, `Bilinear`, `Bicubic`)
    - `wrong.ref` = kevés referenciakép használata
    - `wrong.bframes` = 3-nál kevesebb egymás utána B frame
    - `not.dxva` = nem DXVA kompatibilis videó
    - `wrong.level` = L4.1-nél magasabb Level használata
    - `no.8x8dct` = 8x8-as DCT transzformáció kikapcsolása
    - `wrong.partitions` = kevés partíció használata
    - `wrong.me` = `umh`-nál rosszabb mozgáskereső algoritmus használata
    - `wrong.merange` = túl kicsit mozgáskeresési vektor használata
    - `wrong.sar` = nem négyzet alakú pixelek használata
    - `wrong.range` = nem Limited color range használata
    - `no.deblock` = deblock filter kikapcsolása
    - `no.aq` = adaptív kvantálás kikapcsolása
    - `invalid.vbv` = túl magas VBV értékek használata
    
 - Audio:
    - `wrong.audio.format` = nem megfelelő formátumú hang használata
    - `oversized.audio` = indokolatlanul nagy méretű hang használata
    - `upscaled` = a kész encode bitrátája/csatornaszáma magasabb, mint a forrásé
    - `audio.oos` = hang csúszik a képhez képest
    - `upsampled` = az eredeti hangnál magasabb mintavételezés használata
    - `downsampled` = az eredeti hangnál alacsonyabb mintavételezés használata
    - `forbidden.audio.encoder` = tiltott hang encoder használata
    - `wrong.stretching.algo` = nem megfelelő hangnyújtás használata
    
 - Felirat:
    - `sub.oos` = felirat csúszik a képhez képest
    - `missing.forced` = hiányzó forced felirat
    - `wrong.character.coding` = hibásan beállított karakterkódolás
    - `hardsubbed` = kódolás során égetett felirat

 - Egyéb:
    - `dupe` = DUPE release, azaz egy korábbival megegyezik, vagy közel azonos
    - `grp.req` = csapat kérése
    - `get.repack`, `get.rerip` = van új, javított változat azonos csapattól
    - `get.proper` = van javított változat másik csapattól
    - `invalid.proper` = indokolatlan proper
    - `invalid.repack` = indokolatlan repack
    - `invalid.int` = dupe elkerülésére használt `iNT` tag
    - `bad.container` = MP4 (kivétel Dolby Vision esetén) és hasonló vicces konténer használata
    - `incomplete` = a forrással nem azonos hosszúságú, vágott tartalom
    - `missing.chapterlist` = hiányzó chapterlist
    - `invalid.character` = tiltott karaktert tartalmazó könyvtár és/vagy filenevek
    - `invalid.dirname` = nem eredeti vagy angol nyelvű könyvtárnév használata; hiányzó adatok; 255 karakternél hosszabb könyvtárnév
    - `missing.source` = forrás nincs feltüntetve
    - `mislabeled` = hibás tag; pl. forrás nem a megjelölt
    - `poor.quality` = gyatra minőség
    - `no.nfo` = hiányzó NFO
    - `nfo.wtf` = NFO érthetetlen vagy értelmezhetetlen
    - `compressed` = tömörített formátum
