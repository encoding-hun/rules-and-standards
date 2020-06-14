# Hungarian SD and 480p x264 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapjául a 2009.04.15, 2009.06.08-as magyar és 2011.01.29, 2020.04.15-ös nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.
  
## Érvényes
  2020-02-19-től

## Utolsó frissítés
  2020-06-14

## 1) Általános
 - 1.1) Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - 1.2) Kizárólag `.mkv` konténer használata elfogadott.
   - 1.2.1) Ajánlott muxer: MKVToolNix (mkvmerge).
      - 1.2.1.1) Törekedjünk a lehető legfrissebb változat használatára.
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
 - 1.10) `480p` és `SD` release DUPE-olja egymást. Ha már van `SD` encode, az nem cserélhető `480p`-re csak a felbontás miatt, sem fordítva. `PROPER` vagy `READ.NFO` esetén lehet `SD`-t `480p`-vel javítani/upgrade-elni, és fordítva.
    
 - A stáblista amennyiben nem tartalmaz extra jelenetet kódolható alacsonyabb bitrátával.

## 2) Taggelés - könyvtárnév
  - 2.1) Ékezetes karakterek használata TILOS!
  - 2.2) Engedélyezett karakterek: `a-z` `A-Z` `0-9` `.` `-` `_` `+`.
     - 2.2.1) Ismételt kötőkarakterek használata TILOS! (pl. `...` vagy `-.`)
     - 2.2.2) Amennyiben a cím tiltott karaktert tartalmaz (pl. `*`), akkor `.` vagy `-`-el helyettesítendő.
  - 2.3) TILOS két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - 2.4) A következő nevek nem használhatók könyvtár- és fájlnevek elején ponttal elválasztva: `CON`, `PRN`, `AUX`, `NUL`, `COM*`, `LPT*` (ahol `*` egy számot jelöl).
    - 2.4.1) TILOS: `Con.Man.2018.BDRip.x264.HUN-XYZ`
      - OK: `Con_Man.2018.BDRip.x264.HUN-XYZ`
    - 2.4.2) TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - 2.4.3) OK: `The.Con.Is.On.2018.BDRip.x264.HUN-XYZ`
 - 2.5) Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - 2.5.1) Sorozatok:
    `[series.name].[season].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.1.1) `[season]` tag legalább két jegyre megadandó (mind az évad, mind a rész), kivéve mini-series esetén.
       - 2.5.1.2) Adott sorozat adott évadán belül a taggelés nem változhat.
       - 2.5.1.3) Az évadok és részek számozásánál csak hivatalos források elfogadottak.
    - 2.5.2) Filmek:
    `[movie.title].[year].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.2.1) A dokumentumfilmek filmnek minősülnek.
    - 2.5.3) `[audio.codec]` opcionális.
    - 2.5.4) 480p release esetén `480p` tag is kell `[source]` előtt.
    - 2.5.5) SD és RETAiL forrás esetén `[source]`-t a forrás milyensége + `Rip` taggal képezzük, pl. `BDRip`, `DVDRip`.
  - 2.6) A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - 2.7) `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - 2.8) `[audio.codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - 2.9) `WEB-DL` és `WEBRip` forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`)
  - 2.10) WEB-hez további guide:
    - 2.10.1) Az minősül `WEB-DL`-nek, ami nem lett újrakódolva az oldalról való leszedés után (vagy közben).
    - 2.10.2) Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-et használ.
    - 2.10.3) Egy `WEB-DL` nem feltétlenül jobb, mint egy `WEBRip` (pl. `2160p.WEB-DL`-ből kódolt `720p.WEBRip` vs `720p.WEB-DL`)
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
     - 2.17.1) `PROPER` releasere érkező `PROPER`-t `REAL.PROPER`-nek kell taggelni (és így tovább a későbbieket).
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
  - 3.6) `PROPER`/`REPACK`/`RERiP` releasek esetén fel kell tüntetni a korábbi release problémáit. Képi vagy hangi `PROPER` esetén csatolni kell Proof-ot, hogy valóban jobb az új release.
  - 3.7) Felesleges, zavaró dolgokat az NFO-ba elhelyezni TILOS!

## 4) Források
   - 4.1) Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
      - 4.1.1) Ez alól kivétel, ha eltérő vágással (`THETRICAL` vs. `EXTENDED`) rendelkezik a release.
   - 4.2) Források prioritása:<br />
   `(UHD)` `BluRay` > `HDDVD`, `DTheater` > `(U)HD WEB-DL` > `DVD` > `WEB-DL` > `HDTV` > `PDTV` > `Analog TV`, `VHS`<br />
   `P2P` > `Scene` (kivétel retail lemezek esetén)
   - 4.3) `WEBRip` alacsonyabb felbontással való újratömörítése TILOS!
   - 4.4) Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
   - 4.5) UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
     - 4.5.1) HDR -> SDR tonemapping TILOS, ekkor x265 encode készítendő (lásd: oda vonatkozó szabályzat).
   - 4.6) Muxolni kizárólag olyan már kész release-re szabad, amely megfelel ezen szabályzatban rögzített pontoknak. Saját encode-ok készítése ajánlott.

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
  - 5.8) Hybrid encodeok megengedettek, ha ezzel jobb minőség érhető el.
  - 5.9) A konténerben felbontásra és croppolásra extra metaadatokat megadni TILOS!
  - 5.10) A video sáv Language tagjának beállítása opcionális: vagy magyar vagy az eredeti nyelv.
  
## 6) Felbontás
  - 6.1) SD release maximális szélessége `720 px` lehet (`AutoResize("SD")`)
     - 6.1.1) DVD-ből kizárólag SD release készíthető.
  - 6.2) 480p release maximális felbontása `854x480` lehet. (`AutoResize("480")`)
  - 6.3) A videó felbontása mod2 kell legyen.
  - 6.4) A videó felskálázása SZIGORÚAN TILOS (pl. ha croppolás után 704 széles a kép, tilos 720-ra felnagyítani)!
     - 6.4.1) Amennyiben a forrás szélessége kevesebb, mint `720 px` széles, úgy a kész encode-nak a `forrás-crop` szélesnek kell lennie.
  - 6.5) Eltérő képarányú release (pl. `OM`) nem dupeolja a korábbit és *vica versa*.
  - 6.6) A videót cropolni kell addig amíg maximum 1-1 px fekete sáv marad. A cropot a főcímnél kell meghatározni.
  - 6.7) A dirty lineok, dirty pixelek és faded lineok eltávolítása TILOS!
  - 6.8) Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line/faded line pl.: `bbmod`/`FixRowBrightness`/`BalanceBorders`/`EdgeFixer`
  - 6.9) Javítás után a widow lineok (eredetileg fekete sávok) eltávolítandóak (resize).
  - 6.10) A kódolt videó felbontása 1 pixellel térhet el a forrás alapján (cropolás után) számolttól, pl. 720x405 helyett 720x404 (mod2).
  - 6.11) Alacsonyabb felbontás kizárólag akkor megengedett, ha irreálisan magas bitrátát kapnánk a fentebb említett szélességek esetén.
  
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
  - 8.4) Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod, saiclabs.
  - 8.5) Az x264 header eltávolítása TILOS!
  - 8.6) Törekedjünk a minél újabb encoder használatára!
  - 8.7) Házibarkács encoderek használata TILOS!
  - 8.8) Kizárólag 8 bites YUV420 (YV12) videó megengedett.
  - 8.9) Kizárólag 2pass és CRF kódolások megengedettek.
  - 8.10) Szegmentált kódolás TILOS!
  - 8.11) `level 4.1`-et kell használni.
  - 8.12) Zónák használata megengedett.
  - 8.13) GPU encoding minden formája TILTOTT!
  - 8.14) Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`).
     - 8.14.1) A DVD-k nem négyzet alakú pixeleit négyzetté kell alakítani!
  - 8.15) A keyframe-ek közötti maximális távolság `FPS*20` lehet. (`FPS*10` ajánlott)
  - 8.16) `--min-keyint` értéke legalább `FPS/2`, maximum `FPS*2` lehet (`floor(FPS)` ajánlott, default).
  - 8.17) ColorMatrixot KÖTELEZŐ flaggelni (tipikusan `BT.709` BD esetén vagy `BT.470B/G` PAL DVD esetén).
     - 8.17.1) Ha a forrás HD és a ColorMatrix `undef`, akkor `BT.709`-nek kell flaggelni.
     - 8.17.2) Ha a forrás SD és a ColorMatrix `undef`, akkor meg kell vizsgálni, hogy `BT.601` vagy `BT.709`-el jobbak-e a színek és annak megfelelően flaggelni.
     - 8.17.3) `undef` flaggelése TILOS!
  - 8.18) ColorPrimaries és TransferFunction flaggelése opcionális (háttértudást igényel a stúdió setupról, csak akkor használd, ha tudod, mit csinálsz). Használata esetén a forrással egyezőre kell állítani. Bővebb infó: https://mod16.org/hurfdurf/?p=116
  - 8.19) Kötelező 16 referenciaképet használni (`--ref 16`).
  - 8.20) B frame-ek kikapcsolása TILOS. Minimum `3` egymás utáni B frame-t kell engedni (`--bframes 3` vagy több).
  - 8.21) A készült videónak DXVA-kompatibilisnek kell lennie (max. `High@L4.1`).
  - 8.22) `CABAC` kikapcsolása TILOS.
  - 8.23) `8x8dct` kikapcsolása TILOS.
  - 8.24) Kötelezően használandó partíciók: `i4x4,p4x4,i8x8,p8x8,b8x8` (`--partitions all`).
  - 8.25) `me` értéke KIZÁRÓLAG `umh`, `esa` vagy `tesa` lehet.
  - 8.26) `merange` értéke nem lehet 20-nál kisebb.
  - 8.27) `subme` értéke nem lehet 8-nál kisebb.
  - 8.28) `rc-lookahead` értéke nem lehet `FPS*2`-nél kisebb.
  - Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`). 
  - 8.29) Kizárólag Limited, TV range-ű release készíthető (`16-235`).
  - 8.30) `--vbv-maxrate` maximum `62500`, `--vbv-bufsize` maximum `78125` lehet, de egyik sem lehet kevesebb, mint `30000`.
  - 8.31) `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - 8.32) Adaptív kvantálás használata kötelező! `--aq-mode=1`/`2`/`3` (`3` ajánlott)
  - 8.33) A készített release bitrátája nem lehet nagyobb, mint a forrásé.
     - 8.32.1) Kivételt képeznek Hybrid release-ek, melyek több forrás felhasználásával készülnek.
  - 8.34) A videó bitrátáját vagy CRF értékét úgy kell megválasztani, hogy a képminőség transzparens legyen (amennyire lehet) a forráshoz képest.
  - 8.35) Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - 8.36) HDTV/PDTV forrás esetén logók maszkolása megengedett (pl. `InpaintFunc`).
  - 8.37) A stáblista, amennyiben nem tartalmaz extra jelenetet, kódolható alacsonyabb bitrátával.
  - 8.38) A `WEB-DL`-ek felmentést élveznek az összes 8-as pontbeli szabály alól, kivéve a 8.8-ast.

