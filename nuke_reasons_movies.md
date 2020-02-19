## Általános
 - A szabályzatok nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
 - NUKE requestet bárki kérhet, a jogosság megvizsgálása a NUKE Council feladata
 - Több ok `_` vagy `,` karakterrel fűzendő össze. pl. `bad.res_bad.crop` vagy `bad.res, bad.crop`.
 - A `READ.NFO`-khoz és a `PROPER`-ekhez kötelező proof. Jobb kép esetén comparison, `oos` esetén kép a csúszásról.
 - A szabályzattól notorikusan eltérő csapatok permanens bant kapnak.

## Indokok
 - Video:
    - `bad.res` = hibás felbontás
    - `bad.crop` = hibás cropolás
    - `bad.colorimetry` = `--colormatrix` hibás használata
    - `bad.deinterlace` = hibás deinterlace-elés, általában sávozódó videó és/vagy egyéb képi artifactek
    - `bad.ivtc` = vegyes félképek hibás eltávolítása
    - `dupe.frames` = duplázott képkockák, általában hibás deinterlacelés/IVTC eredménye
    - `bitstarved` = szükségesnél jelentősen alacsonyabb bitráta
    - `bloated` = szükségesnél jelentősen magasabb bitráta
    - `upscaled` = felskálázott kép/hang<br />
       példák kép felskálázottság ellenőrzésére:
      `Interleave(last,last.AutoResize("720").AutoResize("1080").Subtitle("1080 -> 720 -> 1080"))` (720p upscale)<br />
      `Interleave(last,last.AutoResize("480").AutoResize("1080").Subtitle("1080 -> 480 -> 1080"))` (480p upscale)<br />
      (AutoResize z_Spline36Resize-t használ)
    
 - Audio:
    - `audio.oos` = hang csúszik a képhez képest
    - `upsampled` = az eredeti hangnál magasabb mintavételezés használata
    - `downsampled` = az eredeti hangnál alacsonyabb mintavételezés használata
    
 - Felirat:
    - `sub.oos` = felirat csúszik a képhez képest
    - `missing.forced` = hiányzó forced felirat

 - Egyéb:
    - `dupe` = DUPE release, azaz egy korábbival megegyezik, vagy közel azonos
    - `grp.req` = csapat kérése
    - `get.repack`, `get.rerip` = van új, javított változat azonos csapattól
    - `get.proper` = van javított változat másik csapattól
    - `poor.quality` = gyatra minőség
    - `nfo.wtf` = NFO érthetetlen vagy értelmezhetetlen
