# Hungarian HD x264 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapjául a 2009.04.15, 2009.06.08-as magyar és 2011.01.29, 2020.04.15-ös nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.

## 1) Általános
 - 1.1) Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - 1.2) Kizárólag `.mkv` konténer használata elfogadott.
   - 1.2.1) Ajánlott muxer: MKVToolNix (mkvmerge). Törekedjünk a lehető legfrissebb változat használatára.
   - 1.2.2) Header compression használata TILOS.
 - 1.3) A film csonkítása, trimmelése TILOS.
 - 1.4) A film tömörítése (pl. rar, zip stb.) és darabolása TILOS.
 - 1.5) A fő MKV mellé `SFV` vagy `MD5` ellenőrzőösszeg készítése ajánlott, de nem kötelező.
 - 1.6) Sample készítése opcionális.
    - 1.6.1) Hossza 50-120 másodperc közötti legyen.
    - 1.6.2) A Sample nem származhat az epizód/film legelejéről, valamint legvégéről.
    - 1.6.3) A Sample-t újrakódolás nélkül, a végső encode-ból kell kivágni.
    - 1.6.4) A Sample-t egy `Sample` nevű mappába vagy a fő MKV mellé kell helyezni. Utóbbi esetben a filenévben kell jelölni, hogy melyik a sample.
 - 1.7) mHD, HDLight és egyéb vicces baromságok készítése és felhasználása TILOS!
 - 1.8) Chapterlist használata KÖTELEZŐ, amennyiben a forrás tartalmaz ilyet!
   - 1.8.1) Chapterek elnevezése opcionális, kizárólag magyar vagy angol fejezetcímek használhatóak.
 - 1.9) Vízjelek használata TILOS!

