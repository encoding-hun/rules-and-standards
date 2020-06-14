# Hungarian UHD-HD x265 Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Alapjául a 2020.04.15-ös nemzetközi scene szabályzatok szolgáltak, melyek a magyar helyzetre át lettek dolgozva.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.
  
## Érvényes
  2020-06-14-től

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
    - 1.6.1) Hossza 50-90 másodperc közötti legyen.
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
    - 2.4.1) TILOS: `Con.Man.2018.1080p.UHD.BluRay.HDR.DD5.1.x265.HUN-XYZ`
      - OK: `Con_Man.2018.1080p.UHD.BluRay.HDR.DD5.1.x265.HUN-XYZ`
    - 2.4.2) TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - 2.4.3) OK: `The.Con.Is.On.2018.1080p.UHD.BluRay.HDR.DD5.1.x265.HUN-XYZ`
  - 2.5) Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - 2.5.1) Sorozatok:
    `[series.name].[season].[resolution].[source].[dynrng].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.1.1) `[season]` tag legalább két jegyre megadandó (mind az évad, mind a rész), kivéve mini-series esetén.
       - 2.5.1.2) Adott sorozat adott évadán belül a taggelés nem változhat.
       - 2.5.1.3) Az évadok és részek számozásánál csak hivatalos források elfogadottak.
    - 2.5.2) Filmek:
    `[movie.title].[year].[resolution].[source].[dynrng].[audio.codec].[video.codec].[language]-[group]`
       - 2.5.2.1) A dokumentumfilmek filmnek minősülnek.
  - 2.6) A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - 2.7) `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - 2.8) `[audio.codec]` a film/sorozat eredeti nyelvére vonatkozik.
  - 2.9) `WEB-DL` és `WEBRip` forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. `NF.WEB-DL`, `AMZN.WEB-DL`)
  - 2.10) WEB-hez további guide:
    - 2.10.1) Az minősül `WEB-DL`-nek, ami nem lett újrakódolva az oldalról való leszedés után (vagy közben).
    - 2.10.2) Ha x264 settings-t látsz, az nem garancia arra, hogy `WEBRip`, `NF` és `AMZN` maga is `x264`-et használ.
    - 2.10.3) Egy `WEB-DL` nem feltétlenül jobb, mint egy `WEBRip` (pl. `2160p.WEB-DL`-ből kódolt `1080p.WEBRip` vs `1080p.WEB-DL`)
    - 2.10.4) `WEB-DLRip` megjelölés TILTOTT, `WEB-DL`-ből kódolt Rip = `WEBRip`
  - 2.11) `[dynrng]` értéke lehet: `SDR`, `HDR`, `HDR10Plus` (`HDR10+`), `DV`.
  - 2.12) `Rip`, `RiP` és `RIP` megjelölés is elfogadott.
  - 2.13) `REPACK` (`Repack`) és `RERiP` (`Rerip`) tagok használata kötelező, ha saját release-t javít valaki.
  - 2.14) `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
     - 2.14.1) `iNTERNAL`-ként kell feltütnetni minden olyan release-t, amely ellentmond a szabályzat bármely pontjának, de nem érhető el olyan forrás, amely teljesítené.
  - 2.15) TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
  - 2.16) `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.
  - 2.17) Nem Retail és nem WEB forrás esetén NFO-ban jelölni kell, hogy milyen forrás és esetlegesen miben tér el a Retail változattól. `READ.NFO` tag használata KÖTELEZŐ!
  - 2.18) `PROPER` = más hibás munkájának javítása; `REPACK` = muxolási hiba, hiányzó hang/felirat; `RERiP` = hibás videó/hang
     - 2.18.1) `PROPER` release-re érkező `PROPER`-t `REAL.PROPER`-nek kell taggelni (és így tovább a későbbieket, pl. `REAL.REAL.PROPER`)).
  - 2.19) `READ.NFO` és `PROPER`/`REPACK`/`RERiP` tagek együttes használata TILOS!
  - 2.20) Zavaró és felesleges tagek használata TILOS!
  
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
      * Videó dinamikatartománya
      * Videó színinformációi
      * Audiósávok nyelvei
      * Audiósávok típusai
      * Audiósávok csatornaszáma
      * Audiósávok bitrátája
      * Audió mintavételezési rátája (Sample rate)
      * Feliratok nyelve
      * Feliratok formátuma
  - 3.5) Más csapatok sértegetése, személyeskedés TILOS!
  - 3.6) `PROPER`/`REPACK`/`RERiP` release-ek esetén fel kell tüntetni a korábbi release problémáit. Képi vagy hangi `PROPER` esetén csatolni kell proofot, hogy valóban jobb az új release.
  - 3.7) Felesleges, zavaró dolgokat az NFO-ba elhelyezni TILOS!

