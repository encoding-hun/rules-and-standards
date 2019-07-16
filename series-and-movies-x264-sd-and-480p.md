# Hungarian SD x264 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapul a 2009.04.15, 2009.06.08-as magyar és 2011.01.29-es nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új releaset READ.NFO taggel kell ellátni. Minden egyéb DUPE-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor PROPER-elhető.

## Általános
 - Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - Kizárólag `.mkv` konténer használata elfogadott.
 - A film csonkítása, trimmelése TILOS.
 - A stáblista amennyiben nem tartalmaz extra jelenetet kódolható alacsonyabb bitrátával.
 - A film tömörítése és darabolása TILOS.
 - A fő MKV mellé SFV ellenőrzőösszeg készítése ajánlott, de nem kötelező.
 - Sample opcionális, amennyiben van, 60-120 másodperc közötti kell, hogy legyen és nem az epizód/film legelejéről. A Sample-t újrakódolás nélkül, a végső encode-ból kell kivágni és egy `Sample` nevű mappába vagy a fő MKV mellé kell helyezni.
 - Chapterlist használata UHD BD, BD, HDDVD és DVD források esetén KÖTELEZŐ!
 - `480p` és `SD` release DUPE-olja egymást. Ha már van `SD` encode, az nem cserélhető `480p`-re csak a felbontás miatt, sem fordítva. `PROPER` vagy `READ.NFO` esetén lehet `SD`-t `480p`-vel javítani/upgrade-elni, és fordítva.

