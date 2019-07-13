HD felbontású (1080p, 720p), x264-es kódolású filmekre vonatkozó szabályok és előírások

Érvényes: 2019-??-??-től

Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új releaset READ.NFO taggel kell ellátni. Minden egyéb DUPE-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba, stb., ekkor PROPER-elhető.

## Intro
  Alapul a 2009.04.15, 2009.06.08-as magyar és 2011.01.29-es nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.

## Általános
 - Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - Kizárólag `.mkv` konténer használata elfogadott.
 - A film csonkítása, trimmelése TILOS.
 - A stáblista amennyiben nem tartalmaz extra jelenetet kódolható alacsonyabb bitrátával.
 - A film tömörítése és darabolása TILOS.
 - A fő MKV mellé ajánlott SFV ellenőrzőösszeg készítése, de nem kötelező.
 - Sample opcionális, amennyiben van, 60-120mp közötti kell, hogy legyen és nem az epizód/film legelejéről.

## Taggelés
  - Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    
    - Sorozatok:
    `[series.name].[season].[resolution].[source].[audio codec].[video codec].[language]-[group]`
    
    - Filmek:
    `[movie title].[year].[resolution].[source].[audio codec].[video codec].[language]-[group]`
  - A könyvtár és fájlok nevének maximális hossza 252 karakter lehet.
  - `[audio codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - WEB-DL és WEBRip forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`)
  - WEB-hez további guide:
    - Az minősül WEB-DL-nek, ami nem lett újrakódolva az oldalról való leszedés után.
    - Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-t használ.
    - Egy WEB-DL nem feltétlenül jobb mint egy WEBRip (pl. `2160p.WEB-DL`-ből kódolt `720p.WEBRip` vs `720p.WEB-DL`)

## Források
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása: BD > HDDVD > WEB-DL/WEBRiP > HDTV
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt READ.NFO taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping tilos, ekkor x265 encode készítendő (lást oda vonatkozó szabályzat).

## Video
  - Minimum r2800-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok) muxolunk.
  - TILOS minden olyan x264 használata, amely az alábbi commitot tartalmazza (praktikusan `r2969`, `r2970` és ami erre épül): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs féle r2970+1 és tmod r2970+3.
  - Házibarkács encoderek használata TILOS!
  - Kizárólag 8 bites YUV420 (YV12) video megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - A video eredeti FPS értékét meg kell tartani.

## Audio
  - Megengedett hangformátumok: `AC3`, `E-AC3`, `DTS`, `AAC`, `FLAC`. `MP3`, `MP2` és egyéb vicces formátumok használata TILOS!
  - AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge`, `Minnetonka`, `Sonic Foundry`)
  - AAC esetében elfogadott encoderek: QAAC, FDK, Nero (csak stereo hangnál használható)
  - 720p releasek esetén DTS hang használata TILOS!
  - 1080p releasek esetén `TrueHD`, `DTS-HD.MA` és `DTS:X` használata TILOS! Ilyen esetekben a core-t használjuk vagy master audio-ból kódolunk `DD@640` vagy `DDP@1024` hangot.
  - Lossy hangot csak master audioból (lossless) szabad kódolni.
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - Commentary track maximum 2.0 lehet, AC3 esetében maximum 192kbps, AAC esetében `-V 80` - `-V -100` (qaac)
  
## Feliratok
 - A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani, hogy mi a forrás)
 - Az opcionálisan mellékelt feliratok kizárólag SRT formátumú és UTF8-BOM vagy ANSI kódolásúak lehetnek.
 - A feliratok nyelvét kötelező Language tag-ként beállítani.
 - Title tag használata opcionális.
 - Feliratok sorrendje:
    - magyar forced (ha van)
    - magyar full
    - eredeti forced (ha van)
    - eredeti full
    - eredeti full sdh

## NFO
 - NFO használata kötelező.
 - Az NFO nyelve angol és/vagy magyar.
 - Magyar nyelvű NFO esetén az angol kifejezések szakszerű fordításának használata kötelező (ebben segít a Wikipedia).
 - Az NFO-ban kötelező a következő információkat feltüntetni:
      * Release címe
      * Release készítésének ideje
      * Eredeti cím
      * IMDb URL
      * Video és hang forrása (feliratnál jelölni kell, amennyiben fansub)
      * A release mérete (csak a fő mkv, B, kB, MB, GB, KiB, MiB és GiB elfogadott)
      * Videóhoz használt encoder
      * Video felbontása
      * Video bitrátája
      * Video FPS-e
      * Audio sávok nyelvei
      * Audio sávok típusai
      * Audio sávok csatornaszáma
      * Audio sávok bitrátája
      * Audio mintavételezési rátája (Sample rate)
      * Feliratok nyelve
  
## NUKE
 - A szabályzat nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
 - NUKE requestet bárki kérhet, a jogosság megvizsgálása a NUKE Council feladata
 - Indokok taggelése:
    - bad.res = hibás felbontás
    - bitstarved = alacsony bitráta
    - bloated = feleslegesen magas bitráta
    - audio.oos = hang csúszik a képhez képest
    - sub.oos = felirat csúszik a képhez képest
    - nfo.wtf = NFO érthetetlen vagy értelmezhetetlen
    - A READ.NFO-khoz és a PROPER-ekhez kötelező proof. Jobb kép esetén comparison, oos esetén kép a csúszásról.

## Aláírták és tudomásul vették

## Oldalak, akik elfogadták
