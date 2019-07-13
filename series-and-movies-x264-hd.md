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
 - Sample opcionális, amennyiben van, 60-120 másodperc közötti kell, hogy legyen és nem az epizód/film legelejéről.

## Taggelés
  - Ékezetes karakterek használata könyvtárnevekben TILOS!
  - Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    
    - Sorozatok:
    `[series.name].[season].[resolution].[source].[audio codec].[video codec].[language]-[group]`
    
    - Filmek:
    `[movie title].[year].[resolution].[source].[audio codec].[video codec].[language]-[group]`
  - A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - `[audio codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - WEB-DL és WEBRip forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`)
  - WEB-hez további guide:
    - Az minősül WEB-DL-nek, ami nem lett újrakódolva az oldalról való leszedés után.
    - Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-t használ.
    - Egy WEB-DL nem feltétlenül jobb mint egy WEBRip (pl. `2160p.WEB-DL`-ből kódolt `720p.WEBRip` vs `720p.WEB-DL`)
    - `Rip` és `RiP` megjelölés is elfogadott.

## Források
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása: BD > HDDVD > WEB-DL/WEBRiP > HDTV
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt READ.NFO taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping tilos, ekkor x265 encode készítendő (lást oda vonatkozó szabályzat).

## Video
  - Minimum r2800-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok) muxolunk.
  - TILOS minden olyan x264 használata, amely az alábbi commitot tartalmazza (praktikusan `r2969`, `r2970` és ami erre épül): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs féle `r2970+1` és tmod `r2970+3`.
  - Házibarkács encoderek használata TILOS!
  - Kizárólag 8 bites YUV420 (YV12) video megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - A video eredeti FPS értékét meg kell tartani.
  - A videot croppolni kell addíg amíg maximum 1-1 px fekete sáv marad.
  - Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
  - A kódolt videó képarányának hibája nem haladhatja meg a 3%-ot (aspect ratio error).
  - A video felskálázása SZIGORÚAN TILOS!
  - A video szélességének és magasságának 2-vel oszthatónak kell lennie.
  - 1080p esetén a szélesség 1920-crop értéke kell legyen. 720p esetén a szélességnek 1280 px-nek kell lennie.
  - ColorMatrixot, amennyiben a forrás tartalmaz erre vonatkozó információt kötelező flaggelni (tipikusan `BT.709`), amennyiben nem, úgy `undef`-en kell hagyni.
  - ColorPrimaries és Transfer function flaggelése opcionális.
  - A maximálisan engedett referencia képek számának használata kötelező (`--ref`).
  - B framek használata kötelező.
  - A készült videónak `Level 4.1@High` kompatibilisnek kell lennie.
  - `CABAC` használata kötelező.
  - 8x8dct használata kötelező.
  - Kötelezően használandó partíciók: i4x4,i8x8,p8x8,b8x8; p4x4 használata opcionális
  - `merange` értéke nem lehet 24-nél kisebb
  - `subme` értéke nem lehet 10-nél kisebb
  - Kizárólag 1:1 oldalarányú pixelek használhatóak (`--sar 1:1`)
  - Kizárólag Limited, TV rangeű release készíthető (`16-235`)
  - `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet.
  - `deblock` filter használata kötelező.

## Audio
  - Megengedett hangformátumok: `AC3`, `E-AC3`, `DTS`, `AAC`, `FLAC`. `MP3`, `MP2` és egyéb vicces formátumok használata TILOS!
  - LPCM hangot kötelező FLAC-be (film esetén) vagy AAC-be (kommentár esetén) konvertálni
  - AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge`, `Minnetonka`, `Sonic Foundry`)
  - AAC esetében elfogadott encoderek: QAAC, FDK, Nero (csak stereo hangnál használható)
  - 720p releasek esetén `DTS`, `TrueHD`, `DTS-HD.MA` és `DTS:X` hang használata TILOS!
  - 1080p releasek esetén `TrueHD`, `DTS-HD.MA` és `DTS:X` használata TILOS! Ilyen esetekben a core-t használjuk vagy master audio-ból kódolunk `DD@640` vagy `DDP@1024` hangot.
  - DTS hang esetén DD+ vagy AC3 compatibility track használata ajánlott.
  - Lossy hangot csak master audioból (lossless) szabad kódolni. Ez alól kivétel ha csak DTS hang elérhető és compatibility track-et készítünk.
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - Commentary track maximum 2.0 lehet, AC3 esetében maximum 192kbps, AAC esetében `-V 80` - `-V -100` (QAAC) ~ 80-136 kbps
  
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
    - eredeti full SDH

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
    - bad.crop = hibás croppolás
    - bad.colorimetry = hibás ColorMatrix/Primaries/Transfer használata
    - bitstarved = alacsony bitráta
    - bloated = feleslegesen magas bitráta
    - upscaled = felskálázott kép/hang
    - audio.oos = hang csúszik a képhez képest
    - sub.oos = felirat csúszik a képhez képest
    - nfo.wtf = NFO érthetetlen vagy értelmezhetetlen
    - A READ.NFO-khoz és a PROPER-ekhez kötelező proof. Jobb kép esetén comparison, oos esetén kép a csúszásról.

## Aláírták és tudomásul vették

## Oldalak, akik elfogadták
