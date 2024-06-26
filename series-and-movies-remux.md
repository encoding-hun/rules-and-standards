# Hungarian REMUX Release Rules and Standards
  - Célunk egy olyan lefektetett és átlátható szabályrendszer létrehozása, mely kizárólag minőségi szempontokat vesz figyelembe.
  - Ez a szabályzat nem vonatkozik a korábbi release-ekre, az alábbiak alapján nem készíthető proper. Amennyiben jobb minőségű BD/stb. elérhető, mint amiből a korábbi release készült, az új release-t `READ.NFO` taggel kell ellátni. Minden egyéb `DUPE`-nak minősül. Ez alól kivétel, ha a korábbi release súlyos hibával rendelkezik, pl. hangcsúszás, képhiba stb., ekkor `PROPER`-elhető.

## 1) Általános
  - 1.1) Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
  - 1.2) SDR és HDR (ide értve a `HDR10Plus`-t is) tartalmakra kizárólag `.mkv` konténer használata elfogadott.
    - 1.2.1) Ajánlott muxer: MKVToolNix (mkvmerge). Törekedjünk a lehető legfrissebb változat használatára.
    - 1.2.2) Header compression használata tilos.
    - 1.2.3) HDR kép és `.mkv` konténer esetén a különálló Dolby Vision sáv (EL külön sáv) megtartása tilos! Dolby Vision release az 1.3-as pontnak megfelelően készíthető.
    - 1.2.4) Minden muxolt sávnak `track-enabled`-nek kell lennie (`--track-enabled-flag 0:1`).
  - 1.3) Dolby Vision esetén `.mkv` (ha a BL és EL egy videósávban van, SL), valamint `.mp4` és `.m2ts/.ts` (ha a BL és EL két videósávban van, DL) konténer elfogadott.
  - 1.4) A film csonkítása, trimmelése tilos.
  - 1.5) A film tömörítése (pl. rar, zip stb.) és darabolása tilos.
  - 1.6) A fő MKV (MP4/M2TS) mellé `SFV` vagy `MD5` ellenőrzőösszeg készítése ajánlott, de nem kötelező.
  - 1.7) Sample készítése opcionális.
    - 1.7.1) Hossza 50-90 másodperc közötti legyen.
    - 1.7.2) A sample nem származhat az epizód/film legelejéről, valamint legvégéről.
    - 1.7.3) A sample-t újrakódolás nélkül, a végső encode-ból kell kivágni.
    - 1.7.4) A sample-t egy `Sample` nevű mappába vagy a fő MKV (MP4/M2TS) mellé kell helyezni. Utóbbi esetben a filenévben kell jelölni, hogy melyik a sample.
  - 1.8) Chapterlist használata KÖTELEZŐ, amennyiben a forrás tartalmaz ilyet!
    - 1.8.1) Chapterek elnevezése opcionális, kizárólag magyar vagy angol fejezetcímek használhatóak.
  - 1.9) Vízjelek használata tilos!