## 4) Források
   - 4.1) Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
      - 4.1.1) Ez alól kivétel, ha eltérő vágással (`THETRICAL` vs. `EXTENDED`) rendelkezik a release.
   - 4.2) Források prioritása:<br />
   `UHD BluRay` > `WEBRip` nagyobb felbontású WEB-DL-ből kódolva > `WEB-DL` > `UHDTV`<br />
   `P2P` > `Scene` (kivétel retail lemezek esetén)
   - 4.3) `WEBRip` alacsonyabb felbontással való újratömörítése TILOS!
      - 4.3.1) Kivétel, ha nem érhető el magasabb felbontású `WEB-DL`.
   - 4.4) Amennyiben jobb minőségű UHD BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
   - 4.5) Ha az UHD forrás SDR, akkor kizárólag 2160p készíthető x265-tel, az 1080p-t x264-el kell elkészíteni (lásd másik szabályzat).
   - 4.6) Muxolni kizárólag olyan már kész release-re szabad, amely megfelel ezen szabályzatban rögzített pontoknak (kivéve az x265 verziójára vonatkozó szabálypont HDB internalok esetén). Törekedni kell az elérhető legjobb minőségű release felhasználására! Gyatra minőségű release-re való muxolás helyett saját encode készítése ERŐSEN AJÁNLOTT!
   
## 5) Video
  - 5.1) Már kész release alacsonyabb felbontással való újrakódolása SZIGORÚAN TILOS!
  - 5.2) Kizárólag egy videósáv használata megengedett.
  - 5.3) Egybefüggő videó darabolása TILOS! Egy lemezen található több rész (melyeket stáblista választ el) darabolása részekre KÖTELEZŐ!
     - 5.3.1) Ha a film több lemezen található és nincs a lemez végén stáblista, akkor össze kell a szegmenseket fűzni.
  - 5.4) Az előző rész tartalmából-t, a bevezető intrókat, és a stáblistát kötelező teljes hosszukban megtartani és a főcímmel együtt kódolni.
  - 5.5) A zavaró bevágásokat: műsorszám hirdetést tartalmaz, reklámok, FBI Warning, stb. el kell távolítani.
     - 5.5.1) Kivéve, amikor ez a videó/hang (közel) teljes újrakódolásával járna.
  - 5.6) Égetett felirattal rendelkező forrásokat lehetőleg kerüljük, kivéve ha szignifikánsan jobb a minősége.
  - 5.7) Hybrid encodeok megengedettek, ha ezzel jobb minőség érhető el.
     - 5.7.1) SDR és HDR források nem keverhetőek!
  - 5.8) A konténerben felbontásra és croppolásra extra metaadatokat megadni TILOS!
  - 5.10) A video sáv Language tagjának beállítása opcionális: vagy magyar vagy az eredeti nyelv.
  
## 6) Felbontás
  - 6.1) 1080p release maximális felbontása `1920x1080` lehet.
     - 6.1.1) 720p release készítése UHD forrásból kizárólag SDR esetén megengedett és kizárólag x264 segítségével (lásd másik szabályzat).
  - 6.2) 2160p release maximális felbontása `3840x2160` lehet.
  - 6.3) A videó felbontása mod2 kell legyen.
  - 6.4) A videó felskálázása SZIGORÚAN TILOS (pl. ha croppolás után 3836 széles a kép, tilos 3840-re felnagyítani)!
     - 6.4.1) Upscaled forrás esetén az eredeti, upscale előtti (vagy annál kisebb) felbontáson készíthető release. Ennek megkeresésésére jó pl. az UpscaleCheck és a getnative kódok. Köztes felbontások esetén a kerekítés szabályai érvényesek (pl. 900p és felette készíthető 1080p).
  - 6.5) Eltérő képarányú release (pl. `OM`) nem dupeolja a korábbit és *vica versa*.
  - 6.6) A videót cropolni kell addig amíg maximum 1-1 px fekete sáv marad. A cropot a főcímnél kell meghatározni.
  - 6.7) A dirty lineok, dirty pixelek és faded lineok eltávolítása TILOS!
  - 6.8) Az 1 px fekete sávok (widow line) és dirty line-ok javítása ajánlott.
    - widow line javítása pl.: `FillMargins`/`FillBorder`
    - dirty line/faded line pl.: `bbmod`/`FixRowBrightness`/`BalanceBorders`/`EdgeFixer`
  - 6.9) Javítás után a widow lineok (eredetileg fekete sávok) 2160p esetén eltávolíthatóak (resize vagy overlay), 1080p esetén kötelezően eltávolítandóak (resize).
  - 6.10) A kódolt videó felbontása 1 pixellel térhet el a forrás alapján (cropolás után) számolttól (mod2).
  
