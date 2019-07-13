HD felbontású (1080p, 720p), x264-es kódolású filmekre vonatkozó szabályok és előírások

Érvényes: 2019-??-??-től

Ez a szabályzat nem vonatkozik a korábbi releasekre, az alábbiak alapján nem készíthető proper. Amennyiben bizonyítottan jobb minőségű release készült (video és/vagy hang és/vagy felirat), ezt READ.NFO taggal készítsük. Minden egyéb DUPE-nak minősül.

[Intro]
  Alapul a 2009.04.15, 2009.06.08-as magyar és 2011.01.29-es nemzetközi scene szabályzatok szolgáltak, nyilván a kornak megfelelően modernizálva és átdolgozva.

[Általános]
 - Tilos a DUPE, azaz a korábbival megegyező (vagy közel azonos) minőségű release készítése.
 - Kizárólag MKV konténer használata elfogadott.
 - A film csonkítása, trimmelése TILOS.
 - A stáblista amennyiben nem tartalmaz extra jelenetet kódolható alacsonyabb bitrátával.
 - A film tömörítése és darabolása TILOS.
 - A fő MKV mellé ajánlott SFV ellenőrzőösszeg készítése, de nem kötelező.

[Taggelés]
  - [movie title].[year].[resolution].[source].[audio codec].[video codec].[language]-[group]
  - [series.name].[season].[resolution].[source].[audio codec].[video codec].[language]-[group]
  - WEB-DL és WEBRip forrás esetén meg kell jelölni, hogy pontosan melyik oldalról való (pl. NF.WEB-DL, AMZN.WEB-DL)
  - A fájlok elérési útjának maximális hossza 260 karakter lehet.

[Források]
   - Csak jobb forrásból készített új release megengedett, minden egyéb DUPE.
   - Források prioritása: BD > HDDVD > WEB-DL/WEBRiP > HDTV
   - Amennyiben jobb minőségű BD elérhető, mint amiből a korábbi release készült, ezt READ.NFO taggel jelezni kell.
   - UHD forrás kizárólag akkor használható, ha SDR forrásról van szó.
   - HDR -> SDR tonemapping tilos, készíts x265 encode-ot helyette.

[Video]
  - Minimum r2800-as x264-as használata kötelező; kivétel, ha korábbi, minőségi encodera (pl. DON, TayTo, VietHD, egyéb HDB internalok) muxolunk.
  - Elfogadott x264 variánsok: vanilla, tMod, Yuuki, kMod. Házibarkács encoderek használata TILOS!
  - Kizárólag 8 bites YUV420 video megengedett.
  - Kizárólag 2pass és CRF kódolások megengedettek.
  - A video eredeti FPS értékét meg kell tartani.

[Audio]
  - AC3 esetében Dolby certified encodert kell használni (pl. Sound Forge)
  - AAC esetében qaac-t kell használni (csak stereo hangnál használható)
  - Nem lehet bloated a hang, bloatednak minősülnek:
      - 720p-n DTS@1509
      - 1080p-n DTS-HD.MA
  - Maximum +/- 100 ms hangcsúszás megengedett.
  - Commentary track maximum 2.0 lehet, AC3 esetében maximum 192kbps, AAC esetében -V 80-100 (qaac)
  -
  
[Feliratok]
 - A feliratok kizárólag SRT formátumú és UTF8-BOM vagy Windows-1250 kódolásúak lehetnek.
 - A feliratok nyelvét kötelező Language tag-ként beállítani.
 - Title tag használata opcionális.

[NFO]
 - NFO használata kötelező.
 - Az NFO-ban kötelező a következő információkat feltüntetni:
      * Release címe
      * Release készítésének ideje
      * Eredeti cím
      * IMDb URL
      * Video és hang forrása (feliratnál jelölni kell, amennyiben fansub)
      * A release mérete (csak a fő mkv, B, kB, MB, GB, kiB, MiB és GiB elfogadott)
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
  
[NUKE]
 - A szabályzat nem követése, figyelmen kívül hagyása NUKE-ot eredményez.
 - Indokok taggelése:
    - bad.res = hibás felbontás
    - bitstarved = alacsony bitráta
    - bloated = feleslegesen magas bitráta
    - audio.oos = hang csúszik a képhez képest
    - sub.oos = felirat csúszik a képhez képest
    - A READ.NFO-khoz és a PROPER-ekhez kötelező proof. Jobb kép esetén comparison, oos esetén kép a csúszásról.

[Aláírták és tudomásul vették]