## 2) Tagelés - könyvtárnév
  - 2.1) Ékezetes karakterek használata tilos!
  - 2.2) Engedélyezett karakterek: `a-z` `A-Z` `0-9` `.` `-` `_` `+`.
    - 2.2.1) Ismételt kötőkarakterek használata tilos! (pl. `...` vagy `-.`)
    - 2.2.2) Amennyiben a cím tiltott karaktert tartalmaz (pl. `*`), akkor `.` vagy `-`-el helyettesítendő, vagy kiírható az a karakter, amit helyettesít, pl.: `T@gged` -> `Tagged`, `Elk*rtuk` -> `Elkurtuk`.
  - 2.3) Tilos két azonos nevű file létrehozása, amelyek kizárólag kis és nagy betűben térnek el (pl. film-release és Film-release)!
  - 2.4) A következő nevek nem használhatók könyvtár- és fájlnevek elején ponttal elválasztva: `CON`, `PRN`, `AUX`, `NUL`, `COM*`, `LPT*` (ahol `*` egy számot jelöl).\
         tilos: `Con.Man.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`\
         ok: `Con_Man.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`\
         tilos: `con.man.mkv`, `con.mkv`\
         ok: `con_man.mkv`, `conman.mkv`\
         ok: `The.Con.Is.On.2018.1080p.BluRay.REMUX.DTS-HD.MA.5.1.AVC.HUN-XYZ`
  - 2.5) Sorozatok és filmek ajánlott tagelése (a sorrendtől el lehet térni):
    - 2.5.1) Sorozatok: `[series.name].[season].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
      - 2.5.1.1) `[season]` tag legalább két jegyre megadandó (mind az évad, mind a rész), kivéve mini-series esetén.
      - 2.5.1.2) Adott sorozat adott évadán belül a tagelés nem változhat.
      - 2.5.1.3) Az évadok és részek számozásánál csak hivatalos források elfogadottak.
      - 2.5.1.4) Napi sorozat esetén, amennyiben évad/epizód nem ismert, vagy nem tagolt, a következő jelölés alkalmazandó: `[series.name].[YYYY].[MM].[DD].[resolution].[source].[audio.codec].[video.codec].[language]-[group]` (itt `[YYYY]` az évet, `[MM]` a hónapot, `[DD]` a napot jelöli).
    - 2.5.2) Filmek: `[movie.title].[year].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`
      - 2.5.2.1) A dokumentumfilmek filmnek minősülnek.
    - 2.5.3) Sportközvetítések és egyéb TV-s műfajok: `[event.name].[YYYY[-YY]].[team.vs.team].[resolution].[source].[audio.codec].[video.codec].[language]-[group]`.
  - 2.6) A könyvtár és fájlok nevének maximális hossza 255 karakter lehet, de ajánlott 250 alatt megállni.
  - 2.7) `[series.name]` és `[movie.title]` KIZÁRÓLAG eredeti vagy angol nyelvű lehet.
  - 2.8) Elfogadott `[video.codec]` tagek: `AVC`, `VC1`, `MPEG2`, `HEVC`, `AV1`.
  - 2.9) `REPACK` (`Repack`) tag használata kötelező, ha saját release-t javít valaki.
  - 2.10) `iNT` vagy `iNTERNAL` tag használata DUPE elkerülésére tilos!
    - 2.10.1) `iNTERNAL`-ként kell feltüntetni minden olyan release-t, amely ellentmond a szabályzat bármely pontjának, de nem érhető el olyan forrás, amely teljesítené.
  - 2.11) TV-ből származó hangok esetén `CUSTOM` tag használata opcionális.
  - 2.12) `RETAiL` (eredeti lemezről készült) tag használata ajánlott, ha korábban készült olyan release, ahol a hang nem a BD/HDDVD lemezről származik.
    - 2.12.1) A Blu-ray forrásokat `BluRay`-nek kell tagelni.
    - 2.12.2) Az UHD Blu-ray forrásokat `UHD.BluRay`-nek kell tagelni.
    - 2.12.3) A HD-DVD forrásokat `HDDVD`-nek kell tagelni.
  - 2.13) UHD formátum esetén fel kell tüntetni, hogy `HDR`, `HDR10Plus` (`HDR10+`), `HLG`, vagy `DV` a kép.
    - 2.13.1) `SDR` taggelése opcionális.
  - 2.14) Dolby Vision-re elfogadott tagek: `DV`, `Dolby.Vision`, `DoVi`.
  - 2.15) Dolby Vision esetén opcionálisan fel lehet tüntetni, hogy single (`SL`) vagy dual layer (`DL`) a kép.
    - 2.15.1) Ha egy `SL` tartalom Dolby Vision és HDR(10+) metadatával is rendelkezik úgy vagy `DV`-nek kell taggelni és NFO-ban jelezni, hogy van HDR/SDR compatibility layer vagy mindegyik tagnek meg kell jelennie, pl. `DV.HDR`.
  - 2.16) Ha a hangsáv tartalmaz Atmos kiegészítést, úgy azt `Atmos` taggel jelölni kell.
  - 2.17) `PROPER` = más hibás munkájának javítása; `REPACK` = saját hiba javítása
    - 2.17.1) `PROPER` release-re érkező `PROPER`-t `REAL.PROPER`-nek kell tagelni (és így tovább a későbbieket, pl. `REAL.REAL.PROPER`).
  - 2.18) `READ.NFO` és `PROPER`/`REPACK`/`RERiP` tagek együttes használata tilos!
  - 2.19) Zavaró és felesleges tagek használata tilos!
  - 2.20) Több magyar szinkron esetén jelölni kell a szinkronok számát, pl.: `2xHUN`.

## 3) NFO
  - 3.1) NFO használata kötelező.
  - 3.2) Az NFO nyelve angol és/vagy magyar.
  - 3.3) Magyar nyelvű NFO esetén az angol kifejezések szakszerű fordításának használata kötelező (ebben segít a Wikipedia).
  - 3.4) Az NFO-ban kötelező a következő információkat feltüntetni:
    - release címe
    - release készítésének ideje
    - eredeti cím
    - IMDb URL
    - hossz (másodperc megadása nem kötelező), sorozat esetén átlag hossz és/vagy összes hossz
    - videó forrása, `WEB` esetén oldal megjelölése
    - videóhoz használt encoder
    - videó felbontása
    - videó bitrátája
    - videó FPS-e
    - videó dinamikatartománya, `UHD` esetén
    - videó színinformációi, `UHD` esetén
    - `DV` kép esetén a profil száma
    - audiosávok forrása(i), `WEB` esetén oldal megjelölése
    - audiosávok nyelvei
    - audiosávok típusai
    - audiosávok csatornaszáma
    - audiosávok bitrátája
    - audió mintavételezési rátája (sampling rate), opcionális 48kHz esetén
    - feliratok forrása(i) fansub esetén
    - feliratok nyelve
    - feliratok formátuma
  - 3.5) Más csapatok sértegetése, személyeskedés tilos!
  - 3.6) `PROPER`/`REPACK` release-ek esetén fel kell tüntetni a korábbi release problémáit. Képi vagy hangi `PROPER` esetén csatolni kell proofot, hogy valóban jobb az új release.
  - 3.7) Felesleges, zavaró dolgokat az NFO-ba elhelyezni tilos!
  - 3.8) Egy release-ben csak egy NFO lehet. (pl. évadpackoknál részenkénti és COMPLETE packnál évadonkénti NFO tiltott.)

## 4) Források
  - 4.1) Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
    - 4.1.1) Ez alól kivétel, ha eltérő vágással (`THEATRICAL` vs. `EXTENDED`) rendelkezik a release.
  - 4.2) Források prioritása:\
         `(UHD)` `BluRay` > `HDDVD`, `DTheater`
  - 4.3) Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt `READ.NFO` taggel jelezni kell.
  - 4.4) Muxolni kizárólag olyan már kész release-re szabad, amely megfelel ezen szabályzatban rögzített pontoknak. Törekedni kell az elérhető legjobb minőségű release felhasználására!
  - 4.5) Ha egy videóból már készült `DV` és `HDR` sávot is tartalmazó `SL` `Profile 8.1`-es release (`DV.HDR`), úgy külön csak `DV` (`Profile 5`) és csak `HDR`-t tartalmazó release későbbi kiadása már DUPE.
    - 4.5.1) `DL` és `SL` nem DUPE-olja egymást.
    - 4.5.2) Ha egy videóból létezik `DL` `DV` release, de `SL` `DV.HDR` még nem, akkor kiadható külön csak `HDR` release, de javasolt a két sáv megfelelő egyesítése és `DV.HDR` release készítése.

## 5) Videó
  - 5.1) A videó újrakódolása szigorúan tilos!
  - 5.2) Kizárólag egy videósáv használata megengedett.
    - 5.2.1) Kivétel dual layer Dolby Vision formátum.
  - 5.3) 2D-s release-hez nem használható 3D-s film bal vagy jobb szeméhez tartozó kép, kivéve, ha a filmből nem létezik 2D-s kiadás.
  - 5.4) Egybefüggő videó darabolása tilos! Egy lemezen található több rész (melyeket stáblista választ el) darabolása részekre KÖTELEZŐ!
    - 5.4.1) Ha a film több lemezen található és nincs a lemez végén stáblista, akkor össze kell a szegmenseket fűzni.
  - 5.5) Az előző rész tartalmából-t, a bevezető intrókat és a stáblistát kötelező teljes hosszukban megtartani és a főcímmel együtt kódolni.
  - 5.6) A zavaró bevágásokat: műsorszám hirdetést tartalmaz, reklámok, FBI Warning, stb. el kell távolítani.
    - 5.6.1) Kivéve, amikor ez a videó/hang (közel) teljes újrakódolásával járna.
  - 5.7) Égetett felirattal rendelkező forrásokat lehetőleg kerüljük, kivéve ha szignifikánsan jobb a minősége.
  - 5.8) Hybrid remuxok megengedettek, ha ezzel jobb minőség érhető el.
  - 5.9) A konténerben felbontásra és cropolásra extra metaadatokat megadni tilos!
  - 5.10) A videosáv Language tagjének beállítása opcionális: vagy magyar vagy az eredeti nyelv.
  - 5.11) Encoder által beírt header eltávolítása szigorúan tilos!
  - 5.12) Színekre vonatkozó metaadatok (pl. ColorMatrix, ColorPrimaries, TransferFunction, Chroma Location, CLL, stb.) eltávolítása szigorúan tilos!

## 6) Audió
  - 6.1) Magyar hangsávot tartalmazó release esetén kötelező a `HUN` (`Hun`) tag használata.
    - 6.1.1) Amennyiben a release nem tartalmaz magyar hangsávot, úgy nem kell nyelvi taget megadni.
    - 6.1.2) Amennyiben a magyar hang az eredeti, úgy nem kell nyelvi taget megadni.
  - 6.2) A hangok nyelvét kötelező a Language tagben jelezni!
  - 6.3) Az eredeti nyelvű hangsáv megtartása KÖTELEZŐ!
  - 6.4) Nem angol nyelvű, eredeti hangsáv esetén az angol hang (már amennyiben létezik) megtartása opcionális.
  - 6.5) Egyéb nyelvű hangok megtartása tilos!
  - 6.6) Az elérhető legjobb minőségű hangok megtartása KÖTELEZŐ!
  - 6.7) A hangsávok újrakódolása szigorúan tilos!
    - 6.7.1) Kivétel compatibility trackek és audiokommentár.
    - 6.7.2) Kivétel azon hangok, amelyek nyújtást igényelnek vagy egyéb olyan beavatkozást, mely során az újrakódolás nem elkerülhető.
  - 6.8) Megengedett hangformátumok:
    - 6.8.1) 1.0: `AAC`, `FLAC`
    - 6.8.2) 2.0: `AAC` (ajánlott), `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `FLAC`
      - 6.8.2.1) `AC3` (`DD`) esetén a forrással megegyező bitráta vagy jobb forrás esetén 192-384 kbps elfogadott. Lossy források esetén ajánlott a 192-256 kbps, míg 384 kbps lossless források esetén.
    - 6.8.3) 5.1: `AC3` (`DD`), `E-AC3` (`DD+`/`DDP`), `AAC`, `FLAC`, `DTS(-HD MA)`, `TrueHD`
      - 6.8.3.1) `AC3` (`DD`) 640 kbps, ha jobb forrásból készül, vagy az eredetivel megegyező (pl. DVD esetén).
      - 6.8.3.2) `E-AC3` (`DD+`/`DDP`) 128-192 kbps/csatorna (768-1152 kbps), ha jobb forrásból készül, vagy az eredetivel megegyező.
    - 6.8.4) 7.1: `E-AC3` (`DD+`/`DDP`), `DTS(-HD MA)`, `TrueHD`, `DTS-X`
      - 6.8.4.1) 128-192 kbps/csatorna (1024-1536 kbps), ha jobb forrásból készül, vagy az eredetivel megegyező.
  - 6.9) Kizárólag stúdió által készített surround hangok használhatóak fel, házilag felkevertek tilosak. TV-s surround hang esetén mindig győződjünk meg, hogy valódi surround-e, amennyiben nem, downmixeljük. Pl.: `ffmpeg -i input.ac3 -ac 2 -f sox - | sox -p -S -b 24 --norm=-1 output.wav`
  - 6.10) Más formátumok, pl. 5.1-es `AAC`, `FLAC` vagy `DTS-HD MA/DTS-X` használata esetén KÖTELEZŐ `DD@640` (2 csatorna esetén `DD@256` vagy `AAC`) compatibility track készítése.
    - 6.10.1) `TrueHD` formátum esetén az AC3 (`DD`) compatibility stream megtartása KÖTELEZŐ! Ha a lemezen lévő compatibility track csak 384-448 kbps bitrátájú, akkor készíthető a `TrueHD` hangból 640 kbps bitrátájú hang is.
  - 6.11) Lossless formátumok kereszt-konvertálása tilos (pl. `TrueHD` -> `FLAC`).
    - 6.11.1) Ez alól kivételt képeznek az LPCM hangok, amiket kötelező `TrueHD`, `DTS-HD.MA` vagy `FLAC` formátumba vagy kommentár esetén akár `AAC` formátumba konvertálni.
  - 6.12) A hangsávok eredeti csatornaszámát meg kell tartani!
  - 6.13) A maximális megengedett hangcsúszás 100 ms.
  - 6.14) Audiokommentár megtartása opcionális.
  - 6.15) Amennyiben a forrás audió megtartható újrakódolás nélkül, úgy annak újrakódolása tilos. (pl. a forrás megengedett formátumú és nem kell nyújtani.)
  - 6.16) Egy másik forrásból származó hang akkor számít jobb minőségűnek, hogyha a lowpass (cutoff) frekvencia 16 kHz alatt legalább 1 kHz-el, 16 kHz felett legalább 1.5 kHz-el magasabb, és a többlet adat nem sztochasztikus (dithering miatt belekerülő) zaj. Ha ez teljesül, akkor készíthető új release, egyéb esetben `dupe`. Kérdéses esetekben proofként egy-egy spektrum mutatása szükséges a két hangról.
    - 6.16.1) Ez alól kivétel, hogyha az alacsonyabb lowpass-szel rendelkező hang minősége hallhatóan jobb.
    - 6.16.2) További kivételt képez, hogyha jobb forrásból elérhető a hang és a bitrátakülönbség meghaladja a 192 kbps-t `DD` és `DTS` esetén, vagy a `128` kbps-t `DD+` és `AAC` esetén. `DD+` és `DD` hangok bitrátáinak összehasonlítása a 7.11-es pontban rögzítettek szerint `1.7`-es szorzófaktorral történik. `AAC` és `DD` között ugyanezt az átváltást használjuk. Például egy `DD@448`-as DVD hang mindig cserélhető egy BD-ről származó `DD@640`-re.
  - 6.17) A hangok sorrendje:
    - magyar (ha van)
    - eredeti
    - angol (ha az eredeti nem ez; opcionális)
    - kommentárok (opcionális)