## 9) Audio
  - 9.1) Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata. Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi tag-ot megadni.
  - 9.2) Az eredeti hangsáv megtartása opcionális.
  - 9.3) Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - 9.4) Egyéb nyelvű hangok megtartása TILOS!
  - 9.5) Megengedett hangformátumok: `AC3` (`DD`), `AAC`. Amennyiben a forrás hang `E-AC3` (`DD+`/`DDP`) formátumú és maximum 6 csatornát tartalmaz, ez is engedélyezett; egyéb esetekben TILOS!
  - 9.6) `DTS`, `MP3`, `MP2`, és egyéb vicces formátumok használata TILOS!
  - 9.7) A hangsávok eredeti csatornaszámát meg kell tartani!
     - 9.7.1) Kivétel 8 csatornás hangok.
     - 9.7.2) 8 csatornás hang esetén vagy a core-t kell megtartani vagy egy 6 csatornás `DD@640`-et kell készíteni.
  - 9.8) 6 csatornás hang esetén kizárólag `AC3` (`DD`) elfogadott, melynek bitrátája 640 kbps, ha jobb forrásból készül, vagy az eredetivel megegyező (pl. DVD esetén).
  - 9.9) 2 csatornás `RETAiL` hang lehet `AC3` vagy `AAC` is.
     - 9.9.1)`AC3` esetén a forrással megegyező bitráta vagy jobb forrás esetén 192-256 kbps elfogadott.
     - 9.9.2) Amennyiben a forrás hang 2 csatornás `E-AC3`-at tartalmaz, megtarthatjuk. Törekedjünk a felesleges újrakódolások elkerülésére.
  - 9.10) 2 csatornás CUSTOM hangnál (TV-ből, WEB-ről felvett) JAVASOLT az `AAC` használata.
  - 9.11) Mono hang KIZÁRÓLAG `AAC` lehet.
  - 9.12) Lossy hangot csak losslessből szabad kódolni.
     - 9.12.1) Ez alól kivétel ha csak DTS hang érhető el.
  - 9.13) Maximum +/- 100 ms hangcsúszás megengedett.
  - 9.14) A hangok nyelvét kötelező Language tagben jelezni!
  
