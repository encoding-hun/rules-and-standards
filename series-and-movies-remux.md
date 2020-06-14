# Hungarian REMUX Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.
  
## Érvényes
  2020-06-14-től

## Utolsó frissítés
  2020-06-14
  
## 1) Általános
 - 1.1) Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - 1.2) SDR és HDR (ide értve a `HDR10Plus`-t is) tartalmakra kizárólag `.mkv` konténer használata elfogadott.
   - 1.2.1) Ajánlott muxer: MKVToolNix (mkvmerge).
      - 1.2.1.1) Törekedjünk a lehető legfrissebb változat használatára.
   - 1.2.2) Header compression használata TILOS.
   - 1.2.3) HDR kép és `.mkv` konténer esetén a Dolby Vision sáv megtartása TILOS! Dolby Vision release az 1.3-as pontnak megfelelően készíthető.
 - 1.3) Dolby Vision esetén kizárólag `.mp4` és `.m2ts` konténer elfogadott.
 - 1.4) A film csonkítása, trimmelése TILOS.
 - 1.5) A film tömörítése (pl. rar, zip stb.) és darabolása TILOS.
 - 1.6) A fő MKV (MP4/M2TS) mellé `SFV` vagy `MD5` ellenőrzőösszeg készítése ajánlott, de nem kötelező.
 - 1.7) Sample készítése opcionális.
    - 1.7.1) Hossza 50-90 másodperc közötti legyen.
    - 1.7.2) A Sample nem származhat az epizód/film legelejéről, valamint legvégéről.
    - 1.7.3) A Sample-t újrakódolás nélkül, a végső encode-ból kell kivágni.
    - 1.7.4) A Sample-t egy `Sample` nevű mappába vagy a fő MKV (MP4/M2TS) mellé kell helyezni. Utóbbi esetben a filenévben kell jelölni, hogy melyik a sample.
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
    - 2.4.1) TILOS: `Con.Man.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`
      - OK: `Con_Man.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`
    - 2.4.2) TILOS: `con.man.mkv`, `con.mkv`
      - OK: `con_man.mkv`, `conman.mkv`
    - 2.4.3) OK: `The.Con.Is.On.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`
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
  - 2.8) Elfogadott `[video.codec]` tagek: `AVC`, `VC1`, `MPEG2`, `HEVC`, `AV1`.
  - 2.9) `REPACK` (`Repack`) és `RERiP` (`Rerip`) tagok használata kötelező, ha saját release-t javít valaki.
  - 2.10) `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére TILOS!
     - 2.10.1) `iNTERNAL`-ként kell feltütnetni minden olyan release-t, amely ellentmond a szabályzat bármely pontjának, de nem érhető el olyan forrás, amely teljesítené.
  - 2.11) TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
  - 2.12) `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.
     - 2.12.1) A Blu-ray forrásokat `BluRay`-nek kell taggelni.
     - 2.12.2) Az UHD Blu-ray forrásokat `UHD.BluRay`-nek kell taggelni.
     - 2.12.3) A HD-DVD forrásokat `HDDVD`-nek kell taggelni.
  - 2.13) UHD formátum esetén fel kell tüntetni, hogy `SDR`, `HDR` vagy `HDR10Plus` (`HDR10+`) a kép.
  - 2.14) Dolby Vision-re elfogadott tag-ek: `DV`, `Dolby.Vision`.
  - 2.15) Dolby Vision esetén fel kell tüntetni, hogy single (`SL`) vagy dual layer (`DL`) a kép.
  - 2.16) Ha a hangsáv tartalmaz Atmos kiegészítést, úgy azt `Atmos` taggel jelölni kell.
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
   `(UHD)` `BluRay` > `HDDVD`, `DTheater`
   - 4.3) Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
   - 4.4) Muxolni kizárólag olyan már kész releasere szabad, amely megfelel ezen szabályzatban rögzített pontoknak. Törekedni kell az elérhető legjobb minőségű release felhasználására!
   