## 7) Audiokódolás
  - 7.1) `AC3`/`E-AC3` kódolása esetén erősen ajánlott Dolby Certified encodert (pl. `Dolby Encoding Engine`/[`deew`](/files/tools.md), `Minnetonka SurCode`, `Sonic Foundry Soft Encode`, `Sonic Audio Transcoder`) használni, egyéb esetben kizárólag FFmpeg (4.1 vagy újabb) használható.
  - 7.2) A készített `AC3` (`DD`) nem tartalmazhat Copyright Protected flaget.
  - 7.3) `DTS-HD.MA` hang készítéséhez kizárólag `DTS-HD Master Audio Suite` használható.
  - 7.4) `AAC` esetében elfogadott encoderek: `qaac` (`Apple AAC`), `FDK`, `Nero`.
    - 7.4.1) Csak sztereó/monó hangnál használható `AAC`.
    - 7.4.2) Javasolt beállítások:
      - 7.4.2.1) `qaac`: `-V 90` - `-V 127` és `--no-delay --ignorelength` (egyéb kapcsolók használata tilos)
      - 7.4.2.2) `FDK`: `-m 4` vagy `-m 5` (és `-cutoff 20000` FFmpeg-es libfdk_aac használata esetén)
      - 7.4.2.3) `Nero`: `-q 40` - `-q 75`
  - 7.5) A hangok mintavételezését (sampling rate) tilos megváltoztatni!
  - 7.6) Belső konverziók esetén meg kell tartani (vagy jobbat kell használni), mint az eredeti hang bitmélysége és mintavételezési rátája.
  - 7.7) Ha a hangot nyújtani kell, előtte meg kell győződni, hogy Resampling vagy Time Stretch algoritmusra van-e szükség (pl. `hdtools compare`).
    - 7.7.1) Resamplingre használható programok: `SoX`, `hdtools resample`, `eac3to`, `Sound Forge`, `Audacity` és `Adobe Audition`.
    - 7.7.2) TimeStretchingre használható programok: `SoX`, `hdtools tstretch`, `Prosoniq TimeFactory II`, `Sound Forge`, `SONAR` `élastique TimeStretch`, `Audacity` és `Adobe Audition`.
  - 7.8) Szegmentált kódolás használata tilos!
  - 7.9) A `dialnorm` értékeket mérés alapján kell beállítani vagy forrásból kell megtartani. (előbbi preferált)
    - 7.9.1) A `Dolby Encoding Engine`/[`deew`](/files/tools.md) magától beállítja, így itt erre nincs szükség. A mérés kézzel `Adobe Audition` segítségével történhet, a `C` csatornára kapott `ITU-R BS.1770-3 Loudness` értéket kell `dialnorm` értéknek megadni.
  - 7.10) `E-AC3` hang `AC3`-ba történő kódolásakor a megengedett bitráták az eredeti `1.7`-szereséhez legközelebb eső két bitráta (nagyjából ennyivel jobb a `DD+` algoritmus). Például: ha a forrás `DDP@256`, akkor `256 * 1.7 = 435.2`, tehát 384 vagy 448 kbps-es `AC3` készíthető.

