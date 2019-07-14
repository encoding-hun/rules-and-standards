# Hungarian HD x264 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapul a 2009.04.15, 2009.06.08-as magyar és 2011.01.29-es nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új releaset READ.NFO taggel kell ellátni. Minden egyéb DUPE-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba, stb., ekkor PROPER-elhető.

## Általános
 - Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - Kizárólag `.mkv` konténer használata elfogadott.
 - A film csonkítása, trimmelése TILOS.
 - A stáblista amennyiben nem tartalmaz extra jelenetet kódolható alacsonyabb bitrátával.
 - A film tömörítése és darabolása TILOS.
 - A fő MKV mellé ajánlott SFV ellenőrzőösszeg készítése, de nem kötelező.
 - Sample opcionális, amennyiben van, 60-120 másodperc közötti kell, hogy legyen és nem az epizód/film legelejéről. A Sample-t újrakódolás nélkül, a végső encode-ból kell kivágni.
 - mHD, HDLight és egyéb vicces baromságok készítése TILOS!
 - Chapterlist használata UHD BD, BD és HDDVD források esetén KÖTELEZŐ!

## Taggelés
  - Ékezetes karakterek használata TILOS!
  - Lefoglalt karaktereket (`<`,`>`,`:`,`"`,`/`,`\`,`|`,`?`,`*`) könyvtárnévben és filenevekben is TILOS használni!
  - TILOS két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - TILOS a következő könyvárnevek használata: `CON`, `PRN`, `AUX`, `NUL`, `COM1`, `COM2`, `COM3`, `COM4`, `COM5`, `COM6`, `COM7`, `COM8`, `COM9`, `LPT1`, `LPT2`, `LPT3`, `LPT4`, `LPT5`, `LPT6`, `LPT7`, `LPT8` és `LPT9`.
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
    - `WEB-DLRip` megjelölés kerülendő, `WEB-DL`-ből kódolt Rip = `WEBRip`
   - `REPACK` és `RERip` tagok használata kötelező, ha saját releaset javít valaki.
   - `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
   - TV-ből származó hangok esetén `CUSTOM` tag használata kötelező!
   - `RETAiL` tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.

## Források
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása: BD > HDDVD > WEB-DL/WEBRiP > HDTV
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt READ.NFO taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping TILOS, ekkor x265 encode készítendő (lást oda vonatkozó szabályzat).

## Video
  - Minimum `r2800`-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok) muxolunk.
  - TILOS minden olyan x264 használata, amely az alábbi commitot tartalmazza (praktikusan `r2969`, `r2970` és ami erre épül): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs féle vanilla `r2970+1` és tMod `r2970+3`.
  - Házibarkács encoderek használata TILOS!
  - Már kész release alacsonyabb felbontással való újrakódolása (pl. BRRip) SZIGORÚAN TILOS!
  - Kizárólag 8 bites YUV420 (YV12) video megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - Kizárólag progresszív kép megengedett. Amennyiben szükséges deinterlacer vagy ITVC használata kötelező.
  - A video eredeti FPS értékét meg kell tartani. Interlacelt forrás esetén 2 félképből 1-et kell képezni (értsd `50i`-ből `25p`-t kell készíteni). Ez alól kivétel lehet a sportfelvétel, ahol indokolt lehet az `50p`. Ekkor kizárólag QTGMC deinterlacer használható!
  - A videot croppolni kell addig amíg maximum 1-1 px fekete sáv marad.
  - Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line pl.: `bbmod`/`FixColorBrightness`/`BalanceBorders`/`EdgeFixer`
  - A kódolt videó képarányának hibája nem haladhatja meg a 3%-ot (aspect ratio error).
  - A video felskálázása SZIGORÚAN TILOS!
  - A video szélességének és magasságának 2-vel oszthatónak kell lennie.
  - 1080p forrású 1080p encode esetén csak cropolni szabad, resize-olni nem.
  - Resizeoláshoz `z_Spline36Resize` vagy `Spline36ResizeMod` ajánlott, a `Spline36Resize` tartalmaz egy apró chroma shifting bugot, kerülendő. (VapourSynth-et nem érinti.) VapourSynth esetén `Spline64` is ajánlott.
  - Tilos Nearest Neighbor, Bilinear és Bicubic resizer használata.
  - 720p release maximális felbontása `1280x720` lehet.
  - ColorMatrixot, amennyiben a forrás tartalmaz erre vonatkozó információt kötelező flaggelni (tipikusan `BT.709`), amennyiben nem, úgy `undef`-en kell hagyni.
  - ColorPrimaries és Transfer function flaggelése opcionális (háttértudást igényel a stúdió setupról, csak akkor használd, ha tudod mit csinálsz).
    - Bővebb infó: https://mod16.org/hurfdurf/?p=116
  - A maximálisan megengedett referencia képek számának használata kötelező (--ref).
    - `--preset veryslow`/`placebo` magától kiszámolja a legnagyobbat, ami még nem töri meg a kompatibilitást. (Érdemes így csinálni, és akkor nem kell manuálisan számolni.)
    - Kiszámolása: `8388608/(végső szélesség*végső magasság)` -> lefele kerekítés.
    Pl.: `8388608/(1280*640) = 10,24`, `10.24` -> `10`
    `(8388608 = 32768*16*16)` `[32768 a MaxDpbMbs High@4.1-nél, 16*16 egy macroblock]`
  - B framek kikapcsolása TILOS.
  - A készült videónak DXVA-kompatibilisnek kell lennie (max. `High@L4.1`).
  - `CABAC` kikapcsolása TILOS.
  - `8x8dct` kikapcsolása TILOS.
  - Kötelezően használandó partíciók: `i4x4,i8x8,p8x8,b8x8` (default), `p4x4` használata opcionális
  - `me` értéke KIZÁRÓLAG `umh`, `esa` vagy `tesa` lehet.
  - `merange` értéke nem lehet 24-nél kisebb.
  - `subme` értéke nem lehet 8-nál kisebb.
  - Kizárólag 1:1 oldalarányú pixelek használhatóak (`--sar 1:1`).
  - Kizárólag Limited, TV rangeű release készíthető (`16-235`).
  - `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet.
  - `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - Adaptív kvantálás használata kötelező! `--aq-mode>=1`
  - A keyframek közötti maximális távolság `FPS*20` lehet.
  - A video bitrátája UHD BD, BD és HDDVD forrás esetén minimum 8000 kbps, maximum 20 000 kbps lehet, 720p esetén minimum 4000 kbps és maximum 9000 kbps. Ez alól kivétel az anime, ahol a minimum 5000 kbps és 2000 kbps, rendre.
  - WEB-DL, WEBRip és HDTV releasek bitrátája ennél lehet kisebb, de magasabb nem.
  - A készített release bitrátája nem lehet nagyobb, mint a forrásé.
  - Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - HDTV forrás esetén logok maszkolása megengedett.