## 5) Video
  - 5.1) A videó újrakódolása SZIGORÚAN TILOS!
  - 5.2) Kizárólag egy videósáv használata megengedett.
     - 5.2.1) Kivétel dual layer Dolby Vision formátum.
  - 5.3) 2D-s releasehez nem használható 3D-s film bal vagy jobb szeméhez tartozó kép, kivéve, ha a filmből nem létezik 2D-s kiadás.
  - 5.4) Egybefüggő videó darabolása TILOS! Egy lemezen található több rész (melyeket stáblista választ el) darabolása részekre KÖTELEZŐ!
     - 5.4.1) Ha a film több lemezen található és nincs a lemez végén stáblista, akkor össze kell a szegmenseket fűzni.
  - 5.5) Az előző rész tartalmából-t, a bevezető intrókat, és a stáblistát kötelező teljes hosszukban megtartani és a főcímmel együtt kódolni.
  - 5.6) A zavaró bevágásokat: műsorszám hirdetést tartalmaz, reklámok, FBI Warning, stb. el kell távolítani.
     - 5.6.1) Kivéve, amikor ez a videó/hang (közel) teljes újrakódolásával járna.
  - 5.7) Égetett felirattal rendelkező forrásokat lehetőleg kerüljük, kivéve ha szignifikánsan jobb a minősége.
  - 5.8) Hybrid remuxok megengedettek, ha ezzel jobb minőség érhető el.
  - 5.9) A konténerben felbontásra és croppolásra extra metaadatokat megadni TILOS!
  - 5.10) A video sáv Language tagjának beállítása opcionális: vagy magyar vagy az eredeti nyelv.
  - 5.11) Encoder által beírt header eltávolítása SZIGORÚAN TILOS!
  - 5.12) Színekre vonatkozó metaadatok (pl. ColorMatrix, ColorPrimaries, TransferFunction, Chroma Location, CLL, stb.) eltávolítása SZIGORÚAN TILOS!
  