## 8) Feliratok
  - 8.1) Kizárólag `SRT` (SubRip), `SSA`/`ASS` és `PGS-SUP` formátumú feliratok megengedettek!
    - 8.1.1) `SSA`/`ASS` feliratok használata esetén kötelező `SRT`-t is tartalmaznia az mkv-nak. Ez alól animék kivételt képeznek.
    - 8.1.2) `SSA`/`ASS` feliratok használata esetén tartalmaznia kell az mkv-nak a fontokat.
  - 8.2) Az OCR karakterfelismerést a lehető legpontosabban kell elvégezni.
    - 8.2.1) A kész felirat lehetőleg kevés, érthetőséget nem zavaró helyesírási hibát tartalmazhat, de törekedjünk, hogy ne legyen benne hiba.
    - 8.2.2) A felismertetett feliraton javasolt spellchecker / helyesírás-ellenőrző lefuttatása.
  - 8.3) A feliratokat tartalmaznia kell az mkv-nak, de opcionálisan mellette is meghagyhatóak az `SRT` formátumúak.
  - 8.4) `.mp4` konténer használata esetén a feliratok muxolása tilos! A feliratokat a file mellé, vagy egy `Subs` mappába kell helyezni.
  - 8.5) `.m2ts` konténer használata esetén kizárólag PGS-SUP feliratokat szabad muxolni. Az `.srt` feliratokat a file mellé, vagy egy `Subs` mappába kell helyezni.
  - 8.6) Amennyiben HDR formátumról származó PGS-SUP feliratot teszünk SDR remuxra, úgy a fényerejét 60%-kal meg kell növelni.
  - 8.7) Amennyiben SDR formátumról származó PGS-SUP feliratot teszünk HDR remuxra, úgy a fényerejét 60%-kal le kell csökkenteni.
  - 8.8) Kötelező feliratok, amennyiben elérhetőek: magyar forced, magyar, eredeti forced, eredeti.
  - 8.9) Magyar filmek esetén ajánlott az angol nyelvű felirat (ha van) megtartása is.
  - 8.10) A lemezen elérhető, főcímhez tartozó feliratokat `.srt` és `.sup` formátumban is KÖTELEZŐ muxolni/mellékelni.
    - 8.10.1) Kivéve 3D-s filmek esetén, ahol elegendő a PGS-SUP használata.
  - 8.11) Ha a felirat egyéb helyről származik (pl. WEB), akkor készíthető custom PGS-SUP felirat.
  - 8.12) Kommentárfeliratokat csak akkor kötelező muxolni, ha az kapcsolódik az audiokommentárhoz.
    - 8.12.1) Egyéb esetben opcionálisak.
    - 8.12.2) Kommentárfeliratokat elegendő PGS-SUP vagy SRT formátumban muxolni.
  - 8.13) A muxolt `.srt` feliratokat megfelelő karakterkódolással kell muxolni (UTF8 vagy beállítani a forrással egyezőt)
  - 8.14) Az opcionálisan mellékelt `.srt` feliratok kizárólag UTF8(-BOM) vagy ANSI kódolásúak lehetnek.
  - 8.15) PGS-SUP feliratoknál ajánlott a `zlib` tömörítés kikapcsolása.
  - 8.16) A feliratok nyelvét KÖTELEZŐ language tagként beállítani, pl.: `--language 0:hun`.
  - 8.17) Track-name használata opcionális, pl.: `--track-name 0:'Name'`.
    - 8.17.1) Forced feliratoknál track-name és forced flag használata ajánlott, pl.: `--forced-flag 0:yes --track-name 0:'Forced'`.
    - 8.17.2) SDH feliratoknál track-name és hearing-impaired flag használata ajánlott, pl.: `--hearing-impaired-flag 0:yes --track-name 0:'SDH'`.
  - 8.18) Retail felirat használata kötelező, amennyiben elérhető.
    - 8.18.1) Fansub használható Retail felirat mellett is, ilyenkor meg kell adni hogy melyik melyik, pl.: `--track-name 0:'Fansub'`, `--track-name 0:'NF'`.
    - 8.18.2) Silány minőségű gépi fordítás (pl. Google Translate) használata tilos.
  - 8.19) Feliratok sorrendje:
    - magyar forced (ha van)
    - magyar full
    - eredeti forced (ha van)
    - eredeti full
    - eredeti full SDH
    - kommentárok (ha van) (opcionális)
  - 8.20) Az SRT feliratok minden esetben meg kell előzzék az egyéb formátumú feliratokat.
  - 8.21) További feliratok opcionálisan muxolhatóak vagy mellékelhetőek. FIGYELEM: bizonyos lejátszók nem képesek mind az MKV specifikációban leírt 127 sáv kezelésére, így ajánlott 16 sáv alatt maradni (ebbe a videó- és hangsávok is beletartoznak).
  - 8.22) A maximális megengedett feliratcsúszás 300 ms.