## Audio
  - Megengedett hangformátumok: `AC3`, `E-AC3`, `DTS`, `AAC`, `FLAC`. `MP3`, `MP2` és egyéb vicces formátumok használata TILOS!
  - Filmek esetén DTS és AC3 encodeolása AAC-be kizárólag a kommentár sáv esetén megengedett.
  - LPCM hangot kötelező FLAC-be (film esetén) vagy AAC-be (kommentár esetén) konvertálni
  - A hangsávok eredeti csatornaszámát meg kell tartani! Kivétel kommentár sávok.
  - AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge`, `Minnetonka`, `Sonic Foundry`)
  - AAC esetében elfogadott encoderek: QAAC, FDK, Nero (csak stereo hangnál használható)
  - 720p releasek esetén `DTS`, `TrueHD`, `DTS-HD.MA` és `DTS:X` hang használata TILOS!
  - 1080p releasek esetén `TrueHD`, `DTS-HD.MA` és `DTS:X` használata TILOS! Ilyen esetekben a core-t használjuk vagy lossless audio-ból kódolunk `DD@640` vagy `DDP@1024` hangot.
  - Amennyiben az érintetlen forráson DTS core található csak:
    - `DDP@1024` kódolása (ajánlott),
    - DTS meghagyása, mellé `DD@640` compatibility track készítése.
  - Lossy hangot csak losslessből szabad kódolni. (Ez alól kivétel ha csak DTS hang elérhető és compatibility track-et készítünk vagy 1080p-re `DDP@1024`-et.)
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - A hangok nyelvét kötelező Language tagben jelezni!
  - Commentary track maximum 2.0 lehet, AC3 esetében maximum 192kbps, AAC esetében `-V 80` - `-V -100` (QAAC) ~ 80-136 kbps.
  - Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. hdtools compare)
  - Resampling-re használható programok: hdtools resample, eac3to, Sound Forge, Audacity.
  - TimeStretchingre használható programok: hdtools tstretch, Prosoniq TimeFactory II, Sound Forge és SONAR `élastique TimeStretch`, Audacity.
  
## Feliratok
 - A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani, hogy mi a forrás)
 - Az opcionálisan mellékelt feliratok kizárólag SRT formátumú és UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - Feliratok képre égetése, hardcodeolása SZIGORÚAN TILOS!
 - A feliratok nyelvét kötelező Language tag-ként beállítani.
 - Title tag használata opcionális.
 - Feliratok sorrendje:
    - magyar forced (ha van)
    - magyar full
    - eredeti forced (ha van)
    - eredeti full
    - eredeti full SDH
  - Forced feliratoknál a Forced flag használata ajánlott.
  - További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a video és hangsávok is beletartoznak).
  - Fansub kizárólag akkor használható, ha nem érhető el retail.

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
    - dupe = DUPE release, azaz egy korábbival megegyezik, vagy közel azonos
    - grp.req = csapat kérése
    - get.repack, get.rerip = van új, javított változat azonos csapattól
    - get.proper = van javított változat másik csapattól
    - bad.res = hibás felbontás
    - bad.crop = hibás croppolás
    - bad.colorimetry = `--colormatrix` hibás használata
    - bad.deinterlace = hibás deinterlacelés, általában sávozódó videó és/vagy egyéb képi artifactek
    - dupe.frames = duplázott képkockák, általában hibás deinterlacelés/IVTC eredménye
    - mislabeled.custom = `CUSTOM` tag elhagyása
    - bitstarved = alacsony bitráta
    - bloated = feleslegesen magas bitráta
    - upscaled = felskálázott kép/hang
      példák kép felskálázottság ellenőrzésére:
      `Interleave(last,last.AutoResize("720").AutoResize("1080").Subtitle("1080 -> 720 -> 1080"))` (720p upscale)
      `Interleave(last,last.AutoResize("480").AutoResize("1080").Subtitle("1080 -> 480 -> 1080"))` (480p upscale)
      (AutoResize z_Spline36Resize-t használ)
    - audio.oos = hang csúszik a képhez képest
    - sub.oos = felirat csúszik a képhez képest
    - nfo.wtf = NFO érthetetlen vagy értelmezhetetlen
    - Tobb ok `_` karakterrel fűzendő össze. pl. `bad.res_bad.crop`.
    - A READ.NFO-khoz és a PROPER-ekhez kötelező proof. Jobb kép esetén comparison, oos esetén kép a csúszásról.
    - A szabályzattól notorikusan eltérő csapatok permanens bant kapnak.

## Aláírták és tudomásul vették

## Oldalak, akik elfogadták

## Érvényes
  2019-??-??-től

## Banned grps