## Taggelés
  - Ékezetes karakterek használata TILOS!
  - Engedélyezett karakterek: `a-z` `A-Z` `0-9` `.` `-` `_` `+`
  - TILOS két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - A következő nevek nem használhatók könyvtár- és fájlnevek elején ponttal elválasztva: `CON`, `PRN`, `AUX`, `NUL`, `COM*`, `LPT*` (ahol `*` egy számot jelöl).
    - TILOS: `Con.Man.2018.DVDRip.x264.HUN-XYZ`
      - OK: `Con_Man.2018.DVDRip.x264.HUN-XYZ`
    - TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - OK: `The.Con.Is.On.2018.DVDRip.x264.HUN-XYZ`
  - Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - Sorozatok:
    `[series.name].[season].[source].[audio.codec].[video.codec].[language]-[group]`
    - Filmek:
    `[movie.title].[year].[source].[audio.codec].[video.codec].[language]-[group]`
    - `[audio.codec]` opcionális.
    - 480p release esetén `480p` tag is kell `[source]` előtt.
    - SD és RETAiL forrás esetén `[source]`-t a forrás milyensége + `Rip` taggal képezzük, pl. `BDRip`, `DVDRip`.
  - A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - WEB-DL és WEBRip forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEBRip`, `AMZN.WEBRip`)
  - WEB-hez további guide:
    - Az minősül WEB-DL-nek, ami nem lett újrakódolva az oldalról való leszedés után.
    - Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-t használ.
    - Egy WEB-DL nem feltétlenül jobb mint egy WEBRip (pl. `2160p.WEB-DL`-ből kódolt SD `WEBRip` vs SD `WEB-DL`)
    - `WEB-DLRip` megjelölés kerülendő, `WEB-DL`-ből kódolt Rip = `WEBRip`
   - `Rip` és `RiP` megjelölés is elfogadott.
   - `REPACK` és `RERip` tagok használata kötelező, ha saját releaset javít valaki.
   - `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
   - TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
   - `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD/DVD lemezről származik.

## Források
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása:<br />
   `(UHD)` `BluRay` > `HDDVD`, `D-VHS` > `WEBRip` ((U)HD `WEB-DL`-ből) > `DVD` > `WEB-DL` > `HDTV` > `PDTV` > `Analog TV`, `VHS`
   `P2P` > `Scene` (kivétel RETAiL lemezek esetén)
   - `WEBRip` alacsonyabb felbontással való újratömörítése TILOS!
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt READ.NFO taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping TILOS, ekkor x265 encode készítendő (lást oda vonatkozó szabályzat).
   - Muxolni kizárólag olyan már kész releasere szabad, amely megfelel ezen szabályzatban rögzített pontoknak. Saját encodeok készítése ajánlott.

## Video
  - Minimum `r2800`-as x264-as használata kötelező.
  - TILOS minden olyan x264 használata, amely az alábbi commitot tartalmazza (praktikusan `r2969`, `r2970` és ami erre épül): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs féle vanilla `r2970+1` és tMod `r2970+3`.
  - Házibarkács encoderek használata TILOS!
  - Már kész release alacsonyabb felbontással való újrakódolása (pl. BRRip) SZIGORÚAN TILOS!
  - Kizárólag 8 bites YUV420 (YV12) videó megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - Kizárólag progresszív kép megengedett. Amennyiben szükséges deinterlacer vagy IVTC használata kötelező.
  - A videó eredeti FPS értékét meg kell tartani. Interlacelt forrás esetén 2 félképből 1-et kell képezni (értsd `50i`-ből `25p`-t kell készíteni). Ez alól kivétel lehet a sportfelvétel, ahol indokolt lehet az `50p`. Ekkor kizárólag `QTGMC` deinterlacer használható!
  - A videót cropolni kell addig amíg maximum 1-1 px fekete sáv marad.
  - Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line pl.: `bbmod`/`FixColorBrightness`/`BalanceBorders`/`EdgeFixer`
  - A kódolt videó képarányának hibája nem haladhatja meg a 3%-ot (aspect ratio error).
  - A videó felskálázása SZIGORÚAN TILOS!
  - A videó felbontása mod2 kell legyen. (Nem mod16, ez nem XviD.)
  - Resizeoláshoz `z_Spline36Resize` vagy `Spline36ResizeMod` ajánlott, a `Spline36Resize` tartalmaz egy apró chroma shifting bugot, kerülendő. (VapourSynth-et nem érinti.) VapourSynth esetén `Spline64` is ajánlott.
  - Tilos `Nearest Neighbor`, `Bilinear` és `Bicubic` resizer használata.
  - SD release maximális szélessége `720 px` lehet (`AutoResize("SD")`)
  - Amennyiben a forrás szélessége kevesebb, mint `720 px` széles, úgy a kész encodenak a `forrás-crop` szélesnek kell lennie.
  - Alacsonyabb felbontás kizárólag akkor megengedett, ha irreálisan magas bitrátát kapnánk a fentebb említett szélességek esetén.
  - 480p release maximális felbontása `854x480` lehet. (`AutoResize("480")`)
  - ColorMatrixot, amennyiben a forrás tartalmaz erre vonatkozó információt KÖTELEZŐ flaggelni (tipikusan `BT.709` BD esetén vagy `BT.470B/G` PAL DVD esetén), amennyiben nem, úgy `undef`-en kell hagyni.
  - ColorPrimaries és TransferFunction flaggelése opcionális (háttértudást igényel a stúdió setupról, csak akkor használd, ha tudod mit csinálsz). Bővebb infó: https://mod16.org/hurfdurf/?p=116
  - Kötelező 16 referenciaképet használni (`--ref 16`).
  - B frame-ek kikapcsolása TILOS.
  - A készült videónak DXVA-kompatibilisnek kell lennie (max. `High@L4.1`).
  - `CABAC` kikapcsolása TILOS.
  - `8x8dct` kikapcsolása TILOS.
  - Kötelezően használandó partíciók: `i4x4,p4x4,i8x8,p8x8,b8x8` (`--partitions all`).
  - `me` értéke KIZÁRÓLAG `umh`, `esa` vagy `tesa` lehet.
  - `merange` értéke nem lehet 24-nél kisebb.
  - `subme` értéke nem lehet 8-nál kisebb.
  - Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`). A DVD-k nem négyzet alakú pixeleit négyzetté kell alakítani!
  - Kizárólag Limited, TV range-ű release készíthető (`16-235`).
  - `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet.
  - `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - Adaptív kvantálás használata kötelező! `--aq-mode=2`/`3`
  - A keyframe-ek közötti maximális távolság `FPS*20` lehet. (`FPS*10` ajánlott)
  - A készített release bitrátája nem lehet nagyobb, mint a forrásé. Kivéve Hybrid releasek, melyek több forrás felhasználásával készülnek.
  - Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - HDTV/PDTV forrás esetén logók maszkolása megengedett. (`InpaintFunc`)