## 7) Filterek
  - 7.1) Kizárólag progresszív kép megengedett. Amennyiben szükséges deinterlacer vagy IVTC használata kötelező.
  - 7.2) Tonemapping SZIGORÚAN TILOS!
     - 7.2.1) Kivétel mintaképek vagy proof.
  - 7.3) Resize-oláshoz `z_Spline36Resize` (`resize.Spline36`) vagy `Spline36ResizeMod` ajánlott, a `Spline36Resize` tartalmaz egy apró chroma shifting bugot, használata kerülendő. (VapourSynth-et nem érinti.) További engedett resizerek: `z_Spline64Resize` (`resize.Spline64`), `BlackmanResize`.
     - 7.3.1) Tilos `Nearest Neighbor`, `Bilinear`, `Bicubic`, és egyéb gyenge resizerek használata.
  - 7.4) Kizárólag frame pontos forrásfilterek használhatóak (pl. `FFMS2`, `LSMASH`, `DGDecNV`).
     - 7.4.1) Pontatlan forrásfilterek használata TILOS (pl. `DirectShowSource`)!
  - 7.5) A kép minőségét jelentősen befolyásoló filterek használata (pl. grain eltávolítása, warp sharping, stb.) TILOS!
     - 7.5.1) A grain eltávolítása alól kivételt képez, ha az túlságosan magas bitrátát eredményezne.
     - 7.5.2) Számos upscaled anyagra a grain már a magasabb felbontáson kerül rá. Ilyen esetekben eltávolítása indokolt lehet.
  - 7.6) DeBlocking és DeBanding filterek használata megengedett, ezeket érdemes adott zónákra korlátozni (pl. `ReplaceFramesSimple`, `Trim`, vagy `ConditionalFilter` segítségével).
  - 7.7) A videó eredeti FPS értékét meg kell tartani. Interlace-elt forrás esetén 2 félképből 1-et kell képezni (értsd `50i`-ből `25p`-t kell készíteni). Ez alól kivétel lehet a sportfelvétel, ahol indokolt lehet az `50p`. Ekkor kizárólag `QTGMC` (`preset slow` vagy jobb) deinterlacer használható!
  - 7.8) Kizárólag CFR (constant framerate) mód használható! Amennyiben a forrás VFR-el rendelkezik, úgy ez felülírja az 7.6-os pontot.
  - 7.9) A dupe framek eltávolítása kötelező!
  