## 2) Taggelés - könyvtárnév
  - 2.1) Ékezetes karakterek használata TILOS!
  - 2.2) Engedélyezett karakterek: `a-z` `A-Z` `0-9` `.` `-` `_` `+`.
     - 2.2.1) Ismételt kötőkarakterek használata TILOS! (pl. `...` vagy `-.`)
     - 2.2.2) Amennyiben a cím tiltott karaktert tartalmaz (pl. `*`), akkor `.` vagy `-`-el helyettesítendő.
  - 2.3) TILOS két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - 2.4) A következő nevek nem használhatók könyvtár- és fájlnevek elején ponttal elválasztva: `CON`, `PRN`, `AUX`, `NUL`, `COM*`, `LPT*` (ahol `*` egy számot jelöl).
    - 2.4.1) TILOS: `Con.Man.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
      - OK: `Con_Man.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
    - 2.4.2) TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - 2.4.3) OK: `The.Con.Is.On.2018.720p.BluRay.DD5.1.x264.HUN-XYZ`
  - 2.5) Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - 2.5.1) Sorozatok:
    `[series.name].[season].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.1.1) `[season]` tag legalább két jegyre megadandó (mind az évad, mind a rész), kivéve mini-series esetén.
       - 2.5.1.2) Adott sorozat adott évadán belül a taggelés nem változhat.
       - 2.5.1.3) Az évadok és részek számozásánál csak hivatalos források elfogadottak.
    - 2.5.2) Filmek:
    `[movie.title].[year].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.2.1) A dokumentumfilmek filmnek minősülnek.
  - 2.6) A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - 2.7) `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - 2.8) `[audio.codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - 2.9) `WEB-DL` és `WEBRip` forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`).
    - 2.9.1) A használandó hazai és nemzetközi rövidítések itt érhetőek el: [**LINK**](https://github.com/encoding-hun/rules-and-standards/blob/master/web-abbrevation.md).
  - 2.10) WEB-hez további guide:
    - 2.10.1) Az minősül `WEB-DL`-nek, ami nem lett újrakódolva az oldalról való leszedés után (vagy közben).
    - 2.10.2) Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-et használ.
    - 2.10.3) Egy `WEB-DL` nem feltétlenül jobb, mint egy `WEBRip` (pl. `2160p.WEB-DL`-ből kódolt `720p.WEBRip` vs. `720p.WEB-DL`)
    - 2.10.4) `WEB-DLRip` megjelölés TILTOTT, `WEB-DL`-ből kódolt Rip = `WEBRip`
  - 2.11) `Rip`, `RiP` és `RIP` megjelölés is elfogadott.
  - 2.12) `REPACK` (`Repack`) és `RERiP` (`Rerip`) tagok használata kötelező, ha saját release-t javít valaki.
  - 2.13) `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
     - 2.13.1) `iNTERNAL`-ként kell feltütnetni minden olyan release-t, amely ellentmond a szabályzat bármely pontjának, de nem érhető el olyan forrás, amely teljesítené (pl. tonemapping).
  - 2.14) TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
  - 2.15) `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.
     - 2.15.1) A Blu-ray forrásokat `BluRay`-nek kell taggelni.
     - 2.15.2) Az UHD Blu-ray forrásokat `UHD.BluRay`-nek kell taggelni.
     - 2.15.3) A HD-DVD forrásokat `HDDVD`-nek kell taggelni.
  - 2.16) Nem Retail és nem WEB forrás esetén NFO-ban jelölni kell, hogy milyen forrás és esetlegesen miben tér el a Retail változattól. `READ.NFO` tag használata KÖTELEZŐ!
  - 2.17) `PROPER` = más hibás munkájának javítása; `REPACK` = muxolási hiba, hiányzó hang/felirat; `RERiP` = hibás videó/hang
     - 2.17.1) `PROPER` release-re érkező `PROPER`-t `REAL.PROPER`-nek kell taggelni (és így tovább a későbbieket, pl. `REAL.REAL.PROPER`)).
  - 2.18) `READ.NFO` és `PROPER`/`REPACK`/`RERiP` tagek együttes használata TILOS!
  - 2.19) Zavaró és felesleges tagek használata TILOS!

## 3) NFO
 - 3.1) NFO használata kötelező.
 - 3.2) Az NFO nyelve angol és/vagy magyar.
 - 3.3) Magyar nyelvű NFO esetén az angol kifejezések szakszerű fordításának használata kötelező (ebben segít a Wikipedia).
 - 3.4) Az NFO-ban kötelező a következő információkat feltüntetni:
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
  - 3.5) Más csapatok sértegetése, személyeskedés TILOS!
  - 3.6) `PROPER`/`REPACK`/`RERiP` release-ek esetén fel kell tüntetni a korábbi release problémáit. Képi vagy hangi `PROPER` esetén csatolni kell proofot, hogy valóban jobb az új release.
  - 3.7) Felesleges, zavaró dolgokat az NFO-ba elhelyezni TILOS!

## 4) Források
   - 4.1) Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
      - 4.1.1) Ez alól kivétel, ha eltérő vágással (`THETRICAL` vs. `EXTENDED`) rendelkezik a release.
   - 4.2) Források prioritása:<br />
   `(UHD)` `BluRay` > `HDDVD`, `DTheater` > `WEBRip` nagyobb felbontású WEB-DL-ből kódolva > `WEB-DL` > `HDTV`<br />
   `P2P` > `Scene` (kivétel retail lemezek esetén)
   - 4.3) `WEBRip` alacsonyabb felbontással való újratömörítése TILOS!
   - 4.4) Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
   - 4.5) UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
     - 4.5.1) HDR -> SDR tonemapping TILOS, ekkor x265 encode készítendő (lásd: oda vonatkozó szabályzat).
   - 4.6) Muxolni kizárólag olyan már kész release-re szabad, amely megfelel ezen szabályzatban rögzített pontoknak (kivéve az x264 verziójára vonatkozó szabálypont HDB internalok esetén). Törekedni kell az elérhető legjobb minőségű release felhasználására! Gyatra minőségű release-re való muxolás helyett saját encode készítése ERŐSEN AJÁNLOTT!

## 5) Video
  - 5.1) Már kész release alacsonyabb felbontással való újrakódolása (pl. BRRip) SZIGORÚAN TILOS!
  - 5.2) Kizárólag egy videósáv használata megengedett.
  - 5.3) 2D-s releasehez nem használható 3D-s film bal vagy jobb szeméhez tartozó kép, kivéve, ha a filmből nem létezik 2D-s kiadás.
  - 5.4) Egybefüggő videó darabolása TILOS! Egy lemezen található több rész (melyeket stáblista választ el) darabolása részekre KÖTELEZŐ!
     - 5.4.1) Ha a film több lemezen található és nincs a lemez végén stáblista, akkor össze kell a szegmenseket fűzni.
  - 5.5) Az előző rész tartalmából-t, a bevezető intrókat, és a stáblistát kötelező teljes hosszukban megtartani és a főcímmel együtt kódolni.
  - 5.6) A zavaró bevágásokat: műsorszám hirdetést tartalmaz, reklámok, FBI Warning, stb. el kell távolítani.
     - 5.6.1) Kivéve, amikor ez a videó/hang (közel) teljes újrakódolásával járna.
  - 5.7) Égetett felirattal rendelkező forrásokat lehetőleg kerüljük, kivéve ha szignifikánsan jobb a minősége.
  - 5.8) Hybrid encode-ok megengedettek, ha ezzel jobb minőség érhető el.
  - 5.9) A konténerben felbontásra és croppolásra extra metaadatokat megadni TILOS!
  - 5.10) A video sáv Language tagjának beállítása opcionális: vagy magyar vagy az eredeti nyelv.

## 6) Felbontás
  - 6.1) 720p release maximális felbontása `1280x720` lehet. (`AutoResize(720)`)
  - 6.2) 1080p release maximális felbontása `1920x1080` lehet. (`AutoResize(1080)`)
     - 6.2.1) 3D-s release kizárólag 1080p felbontással készülhet.
  - 6.3) A videó felbontása mod2 kell legyen.
  - 6.4) A videó felskálázása SZIGORÚAN TILOS (pl. ha croppolás után 1916 széles a kép, tilos 1920-ra felnagyítani)!
     - 6.4.1) Upscaled forrás esetén az eredeti, upscale előtti (vagy annál kisebb) felbontáson készíthető release. Ennek megkeresésésére jó pl. az UpscaleCheck és a getnative kódok. Köztes felbontások esetén a kerekítés szabályai érvényesek (pl. 900p és felette készíthető 1080p).
  - 6.5) Eltérő képarányú release (pl. `OM`) nem dupeolja a korábbit és *vica versa*.
  - 6.6) A videót cropolni kell addig amíg maximum 1-1 px fekete sáv marad. A cropot a főcímnél kell meghatározni.
  - 6.7) A dirty lineok, dirty pixelek és faded lineok eltávolítása TILOS!
  - 6.8) Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line/faded line pl.: `bbmod`/`FixRowBrightness`/`BalanceBorders`/`EdgeFixer`
  - 6.9) Javítás után a widow lineok (eredetileg fekete sávok) 1080p esetén eltávolíthatóak (resize vagy overlay), 720p esetén kötelezően eltávolítandóak (resize).
  - 6.10) A kódolt videó felbontása 1 pixellel térhet el a forrás alapján (cropolás után) számolttól, pl. 1280x539 helyett 1280x538 (mod2).

## 7) Filterek
  - 7.1) Kizárólag progresszív kép megengedett. Amennyiben szükséges deinterlacer vagy IVTC használata kötelező.
  - 7.2) Resize-oláshoz `z_Spline36Resize` (`resize.Spline36`) vagy `Spline36ResizeMod` ajánlott, a `Spline36Resize` tartalmaz egy apró chroma shifting bugot, használata kerülendő. (VapourSynth-et nem érinti.) További engedett resizerek: `z_Spline64Resize` (`resize.Spline64`), `BlackmanResize`.
     - 7.2.1) Tilos `Nearest Neighbor`, `Bilinear`, `Bicubic`, és egyéb gyenge resizerek használata.
  - 7.3) Kizárólag frame pontos forrásfilterek használhatóak (pl. `FFMS2`, `LSMASH`, `DGDecNV`, `DGIndex`).
     - 7.3.1) Pontatlan forrásfilterek használata TILOS (pl. `DirectShowSource`)!
  - 7.4) A kép minőségét jelentősen befolyásoló filterek használata (pl. grain eltávolítása, warp sharping, stb.) TILOS!
     - 7.4.1) A grain eltávolítása alól kivételt képez, ha az túlságosan magas bitrátát eredményezne.
     - 7.4.2) Számos upscaled anyagra a grain már a magasabb felbontáson kerül rá. Ilyen esetekben eltávolítása indokolt lehet.
  - 7.5) DeBlocking és DeBanding filterek használata megengedett, ezeket érdemes adott zónákra korlátozni (pl. `ReplaceFramesSimple`, `Trim`, vagy `ConditionalFilter` segítségével).
  - 7.6) A videó eredeti FPS értékét meg kell tartani. Interlace-elt forrás esetén 2 félképből 1-et kell képezni (értsd `50i`-ből `25p`-t kell készíteni). Ez alól kivétel lehet a sportfelvétel, ahol indokolt lehet az `50p`. Ekkor kizárólag `QTGMC` (`preset slow` vagy jobb) deinterlacer használható!
  - 7.7) Kizárólag CFR (constant framerate) mód használható! Amennyiben a forrás VFR-el rendelkezik, úgy ez felülírja az 7.6-os pontot.
  - 7.8) A dupe framek eltávolítása kötelező!

## 8) Videó kódolás
  - 8.1) Kizárólag x264 használható.
  - 8.2) Minimum `r2800`-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok; megbízható források) muxolunk.
  - 8.3) TILOS minden olyan x264 használata, amely az alábbi bugos commitot tartalmazza (`r2969`-`r2979`): https://code.videolan.org/videolan/x264/commit/92d36908cbafd2a6edf7e61d69f341027b57f6f8
  - 8.4) Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs, aMod.
  - 8.5) Az x264 header eltávolítása TILOS!
  - 8.6) Törekedjünk a minél újabb encoder használatára!
  - 8.7) Házibarkács encoderek használata TILOS!
  - 8.8) Kizárólag 8 bites YUV420 (YV12) videó megengedett.
  - 8.9) Kizárólag 2pass és CRF kódolások megengedettek.
  - 8.10) Szegmentált kódolás TILOS!
  - 8.11) 1080p és 30 fps alatt `level 4.1`-et kell használni, 1080p felbontás és magasabb fps mellett `level 4.2`-t.
  - 8.12) Zónák használata megengedett.
  - 8.13) GPU encoding minden formája TILTOTT!
  - 8.14) Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`).
  - 8.15) A keyframe-ek közötti maximális távolság (`--keyint`) `FPS*20` lehet (`FPS*10` ajánlott, default); minimum `FPS*5` adható meg.
  - 8.16) `--min-keyint` értéke legalább `FPS/2`, maximum `FPS*2` lehet (`floor(FPS)` ajánlott, default).
  - 8.17) ColorMatrixot, amennyiben a forrás tartalmaz erre vonatkozó információt KÖTELEZŐ flaggelni (tipikusan `BT.709`), amennyiben nem, úgy `undef`-en kell hagyni.
  - 8.18) ColorPrimaries és TransferFunction flaggelése opcionális (háttértudást igényel a stúdió setupról, csak akkor használd, ha tudod, mit csinálsz). Használata esetén a forrással egyezőre kell állítani. Bővebb infó: [**mod16.org**](https://mod16.org/hurfdurf/?p=116) | [**mirror**](https://github.com/encoding-hun/rules-and-standards/blob/master/files/color-coefficient.md)
  - 8.19) A maximálisan megengedett referencia képek számának használata kötelező (--ref).
    - 8.19.1) `--preset veryslow`/`placebo` magától kiszámolja a legnagyobbat, ami még nem töri meg a kompatibilitást. (Érdemes így csinálni, és akkor nem kell manuálisan számolni.)
    - 8.19.2) Kiszámolása: `8388608/(végső szélesség*végső magasság)` -> lefele kerekítés.
    Pl.: `8388608/(1280*640) = 10.24`, `10.24` -> `10`
    `(8388608 = 32768*16*16)` `[32768 a MaxDpbMbs High@4.1-nél, 16*16 egy macroblock]`
  - 8.20) B frame-ek kikapcsolása TILOS. Minimum `5` egymás utáni B frame-t kell engedni (`--bframes 5` vagy több).
  - 8.21) A készült videónak DXVA-kompatibilisnek kell lennie (max. `High@L4.1`).
  - 8.22) `CABAC` kikapcsolása TILOS.
  - 8.23) `8x8dct` kikapcsolása TILOS.
  - 8.24) Kötelezően használandó partíciók: `i4x4,i8x8,p8x8,b8x8` (default), `p4x4` használata opcionális, de ajánlott
  - 8.25) `me` értéke KIZÁRÓLAG `umh`, `esa` vagy `tesa` lehet.
  - 8.26) `merange` értéke nem lehet 24-nél kisebb.
  - 8.27) `subme` értéke nem lehet 8-nál kisebb.
  - 8.28) `rc-lookahead` értéke nem lehet `FPS*2`-nél kisebb.
  - 8.29) Kizárólag Limited, TV range-ű release készíthető (`16-235`).
  - 8.30) `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet, de egyik sem lehet kevesebb, mint `50000`.
  - 8.31) `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - 8.32) Adaptív kvantálás használata kötelező! `--aq-mode=1`/`2`/`3` (`3` ajánlott).
  - 8.33) A készített release bitrátája nem lehet nagyobb, mint a forrásé.
     - 8.32.1) Kivételt képeznek Hybrid release-ek, melyek több forrás felhasználásával készülnek.
  - 8.34) A videó bitrátáját vagy CRF értékét úgy kell megválasztani, hogy a képminőség transzparens legyen (amennyire lehet) a forráshoz képest.
  - 8.35) Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - 8.36) HDTV forrás esetén logók maszkolása megengedett (pl. `InpaintFunc`).
  - 8.37) A stáblista, amennyiben nem tartalmaz extra jelenetet, kódolható alacsonyabb bitrátával.
  - 8.38) A `WEB-DL`-ek felmentést élveznek az összes 8-as pontbeli szabály alól, kivéve a 8.8-ast.