## Audio
  - Megengedett hangformátumok: `AC3`, `AAC`.
  - `DTS`, `MP3`, `MP2` és egyéb vicces formátumok használata TILOS!
  - A hangsávok eredeti csatornaszámát meg kell tartani! Kivétel 8 csatornás hangok.
  - 8 csatornás hang esetén vagy a core-t kell megtartani vagy egy 6 csatornás `DD@640`-et kell készíteni.
  - 6 csatornás hang esetén kizárólag `AC3` elfogadott, melynek bitrátája 640 kbps, ha jobb forrásból készül, vagy az eredetivel megegyező (pl. DVD esetén).
  - 2 csatornás RETAiL hang lehet `AC3` vagy `AAC` is. `AC3` esetén a forrással megegyező bitráta vagy jobb forrás esetén 192-256 kbps elfogadott.
  - 2 csatornás CUSTOM hang (TV-ből felvett) KIZÁRÓLAG `AAC` lehet, CUSTOM `AC3` TILOS!
  - Mono hang KIZÁRÓLAG `AAC` lehet.
  - AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry`, `Dolby Media Encoder`)
  - A készített AC3 nem tartalmazhat Copyright Protected flag-et.
  - AAC esetében elfogadott encoderek: QAAC, FDK, Nero
    - Csak mono/stereo hangnál használható AAC.
    - QAAC: `-V 90` - `-V 127`
    - FDK: `-m 4` vagy `-m 5`
    - Nero: `-q 40` - `-q 75`
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - A hangok nyelvét kötelező Language tagben jelezni!
  - Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. hdtools compare)
  - Resampling-re használható programok: hdtools resample, eac3to, Sound Forge, Audacity.
  - TimeStretchingre használható programok: hdtools tstretch, Prosoniq TimeFactory II, Sound Forge és SONAR `élastique TimeStretch`, Audacity.
  - Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  
## Feliratok
 - Kizárólag a magyar forced felirat megtartása kötelező, a többi opcionális. Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani, hogy mi a forrás)
 - Az opcionálisan mellékelt feliratok kizárólag SRT formátumú és UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - Feliratok képre égetése, hardcodeolása SZIGORÚAN TILOS!
 - A feliratok nyelvét KÖTELEZŐ Language tag-ként beállítani.
 - Title tag használata opcionális.
 - Feliratok sorrendje:
    - magyar forced (ha van)
    - magyar full
    - eredeti forced (ha van)
    - eredeti full
    - eredeti full SDH
  - Forced feliratoknál a Forced flag használata ajánlott.
  - További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
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
  - Más csapatok sértegetése, személyeskedés TILOS!
  
## NUKE
 - A szabályzat nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
 - NUKE requestet bárki kérhet, a jogosság megvizsgálása a NUKE Council feladata
 - Indokok taggelése:
    - dupe = DUPE release, azaz egy korábbival megegyezik, vagy közel azonos
    - grp.req = csapat kérése
    - get.repack, get.rerip = van új, javított változat azonos csapattól
    - get.proper = van javított változat másik csapattól
    - bad.res = hibás felbontás
    - bad.crop = hibás cropolás
    - bad.colorimetry = `--colormatrix` hibás használata
    - bad.deinterlace = hibás deinterlacelés, általában sávozódó videó és/vagy egyéb képi artifactek
    - bad.IVTC = vegyes félképek hibás eltávolítása
    - dupe.frames = duplázott képkockák, általában hibás deinterlacelés/IVTC eredménye
    - bitstarved = szükségesnél jelentősen alacsonyabb bitráta
    - bloated = szükségesnél jelentősen magasabb bitráta
    - upscaled = felskálázott kép/hang<br />
      példák kép felskálázottság ellenőrzésére:
      `Interleave(last,last.AutoResize("720").AutoResize("1080").Subtitle("1080 -> 720 -> 1080"))` (720p upscale)<br />
      `Interleave(last,last.AutoResize("480").AutoResize("1080").Subtitle("1080 -> 480 -> 1080"))` (480p upscale)<br />
      (AutoResize z_Spline36Resize-t használ)
    - audio.oos = hang csúszik a képhez képest
    - sub.oos = felirat csúszik a képhez képest
    - nfo.wtf = NFO érthetetlen vagy értelmezhetetlen
    - Több ok `_` vagy `,` karakterrel fűzendő össze. pl. `bad.res_bad.crop` vagy `bad.res, bad.crop`.
    - A READ.NFO-khoz és a PROPER-ekhez kötelező proof. Jobb kép esetén comparison, oos esetén kép a csúszásról.
    - A szabályzattól notorikusan eltérő csapatok permanens bant kapnak.

## Aláírták és tudomásul vették

## Oldalak, akik elfogadták

## Érvényes
  2019-??-??-től

## Banned grps