## 8) Videó kódolás
  - 8.1) Kizárólag x265 használható.
  - 8.2) Minimum `2.9`-es x265-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. `DON`, `TayTo`, `VietHD` és egyéb HDB internalok; megbízható források) muxolunk.
  - 8.3) Elfogadott x265 variánsok: vanilla, Yuuki
  - 8.4) Az x265 header eltávolítása TILOS!
  - 8.5) Törekedjünk a minél újabb encoder használatára!
  - 8.6) Házibarkács encoderek használata TILOS!
  - 8.7) 2160p SDR videó esetén kizárólag 8 bites YUV420 (YV12), HDR videó esetén kizárólag 10 bites YUV420 megengedett.
  - 8.8) Kizárólag 2pass és CRF kódolások megengedettek.
  - 8.9) Szegmentált kódolás TILOS!
  - 8.10) 2160p és 30 fps alatt `level 5.1`-et kell használni, 2160p felbontás és magasabb fps mellett `level 5.2`-t `SDR`, `HDR` és `HDR10Plus` esetén.
  - 8.11) Dolby Vision esetén kizárólag `level 8.1` elfogadott.
  - 8.12) Zónák használata megengedett.
  - 8.13) GPU encoding minden formája TILTOTT!
  - 8.14) Kizárólag 1:1 oldalarányú pixelek használata megengedett (`--sar 1:1`).
  - 8.15) A keyframe-ek közötti maximális távolság (`--keyint`) `FPS*20` lehet (`FPS*10` ajánlott, default).
  - 8.16) `--min-keyint` értéke legalább `FPS/2`, maximum `FPS*2` lehet (`floor(FPS)` ajánlott, default).
  - 8.17) Színadatok forrással egyező flaggelése KÖTELEZŐ!
     - 8.18) Megadandó paraméterek: `--colorprim`, `--transfer`, `--colormatrix`, `--chromaloc`, `--master-display`, `--max-cll`.
  - 8.18) Range megadása kötelező: `--range` (általában `limited`).
  - 8.19) `--ref` értéke maximum `6`, minimum `4` lehet.
     - 8.19.1) 1080p esetén `--ref` értéke kizárólag `6` lehet.
  - 8.20) B frame-ek kikapcsolása TILOS. Minimum `4` egymás utáni B frame-t kell engedni (`--bframes 4` vagy több).
  - 8.21) `--rd` értéke minimum `3` kell legyen.
  - 8.22) `--dynamic-rd` használata megengedett.
  - 8.23) `--ctu` értéke minimum `32`.
  - 8.24) `--rect` és `--amp` (aszimmetrikus partíciók) használata megengedett.
  - 8.24) `--limit-refs` értéke maximum `2` lehet ha `--rect` és `--amp` be van kapcsolva, egyébként `1`.
  - 8.25) Early skip, split RD, tskip-fast, adaptív frameduplikálás bekapcsolása TILOS (`--no-early-skip`, `--no-splitrd-skip`, `--no-tskip-fast`, `--no-frame-dup`, default)!
  - 8.26) `--max-merge` értéke legalább `2`.
  - 8.27) `--subme` értéke legalább `3`.
  - 8.28) `--merange` értéke legalább `32`.
  - 8.29) `--weightp` használata KÖTELEZŐ, `--weightb` használata ajánlott.
  - 8.30) `--psy-rd` és `--psy-rdoq` kikapcsolása TILOS!
  - 8.31) `--rc-lookahead` értéke nem lehet `FPS`-nél kisebb.
  - 8.32) `--lookahead-slices` maximum `4` lehet 2160p esetén és maximum `2` 1080p esetén.
  - 8.33) `--vbv-maxrate` és `--vbv-bufsize` értéke nem haladhatja meg a `160000`-et és egyik sem lehet kisebb, mint `100000`.
  - 8.34) Adaptív kvantálás használata kötelező! `--aq-mode=1`/`2`/`3`/`4` (`3` vagy `4` ajánlott).
  - 8.35) `--hevc-aq` és `--aq-motion` használata egyelőre nem javasolt.
  - 8.36) `--qg-size` mérete nem lehet nagyobb, mint `32`.
  - 8.37) `--deblock` kikapcsolása TILOS. Ajánlott beállítás filmek esetén: `-3:-3`.
  - 8.38) SAO kikapcsolása ajánlott (`--no-sao --selective-sao 0`).
  - 8.39) Mindenképpen high tier-t kell használni (`--high-tier`), be kell kapcsolni a header ismétlést (`--repeat-headers`), be kell kapcsolni az access unit delimitert (`--aud`), és a HRD adatok továbbítását (`--hrd`).
  - 8.40) `--uhd-bd` kapcsoló használata TILOS!
  - 8.41) HDR esetén `--hdr10` és `--hdr10-opt` kapcsolók használata KÖTELEZŐ.
  - 8.42) HDR10Plus esetén kizárólag `--dhdr10-info` használható, `--dhdr10-opt` használata TILOS!
  - 8.43) A készített release bitrátája nem lehet nagyobb, mint a forrásé.
     - 8.43.1) Kivételt képeznek Hybrid release-ek, melyek több forrás felhasználásával készülnek.
  - 8.44) A videó bitrátáját vagy CRF értékét úgy kell megválasztani, hogy a képminőség transzparens legyen (amennyire lehet) a forráshoz képest.
  - 8.45) Ajánlott frameserverek: AviSynth+ és VapourSynth.
  - 8.46) UHDTV forrás esetén logók maszkolása megengedett (pl. `InpaintFunc`).
  - 8.47) A stáblista, amennyiben nem tartalmaz extra jelenetet, kódolható alacsonyabb bitrátával.
  - 8.48) A `WEB-DL`-ek felmentést élveznek az összes 8-as pontbeli szabály alól, kivéve a 8.7-est.
  