## 6) Audio
  - 6.1) Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata. Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi tag-ot megadni.
  - 6.2) Az eredeti nyelvű hangsáv megtartása KÖTELEZŐ!
  - 6.3) Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - 6.4) Egyéb nyelvű hangok megtartása TILOS!
  - 6.5) Az elérhető legjobb minőségű hangok megtartása KÖTELEZŐ!
  - 6.6) A hangsávok újrakódolása SZIGORÚAN TILOS!
     - 6.6.1) Kivétel compatibility trackek és audiokommentár.
  - 6.7) Megengedett hangformátumok: `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `DTS`, `DTS-HD.MA`, `DTS-X`, `TrueHD`, `AAC`, `FLAC`.
  - 6.8) LPCM használata TILOS!
     - 6.8.1) Az ilyen hangokat `DTS-HD.MA`, `TrueHD` vagy `FLAC` formátumba kell tömöríteni.
  - 6.9) A hangsávok eredeti csatornaszámát meg kell tartani!
  - 6.10) Minden `DTS`, `DTS-HD.MA`, és `DTS-X` formátumú hang mellé KÖTELEZŐ `DD` compatibility track készítése!
  - 6.11) `TrueHD` formátum esetén a `DD` compatibility stream megtartása KÖTELEZŐ!
     - 6.11.1) Ha a lemezen lévő compatibility track csak 384-448 kbps bitrátájú, akkor készíthető a `TrueHD` hangból 640 kbps bitrátájú hang is.
  - 6.12) Audiokommentár megtartása opcionális.
  - 6.13) Audiokommentár formátuma kizárólag `DD` lehet vagy `AAC`.
  - 6.14) Maximum +/- 100 ms hangcsúszás megengedett.
  - 6.15) A hangok nyelvét kötelező Language tagben jelezni!

## 7) Audio kódolás
  - 7.1) AC3 esetében erősen ajánlott Dolby Certified encodert (pl. `Sound Forge AC-3 Pro`, `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Dolby Media Encoder`, `Sonic Audio Transcoder`).
  - 7.2) Egyéb esetben kizárólag FFmpeg (4.1 vagy újabb) vagy Aften (2009-12-26 vagy újabb) használható.
  - 7.3) A készített AC3 nem tartalmazhat Copyright Protected flaget.
  - 7.4) AAC esetében elfogadott encoderek: QAAC, FDK, Nero
    - 7.4.1) Csak stereo/mono hangnál használható AAC.
    - 7.4.2) Javasolt beállítások:
       - 7.4.2.1) QAAC: `-V 90` - `-V 127` és `-q 2`
       - 7.4.2.2) FDK: `-m 4` vagy `-m 5`
       - 7.4.2.3) Nero: `-q 40` - `-q 75`
  - 7.5) A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - 7.6) Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  - 7.7) Ha a hangot nyújtani kell előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`)
  - 7.8) Resamplingre használható programok: `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 7.9) TimeStretchingre használható programok: `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge`, `SONAR` `élastique TimeStretch`, `Audacity`, `SoX`, és `Adobe Audition`.
  - 7.10) Commentary track maximum 2.0 lehet, AC3 esetében maximum 192 kbps, AAC esetében 80-160 kbps.
  - 7.11) Szegmentált kódolás használata TILOS!
  - 7.12) AC3 és E-AC3 esetén a `dialnorm` értéket meg kell tartani!

## 8) Feliratok
 - 8.1) Kizárólag SRT (SubRip) és PGS-SUP formátumú feliratok megengedettek!
    - 8.1.1) Az OCR karakterfelismerést a lehető legpontosabban kell elvégezni.
    - 8.1.2) A kész felirat lehetőleg kevés, érthetőséget nem zavaró helyesírási hibát tartalmazhat, de törekedjünk, hogy ne legyen benne hiba.
    - 8.1.3) A felismertetett feliraton javasolt egy spellchecker lefuttatása.
 - 8.2) A feliratokat tartalmaznia kell az `.mkv`-nak, opcionálisan mellette is meghagyható.
 - 8.3) `.mp4` konténer használata esetén a feliratok muxolása TILOS! A feliratokat a file mellé, vagy egy `Subs` mappába kell helyezni.
 - 8.4) `.m2ts` konténer használata esetén kizárólag PGS-SUP feliratokat szabad muxolni. Az `.srt` feliratokat a file mellé, vagy egy `Subs` mappába kell helyezni.
 - 8.5) Amennyiben HDR formátumról származó PGS-SUP feliratot teszünk SDR remuxra, úgy a fényerejét 60%-al meg kell növelni.
 - 8.6) Amennyiben SDR formátumról származó PGS-SUP feliratot teszünk HDR remuxra, úgy a fényerejét 60%-al le kell csökkenteni.
 - 8.7) Kötelező feliratok, amennyiben elérhetőek a forráson: magyar forced, magyar, eredeti nyelv forced, eredeti nyelv.
 - 8.8) Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
 - 8.9) A lemezen elérhető, főcímhez tartozó feliratokat `.srt` és `.sup` formátumban is KÖTELEZŐ muxolni/mellékelni.
    - 8.9.1) Kivéve 3D-s filmek esetén, ahol elegendő a PGS-SUP használata.
 - 8.10) Ha a felirat egyéb helyről származik (pl. WEB), akkor készíthető custom PGS-SUP felirat, de nem kötelező.
 - 8.11) Kommentár feliratokat csak akkor kötelező muxolni, ha az kapcsolódik az audiókommentárhoz.
    - 8.11.1) Egyéb esetben opcionálisak.
    - 8.11.2) Kommentár feliratokat elegendő PGS-SUP vagy SRT formátumban muxolni.
 - 8.12) A muxolt `.srt` feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani a forrással egyezőt)
 - 8.13) Az opcionálisan mellékelt `.srt` feliratok kizárólag UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
 - 8.14) PGS-SUP feliratoknál ajánlott a `zlib` tömörítés kikapcsolása.
 - 8.15) A feliratok nyelvét KÖTELEZŐ Language tagként beállítani.
 - 8.16) Title tag használata opcionális.
 - 8.17) Feliratok sorrendje:
    - 8.17.1) magyar forced (ha van), srt
    - 8.17.2) magyar full, srt
    - 8.17.3) eredeti forced (ha van), srt
    - 8.17.4) eredeti full, srt
    - 8.17.5) eredeti full SDH, srt
    - 8.17.6) kommentárok (opcionális), srt
    - 8.17.7) magyar forced (ha van), sup
    - 8.17.8) magyar full, sup
    - 8.17.9) eredeti forced (ha van), sup
    - 8.17.10) eredeti full, sup
    - 8.17.11) eredeti full SDH, sup
    - 8.17.12) kommentárok (opcionális), sup
  - 8.18) Forced feliratoknál a Forced flag használata ajánlott.
  - 8.19) További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
  - 8.21) Fansub kizárólag akkor használható, ha nem érhető el retail.
     - 8.21.1) Fansub használatát az NFO-ban kötelező jelezni.
  - 8.21) A feliratok nem csúszhatnak zavaró mértékben a képhez képest (max. ~600 ms).
  
