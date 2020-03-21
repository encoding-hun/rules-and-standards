# Hungarian HD x264 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapjául a 2009.04.15, 2009.06.08-as magyar és 2011.01.29-es nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.

## Általános
 - Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - Kizárólag `.mkv` konténer használata elfogadott.
 - A film csonkítása, trimmelése TILOS.
 - A stáblista, amennyiben nem tartalmaz extra jelenetet, kódolható alacsonyabb bitrátával.
 - A film tömörítése (pl. rar, zip stb.) és darabolása TILOS.
 - A fő MKV mellé SFV ellenőrzőösszeg készítése ajánlott, de nem kötelező.
 - A sample opcionális, amennyiben van, 60-120 másodperc közöttinek kell lennie és nem az epizód/film legelejéről. A sample-t újrakódolás nélkül, a végső encode-ból kell kivágni és egy `Sample` nevű mappába vagy a fő MKV mellé kell helyezni.
 - mHD, HDLight és egyéb vicces baromságok készítése és felhasználása TILOS!
 - Chapterlist használata UHD BD, BD és HDDVD források esetén KÖTELEZŐ!

## Taggelés
  - Ékezetes karakterek használata TILOS!
  - Engedélyezett karakterek: `a-z` `A-Z` `0-9` `.` `-` `_` `+`
  - TILOS két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - A következő nevek nem használhatók könyvtár- és fájlnevek elején ponttal elválasztva: `CON`, `PRN`, `AUX`, `NUL`, `COM*`, `LPT*` (ahol `*` egy számot jelöl).
    - TILOS: `Con.Man.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
      - OK: `Con_Man.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
    - TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - OK: `The.Con.Is.On.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
  - Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - Sorozatok:
    `[series.name].[season].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
    - Filmek:
    `[movie.title].[year].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
  - A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - `[audio.codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - WEB-DL és WEBRip forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`)
  - WEB-hez további guide:
    - Az minősül WEB-DL-nek, ami nem lett újrakódolva az oldalról való leszedés után (vagy közben).
    - Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-et használ.
    - Egy WEB-DL nem feltétlenül jobb, mint egy WEBRip (pl. `2160p.WEB-DL`-ből kódolt `720p.WEBRip` vs `720p.WEB-DL`)
    - `WEB-DLRip` megjelölés kerülendő, `WEB-DL`-ből kódolt Rip = `WEBRip`
   - `Rip` és `RiP` megjelölés is elfogadott.
   - `REPACK` és `RERip` tagok használata kötelező, ha saját release-t javít valaki.
   - `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
   - TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
   - `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.

## Források
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása:<br />
   `(UHD)` `BluRay` > `HDDVD`, `DTheater` > `WEBRip` nagyobb felbontású WEB-DL-ből kódolva > `WEB-DL` > `HDTV`<br />
   `P2P` > `Scene` (kivétel retail lemezek esetén)
   - `WEBRip` alacsonyabb felbontással való újratömörítése TILOS!
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping TILOS, ekkor x265 encode készítendő (lásd: oda vonatkozó szabályzat).
   - Muxolni kizárólag olyan már kész releasere szabad, amely megfelel ezen szabályzatban rögzített pontoknak (kivéve az x264 verziójára vonatkozó szabálypont HDB internalok esetén). Törekedni kell az elérhető legjobb minőségű release felhasználására! Gyatra minőségű release-re való muxolás helyett saját encode készítése ERŐSEN AJÁNLOTT!

## Video
  - Minimum `r2800`-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok) muxolunk.
  - TILOS minden olyan x264 használata, amely az alábbi bugos commitot tartalmazza (`r2969`-`r2979`): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs féle vanilla `r2970+1` és tMod `r2970+3`.
  - Törekedjünk a minél újabb encoder használatára!
  - Házibarkács encoderek használata TILOS!
  - Már kész release alacsonyabb felbontással való újrakódolása (pl. BRRip) SZIGORÚAN TILOS!
  - Kizárólag 8 bites YUV420 (YV12) videó megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - Kizárólag progresszív kép megengedett. Amennyiben szükséges deinterlacer vagy IVTC használata kötelező.
  - A videó eredeti FPS értékét meg kell tartani. Interlace-elt forrás esetén 2 félképből 1-et kell képezni (értsd `50i`-ből `25p`-t kell készíteni). Ez alól kivétel lehet a sportfelvétel, ahol indokolt lehet az `50p`. Ekkor kizárólag `QTGMC` deinterlacer használható!
  - A videót cropolni kell addig amíg maximum 1-1 px fekete sáv marad.
  - Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line pl.: `bbmod`/`FixColorBrightness`/`BalanceBorders`/`EdgeFixer`
  - A kódolt videó felbontása 1 pixellel térhet el a forrás alapján (cropolás után) számolttól, pl. 1280x539 helyett 1280x538 (mod2).
  - A videó felbontása mod2 kell legyen. (Nem mod16, ez nem XviD.)
  - A videó felskálázása SZIGORÚAN TILOS!
  - 1080p forrású 1080p encode esetén csak cropolni szabad, resize-olni nem.
  - Resize-oláshoz `z_Spline36Resize` vagy `Spline36ResizeMod` ajánlott, a `Spline36Resize` tartalmaz egy apró chroma shifting bugot, kerülendő. (VapourSynth-et nem érinti.) VapourSynth esetén `Spline64` is ajánlott.
  - Tilos `Nearest Neighbor`, `Bilinear` és `Bicubic` resizer használata.
  - 720p release maximális felbontása `1280x720` lehet. (`AutoResize("720")`)
  - 1080p release maximális felbontása `1920x1080` lehet. (`AutoResize("1080")`)
  - ColorMatrixot, amennyiben a forrás tartalmaz erre vonatkozó információt KÖTELEZŐ flaggelni (tipikusan `BT.709`), amennyiben nem, úgy `undef`-en kell hagyni.
  - ColorPrimaries és TransferFunction flaggelése opcionális (háttértudást igényel a stúdió setupról, csak akkor használd, ha tudod, mit csinálsz). Bővebb infó: https://mod16.org/hurfdurf/?p=116
  - A maximálisan megengedett referencia képek számának használata kötelező (--ref).
    - `--preset veryslow`/`placebo` magától kiszámolja a legnagyobbat, ami még nem töri meg a kompatibilitást. (Érdemes így csinálni, és akkor nem kell manuálisan számolni.)
    - Kiszámolása: `8388608/(végső szélesség*végső magasság)` -> lefele kerekítés.
    Pl.: `8388608/(1280*640) = 10.24`, `10.24` -> `10`
    `(8388608 = 32768*16*16)` `[32768 a MaxDpbMbs High@4.1-nél, 16*16 egy macroblock]`
  - B frame-ek kikapcsolása TILOS. Minimum `3` egymás utáni B frame-t kell engedni (`--bframes 3` vagy több).
  - A készült videónak DXVA-kompatibilisnek kell lennie (max. `High@L4.1`).
  - `CABAC` kikapcsolása TILOS.
  - `8x8dct` kikapcsolása TILOS.
  - Kötelezően használandó partíciók: `i4x4,i8x8,p8x8,b8x8` (default), `p4x4` használata opcionális, de ajánlott
  - `me` értéke KIZÁRÓLAG `umh`, `esa` vagy `tesa` lehet.
  - `merange` értéke nem lehet 24-nél kisebb.
  - `subme` értéke nem lehet 8-nál kisebb.
  - `rc-lookahead` értéke nem lehet `FPS*2`-nél kisebb.
  - Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`).
  - Kizárólag Limited, TV range-ű release készíthető (`16-235`).
  - `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet.
  - `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - Adaptív kvantálás használata kötelező! `--aq-mode=1`/`2`/`3` (`3` ajánlott)
  - A keyframe-ek közötti maximális távolság `FPS*20` lehet. (`FPS*10` ajánlott)
  - A készített release bitrátája nem lehet nagyobb, mint a forrásé. Kivéve Hybrid release-ek, melyek több forrás felhasználásával készülnek.
  - Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - HDTV forrás esetén logók maszkolása megengedett. (`InpaintFunc`)