## 9) Audio
  - 9.1) Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata. Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi tag-ot megadni.
  - 9.2) Az eredeti nyelvű hangsáv megtartása KÖTELEZŐ!
  - 9.3) Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - 9.4) Egyéb nyelvű hangok megtartása TILOS!
  - 9.5) Megengedett hangformátumok: `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `DTS`, `AAC`, `FLAC`.
  - 9.6) `MP3`, `MP2`, és egyéb vicces formátumok használata TILOS!
  - 9.7) `DTS` és `AC3` (`DD`) encode-olása `AAC`-be kizárólag a kommentár sáv esetén megengedett.
     - 9.7.1) Kivétel, ha nyújtani és/vagy vágni kell, ekkor lehet `AAC`, amennyiben stereo vagy mono.
  - 9.8) LPCM hangot kötelező FLAC-be (film esetén) vagy AAC-be (kommentár esetén) konvertálni.
  - 9.9) A hangsávok eredeti csatornaszámát meg kell tartani! Kivétel 8 csatornás hangok és kommentár sávok.
  - 9.10) 8 csatornás hang esetén vagy DD+ formátumot kell használni (`DDP@1536`) vagy a core-t kell meghagyni.
  - 9.11) 2 csatornás `CUSTOM` hangnál (TV-ből vagy WEB-ről felvett) javasolt `AAC` használata.
  - 9.12) 720p release-ek esetén `DTS`, `TrueHD`, `DTS-HD.MA` és `DTS-X` hang használata TILOS!
  - 9.13) 1080p release-ek esetén `TrueHD`, `DTS-HD.MA` és `DTS-X` használata TILOS! Ilyen esetekben vagy a core-t használjuk vagy lossless audióból kódolunk `DD@640`, `DDP@1024` 6 csatornás vagy `DDP@1536` 8 csatornás hangot (9.9 és 9.10 figyelembevételével).
  - 9.14) Amennyiben az érintetlen forráson kizárólag `DTS` (vagy `DTS-HD MA`, `DTS:X`) található:
    - 9.14.1) `DDP@1024` kódolása (ajánlott, kivéve ha 768 kbps vagy kisebb a DTS bitrátája),
    - 9.14.2) DTS meghagyása, mellé KÖTELEZŐ `DD@640` (2 csatorna esetén `DD@256` vagy `AAC`) compatibility track készítése.
  - 9.15) Lossy hangot csak losslessből szabad kódolni.
     - 9.15.1) Ez alól kivétel ha csak DTS hang érhető el és compatibility tracket készítünk vagy 1080p-re `DDP@1024`-et.
  - 9.16) Maximum +/- 100 ms hangcsúszás megengedett.
  - 9.17) A hangok nyelvét kötelező Language tagben jelezni!
  - 9.18) Kizárólag stúdió által készített surround hangok használhatóak fel, házilag felkevertek tilosak. TV-s surround hang esetén mindig győződjünk meg, hogy valódi surround-e, amennyiben nem, downmixeljük. Pl.: `ffmpeg -i input.ac3 -ac 2 -f sox - | sox -p -S -b 24 --norm=-1 output.wav`
  - 9.19) Amennyiben a forrás audió megtartható újrakódolás nélkül, úgy annak újrakódolása tilos.
    - 9.19.1) Ez alól kivétel, ha kizárólag `E-AC3` hang áll rendelkezésre, ekkor a nagyobb kompatibilitás érdekében `AC3` hang készíthető. Ennek módjáról lásd 10.14-es pont.
  - 9.20) Egy másik forrásból származó hang akkor számít jobb minőségűnek, hogyha a lowpass (cutoff) frekvencia 16 kHz alatt legalább 1 kHz-el, 16 kHz felett legalább 1.5 kHz-el magasabb, és a többlet adat nem sztochasztikus (dithering miatt belekerülő) zaj. Ha ez teljesül, akkor készíthető új release, egyéb esetben `dupe`. Kérdéses esetekben proofként egy-egy spektrum mutatása szükséges a két hangról.
    - 9.20.1) Ez alól kivétel, hogyha az alacsonyabb lowpass-szel rendelkező hang minősége hallhatóan jobb.
    - 9.20.2) További kivételt képez, hogyha jobb forrásból elérhető a hang és a bitrátakülönbség meghaladja a 192 kbps-t `DD` és `DTS` esetén, vagy a `128` kbps-t `DD+` és `AAC` esetén. `DD+` és `DD` hangok bitrátáinak összehasonlítása a 10.14-es pontban rögzítettek szerint `1.7`-es szorzófaktorral történik. `AAC` és `DD` között ugyanezt az átváltást használjuk. Például egy `DD@448`-as DVD hang mindig cserélhető egy BD-ről származó `DD@640`-re.
  - 9.21) A hangok sorrendje:
    - magyar (ha van)
    - eredeti
    - angol (ha az eredeti nem ez; opcionális)
    - kommentárok (opcionális)

## 10) Audio kódolás
  - 10.1) `AC3` (`DD`) esetében Dolby Certified encodert kell használni (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Dolby Media Encoder`, `Sonic Audio Transcoder`).
  - 10.2) A készített `AC3` (`DD`) nem tartalmazhat Copyright Protected flaget.
  - 10.3) `AAC` esetében elfogadott encoderek: `qaac` (`Apple AAC`), `FDK`, `Nero`.
    - 10.3.1) Csak stereo/mono hangnál használható `AAC`.
    - 10.3.2) Javasolt beállítások:
       - 10.3.2.1) `qaac`: `-V 90` - `-V 127` és `--no-delay --ignorelength` (egyéb kapcsolók használata tilos)
       - 10.3.2.2) `FDK`: `-m 4` vagy `-m 5` (és `-cutoff 20000` ffmpeg-es libfdk_aac használata esetén)
       - 10.3.2.3) `Nero`: `-q 40` - `-q 75`
  - 10.4) Compatibility `AC3` (`DD`) track készülhet FFmpeg (4.1 vagy újabb) vagy Aften (2009-12-26 vagy újabb) segítségével is.
  - 10.5) A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - 10.6) Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  - 10.7) Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`).
  - 10.8) Resamplingre használható programok: `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.9) TimeStretchingre használható programok: `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge`, `SONAR` `élastique TimeStretch`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.10) Commentary track maximum 2.0 lehet, `AC3` esetében maximum 192 kbps, `AAC` esetében 80-160 kbps.
  - 10.11) Szegmentált kódolás használata TILOS!
  - 10.12) `AC3`, `E-AC3`, és `DTS` esetén a `dialnorm` értéket meg kell tartani!
  - 10.13) Amennyiben a forrás `AC3` és újrakódolás szükséges, akkor az újrakódolt hang bitrátája nem lehet magasabb, mint a forrásé.
  - 10.14) `E-AC3` hang `AC3`-ba történő kódolásakor a megengedett bitráták az eredeti `1.7`-szereséhez legközelebb eső két bitráta (nagyjából ennyivel jobb a `DD+` algoritmus). Például: ha a forrás `DDP@192`, akkor `192 * 1.7 = 326.4`, tehát az `AC3` bitrátája lehet `320 kbps` vagy `384 kbps` vagy ha a forrás `DDP@256`, akkor `256 * 1.7 = 435.2`, tehát `384 kbps` és `448 kbps`-es `AC3` készíthető.