## 9) Audio
  - 9.1) Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata. Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi tag-ot megadni.
  - 9.2) Az eredeti nyelvű hangsáv megtartása KÖTELEZŐ!
  - 9.3) Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - 9.4) Egyéb nyelvű hangok megtartása TILOS!
  - 9.5) Megengedett hangformátumok: `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `DTS`, `AAC`, `FLAC`.
     - 9.5.1) 2160p esetén `TrueHD`, `DTS-HD.MA`, és `DTS-X` is megengedett.
     - 9.5.2) `TrueHD`, `DTS`, `DTS-HD.MA`, és `DTS-X` hangokhoz KÖTELEZŐ `DD@640` compatibility track készítése.
     - 9.5.3) Lossless formátumok kereszt-konvertálása TILOS (pl. `TrueHD`-> `FLAC`)!
  - 9.6) `MP3`, `MP2`, és egyéb vicces formátumok használata TILOS!
  - 9.7) Más hangok encodeolása `AAC`-be kizárólag a kommentár sáv esetén megengedett.
     - 9.7.1) Kivétel, ha nyújtani és/vagy vágni kell, ekkor lehet AAC, amennyiben stereo vagy mono.
  - 9.8) LPCM hangot kötelező `TrueHD`, `DTS-HD.MA` vagy `FLAC` formátumba (film esetén) vagy AAC formátumba (kommentár esetén) konvertálni.
  - 9.9) A hangsávok eredeti csatornaszámát meg kell tartani!
  - 9.10) 1080p felbontás és 8 csatornás hang esetén DD+ formátumot kell használni (`DDP@1536`).
     - 9.10.1) Amennyiben a lemezen ilyen nem áll rendelkezésre, úgy a lossless hangból kell elkészíteni.
     - 9.10.2) 2160p felbontás esetén lásd 9.5.1 és 9.5.2-es pont.
  - 9.11) 2 csatornás `CUSTOM` hangnál (TV-ből vagy WEB-ről felvett) JAVASOLT az `AAC` használata.
  - 9.12) Amennyiben az érintetlen forráson kizárólag DTS található:
    - 9.12.1) `DDP@1024` kódolása (ajánlott, kivéve ha 768 kbps vagy kisebb a DTS bitrátája),
    - 9.12.2) DTS meghagyása, mellé `DD@640` (2 csatorna esetén `DD@256`) compatibility track készítése.
  - 9.13) Lossy hangot csak losslessből szabad kódolni.
     - 9.13.1) Ez alól kivétel ha csak DTS hang érhető el és compatibility tracket készítünk vagy 1080p-re `DDP@1024`-et.
  - 9.14) Maximum +/- 100 ms hangcsúszás megengedett.
  - 9.15) A hangok nyelvét kötelező Language tagben jelezni!
  
## 10) Audio kódolás
  - 10.1) `AC3` esetében Dolby Certified encodert kell használni (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Dolby Media Encoder`, `Sonic Audio Transcoder`).
  - 10.2) A készített `AC3` nem tartalmazhat Copyright Protected flaget.
  - 10.3) `DTS-HD.MA` hang készítéséhez kizárólag `DTS-HD Master Audio Suite` használható.
  - 10.4) `AAC` esetében elfogadott encoderek: `qaac` (`Apple AAC`), `FDK`, `Nero`.
    - 10.4.1) Csak stereo/mono hangnál használható AAC.
    - 10.3.2) Javasolt beállítások:
       - 10.3.2.1) qaac: `-V 90` - `-V 127` és `--no-delay --ignorelength` (egyéb kapcsolók használata tilos)
       - 10.3.2.2) FDK: `-m 4` vagy `-m 5` (és `-cutoff 20000` ffmpeg-es libfdk_aac használata esetén)
       - 10.3.2.3) Nero: `-q 40` - `-q 75`
  - 10.5) Compatibility `AC3` track készület FFmpeg (4.1 vagy újabb) vagy Aften (2009-12-26 vagy újabb) segítségével is.
  - 10.6) A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - 10.7) Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  - 10.8) Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`).
  - 10.9) Resamplingre használható programok: `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.10) TimeStretchingre használható programok: `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge`, `SONAR` `élastique TimeStretch`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 10.11) Commentary track maximum 2.0 lehet, `AC3` esetében maximum 192 kbps, `AAC` esetében 80-160 kbps.
  - 10.12) Szegmentált kódolás használata TILOS!
  - 10.13) `AC3`, `E-AC3`, `DTS`, `DTS-HD.MA`, és `DTS-X` esetén a `dialnorm` értéket meg kell tartani!
  