## Audio
  - Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata. Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi tag-ot megadni.
  - Az eredeti nyelvű hangsáv megtartása KÖTELEZŐ!
  - Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - Egyéb nyelvű hangok megtartása TILOS!
  - Megengedett hangformátumok: `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `DTS`, `AAC`, `FLAC`.
  - `MP3`, `MP2` és egyéb vicces formátumok használata TILOS!
  - `DTS` és `AC3` encodeolása `AAC`-be kizárólag a kommentár sáv esetén megengedett. Kivétel, ha nyújtani és/vagy vágni kell, ekkor lehet AAC.
  - LPCM hangot kötelező FLAC-be (film esetén) vagy AAC-be (kommentár esetén) konvertálni
  - A hangsávok eredeti csatornaszámát meg kell tartani! Kivétel 8 csatornás hangok és kommentár sávok.
  - 8 csatornás hang esetén vagy DD+ formátumot kell használni (`DDP@1536`) vagy a core-t kell meghagyni.
  - AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Dolby Media Encoder`, `Sonic Audio Transcoder`)
  - A készített AC3 nem tartalmazhat Copyright Protected flaget.
  - AAC esetében elfogadott encoderek: QAAC, FDK, Nero
    - Csak stereo/mono hangnál használható AAC.
    - QAAC: `-V 90` - `-V 127`
    - FDK: `-m 4` vagy `-m 5`
    - Nero: `-q 40` - `-q 75`
  - 720p release-ek esetén `DTS`, `TrueHD`, `DTS-HD.MA` és `DTS-X` hang használata TILOS!
  - 1080p release-ek esetén `TrueHD`, `DTS-HD.MA` és `DTS-X` használata TILOS! Ilyen esetekben a core-t használjuk vagy lossless audióból kódolunk `DD@640`, `DDP@1024` 6 csatornás vagy `DDP@1536` 8 csatornás hangot.
  - Amennyiben az érintetlen forráson DTS található csak:
    - `DDP@1024` kódolása (ajánlott, kivéve ha 768 kbps vagy kisebb a DTS bitrátája),
    - DTS meghagyása, mellé `DD@640` (2 csatorna esetén `DD@256`) compatibility track készítése.
  - Lossy hangot csak losslessből szabad kódolni. (Ez alól kivétel ha csak DTS hang elérhető és compatibility tracket készítünk vagy 1080p-re `DDP@1024`-et.)
  - Compatibility AC3 track készület FFmpeg (4.1 vagy újabb) vagy Aften (2009-12-26 vagy újabb) segítségével is.
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - A hangok nyelvét kötelező Language tagben jelezni!
  - Commentary track maximum 2.0 lehet, AC3 esetében maximum 192 kbps, AAC esetében 80-160 kbps.
  - Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`)
  - Resamplingre használható programok: `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity`, `SoX`, `Adobe Audition`.
  - TimeStretchingre használható programok: `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge` és `SONAR` `élastique TimeStretch`, `Audacity`, `SoX`, `Adobe Audition`.
  - Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  
## Feliratok
 - A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - Kötelező feliratok, amennyiben elérhetőek a forráson: magyar forced, magyar, eredeti nyelv forced, eredeti nyelv.
 - Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani, hogy mi a forrás)
 - Az opcionálisan mellékelt feliratok kizárólag SRT formátumú és UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - Feliratok képre égetése, hardcodeolása SZIGORÚAN TILOS!
 - A feliratok nyelvét kötelező Language tagként beállítani.
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
      * Videó felbontása
      * Videó bitrátája
      * Videó FPS-e
      * Audiósávok nyelvei
      * Audiósávok típusai
      * Audiósávok csatornaszáma
      * Audiósávok bitrátája
      * Audió mintavételezési rátája (Sample rate)
      * Feliratok nyelve
  - Más csapatok sértegetése, személyeskedés TILOS!
  
## Aláírták és tudomásul vették
`boOk`, `Legacy`, `NaGa`, `NFC`, `pcroland`, `prldm`

## Oldalak, akik elfogadták

## Érvényes
  2020-02-19-től

## Utolsó frissítés
  2020-03-21

## Banned grps