## 11) Feliratok
 - 11.1) Kizárólag SRT (SubRip) formátumú feliratok megengedettek!
    - 11.1.1) Az OCR karakterfelismerést a lehető legpontosabban kell elvégezni.
    - 11.1.2) A kész felirat lehetőleg kevés, érthetőséget nem zavaró helyesírási hibát tartalmazhat, de törekedjünk, hogy ne legyen benne hiba.
    - 11.1.3) A felismertetett feliraton javasolt egy spellchecker lefuttatása.
    - 11.1.4) Kivételt képeznek a 3D-s encode-ok, ahol megengedett a pgs/sup formátum is.
 - 11.2) A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - 11.3) Kötelező feliratok, amennyiben elérhetőek a forráson: magyar forced, magyar, eredeti nyelv forced, eredeti nyelv.
 - 11.4) Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - 11.5) A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani a forrással egyezőt)
 - 11.6) Az opcionálisan mellékelt feliratok kizárólag `.srt` formátumú és UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - 11.7) Feliratok képre égetése, hardcodeolása SZIGORÚAN TILOS!
 - 11.8) A feliratok nyelvét KÖTELEZŐ Language tagként beállítani.
 - 11.9) Title tag használata opcionális.
 - 11.10) Feliratok sorrendje:
    - magyar forced (ha van)
    - magyar full
    - eredeti forced (ha van)
    - eredeti full
    - eredeti full SDH
    - kommentárok (opcionális)
  - 11.11) Forced feliratoknál a Forced flag használata ajánlott.
  - 11.12) További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
  - 11.13) Retail felirat használata kötelező, amennyiben elérhető.
     - 11.13.1) Fansub használható Retail felirat mellett is.
     - 11.13.2) Fansub és Retail együttes használatánál `--track-name`-ben kötelező megadni a nevüket.
  - 11.14) A feliratok nem csúszhatnak zavaró mértékben a képhez képest (max. ~400 ms).