## 10) Audio kódolás
  - 10.1) AC3 esetében Dolby Certified encodert kell használni (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Dolby Media Encoder`, `Sonic Audio Transcoder`).
  - 10.2) A készített `AC3` nem tartalmazhat Copyright Protected flaget.
  - 10.3) `AAC` esetében elfogadott encoderek: QAAC, FDK, Nero
    - 10.3.1) Csak stereo/mono hangnál használható AAC.
    - 10.3.2) Javasolt beállítások:
       - 10.3.2.1) QAAC: `-V 90` - `-V 127` és `-q 2`
       - 10.3.2.2) FDK: `-m 4` vagy `-m 5`
       - 10.3.2.3) Nero: `-q 40` - `-q 75`
  - 10.5) A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - 10.6) Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  - 10.7) Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`)
  - 10.8) Resamplingre használható programok: `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.9) TimeStretchingre használható programok: `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge`, `SONAR` `élastique TimeStretch`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.10) Szegmentált kódolás használata TILOS!
  - 10.11) Commentary trackek használata csak akkor megengedett, ha kizárólag SD (DVD, PDTV, SD WEB-DL) forrás érhető el.
    - 10.11.1) Commentary track kizárólag AAC 2.0 (vagy mono) lehet és 80-160 kbps bitrátával rendelkezhet (mono esetén 40-80 kbps).
    - 10.11.2) (UHD) BluRay, HDDVD, (UHD) WEB-DL források esetén Commentary trackek használata TILOS (erre ott vannak a HD formátumok)!
  - 10.12) `AC3` és `E-AC3` esetén a `dialnorm` értéket meg kell tartani!
  
## 11) Feliratok
 - 11.1) Kizárólag SRT (SubRip) formátumú feliratok megengedettek!
     - 11.1.1) Az OCR karakterfelismerést a lehető legpontosabban kell elvégezni.
    - 11.1.2) A kész felirat lehetőleg kevés, érthetőséget nem zavaró helyesírási hibát tartalmazhat, de törekedjünk, hogy ne legyen benne hiba.
    - 11.1.3) A felismertetett feliraton javasolt egy spellchecker lefuttatása.
 - 11.2) A feliratokat tartalmaznia kell az mkv-nak, opcionálisan mellette is meghagyható.
 - 11.3) Kizárólag a magyar forced felirat megtartása kötelező, a többi opcionális.
 - 11.4) Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - 11.5) A muxolt feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani a forrással egyezőt)
 - 11.6) Az opcionálisan mellékelt feliratok kizárólag `.srt` formátumú és UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - 11.7) Feliratok képre égetése, hardcodeolása SZIGORÚAN TILOS!
 - 11.8) A feliratok nyelvét KÖTELEZŐ Language tagként beállítani.
 - 11.9) Title tag használata opcionális.
 - 11.10) Feliratok sorrendje:
    - 11.10.1) magyar forced (ha van)
    - 11.10.2) magyar full
    - 11.10.3) eredeti forced (ha van)
    - 11.10.4) eredeti full
    - 11.10.5) eredeti full SDH
  - 11.11) Forced feliratoknál a Forced flag használata ajánlott.
  - 11.12) További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
  - 11.13) Fansub kizárólag akkor használható, ha nem érhető el retail.
     - 11.13.1) Fansub használatát az NFO-ban kötelező jelezni.
  - 11.14) A feliratok nem csúszhatnak zavaró mértékben a képhez képest (max. ~600 ms).
 
## Aláírták és tudomásul vették
`boOk`, `Legacy`, `NaGa`, `NFC`, `pcroland`, `prldm`

## Banned grps