## 11) Feliratok
 - 11.1) Kizárólag SRT (SubRip) és PGS-SUP formátumú feliratok megengedettek!
    - 11.1.1) Az OCR karakterfelismerést a lehető legpontosabban kell elvégezni.
    - 11.1.2) A kész felirat lehetőleg kevés, érthetőséget nem zavaró helyesírási hibát tartalmazhat, de törekedjünk, hogy ne legyen benne hiba.
    - 11.1.3) A felismertetett feliraton javasolt egy spellchecker lefuttatása.
 - 11.2) A feliratokat tartalmaznia kell az `.mkv`-nak, opcionálisan mellette is meghagyható.
 - 11.3) Amennyiben HDR formátumról származó PGS-SUP feliratot teszünk SDR 2160p encodera, úgy a fényerejét 60%-al meg kell növelni.
 - 11.4) Amennyiben SDR formátumról származó PGS-SUP feliratot teszünk HDR encodera, úgy a fényerejét 60%-al le kell csökkenteni.
 - 11.5) Kötelező feliratok, amennyiben elérhetőek a forráson: magyar forced, magyar, eredeti nyelv forced, eredeti nyelv.
 - 11.6) Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - 11.7) A lemezen elérhető, főcímhez tartozó feliratokat `.srt` formátumban KÖTELEZŐ muxolni. PGS-SUP feliratok használata opcionális.
 - 11.8) Kommentár feliratokat csak akkor kötelező muxolni, ha az kapcsolódik az audiókommentárhoz.
    - 11.11.1) Egyéb esetben opcionálisak.
    - 11.11.2) Kommentár feliratokat elegendő PGS-SUP vagy SRT formátumban muxolni.
 - 11.9) A muxolt `.srt` feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani a forrással egyezőt)
 - 11.10) Az opcionálisan mellékelt `.srt` feliratok kizárólag UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - 11.11) PGS-SUP feliratoknál ajánlott a `zlib` tömörítés kikapcsolása.
 - 11.12) A feliratok nyelvét KÖTELEZŐ Language tagként beállítani.
 - 11.13) Title tag használata opcionális.
 - 11.14) Feliratok sorrendje:
    - 11.14.1) magyar forced (ha van), srt
    - 11.14.2) magyar full, srt
    - 11.14.3) eredeti forced (ha van), srt
    - 11.14.4) eredeti full, srt
    - 11.14.5) eredeti full SDH, srt
    - 11.14.6) kommentárok (opcionális), srt
    - 11.14.7) magyar forced (ha van), sup (opcionális)
    - 11.14.8) magyar full, sup (opcionális)
    - 11.14.9) eredeti forced (ha van), sup (opcionális)
    - 11.14.10) eredeti full, sup (opcionális)
    - 11.14.11) eredeti full SDH, sup (opcionális)
    - 11.14.12) kommentárok, sup (opcionális)
  - 11.15) Forced feliratoknál a Forced flag használata ajánlott.
  - 11.16) További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
  - 11.17) Fansub kizárólag akkor használható, ha nem érhető el retail.
     - 11.17.1) Fansub használatát az NFO-ban kötelező jelezni.
  - 11.18) A feliratok nem csúszhatnak zavaró mértékben a képhez képest (max. ~600 ms).
  
## Aláírták és tudomásul vették
`boOk`, `Legacy`, `NaGa`, `NFC`, `pcroland`, `prldm`

## Banned grps
