# Videó
- [MKVToolNix](https://mkvtoolnix.download/downloads.html) | continuous buildek: [win](https://mkvtoolnix.download/windows/continuous/64-bit/), [linux](https://mkvtoolnix.download/appimage/continuous)
- [MakeMKV](https://www.makemkv.com/)
- [DGDemux](http://rationalqm.us/dgdemux/binaries/)
- [DGDecNV](http://rationalqm.us/dgdecnv/binaries/)
- [DGMPGDec](http://rationalqm.us/dgmpgdec/)
- x264
  - [vanilla r3094](https://artifacts.videolan.org/x264/release-win64/)
  - [tMod r3094](https://emma.cloud.tabdigital.eu/s/rrHWew8eH8R8ezc) | [mirror](https://drive.google.com/drive/folders/18UzdSN66G0I646w9sP1qsCZuPO52CwYP)
    <details><summary>There are few minor differences compared to the jpsdr builds:</summary>

    - patch for building with mingw on Linux instead of Windows
    - audio is disabled
    - not applied patches
      - AviSynth 16-bit hack (AviSynth+ native high bit depth is officiallly long time supported)
      - f3kdb usage for converting from higher bit depth to output bit depth
      - double unicode buffer
      - weightp 2 for Blu-ray
      - rbsp_alignment_zero_bit</details>
  - [tMod r3085](https://github.com/jpsdr/x264/releases)
  - [Patman r3079](https://github.com/Patman86/x264-Mod-by-Patman/releases)
  - [kMod r3059](https://github.com/cshmnyfy/x264-kMod-patches/releases)
  - [aMod r3059+18](https://github.com/DJATOM/x264-aMod/releases)
- x265
  - [vanilla 3.5+29](http://msystem.waw.pl/x265/)
  - [Patman 3.5+21+12](https://github.com/Patman86/x265-Mod-by-Patman/releases)
  - [aMod 3.5+20](https://github.com/DJATOM/x265-aMod/releases/)
  - [Yuuki 3.5+2](https://down.7086.in/x265-Yuuki-Asuna/)
- [ffmpeg](https://ffmpeg.org/download.html)
- [VideoReDo TVSuite](https://ncore.pro/torrents.php?action=details&id=3248269) | [béta buildek](https://www.videoredo.net/msgBoard/index.php?resources/videoredo-tvsuite-v6-beta.3/)
- [tsMuxer](https://github.com/justdan96/tsMuxer/releases)
- [dovi_tool](https://github.com/quietvoid/dovi_tool/releases)
- [hdr10plus_tool](https://github.com/quietvoid/hdr10plus_tool/releases)

### AviSynth+
- [AviSynth+ official build](https://github.com/AviSynth/AviSynthPlus/releases) | [béta buildek](https://forum.doom9.org/showthread.php?t=181351)
- [Avisynth+ 3.7.1 (r3593) clang build](https://cloud01.opsdata.ch/index.php/s/xeMjWNC6biXcoeC) | [mirror](https://drive.google.com/drive/folders/1oJunPPq9C30d-ZIb_7RgXaFFaGujMoJY)
  - ~7%-kal gyorsabb az official buildnél.
  - A telepítéséhez először telepítsük az official buildet, majd futtassuk az `avisynth_updater.bat` fájlt admin módban.
- [AvsPmod](https://github.com/gispos/AvsPmod/releases)
- [AviSynth+ plugin pack](https://gitlab.com/uvz/AviSynthPlus-Plugins-Scripts) | [pluginok és scriptek listája](https://docs.google.com/spreadsheets/d/1-R-LZ2U5y6N6gV40PuYWQvXBzKCeGZ8iGDmQGpT85Jw)
- [DevIL 1.8.0 SDK](http://openil.sourceforge.net/download.php)
  - 32 bites AviSynth+ esetén másoljuk a `lib\x86\Release`-ben található `DevIL.dll`-t a `C:\Windows\SysWOW64` mappába.
  - 64 bites AviSynth+ esetén másoljuk a `lib\x64\Release`-ben található `DevIL.dll`-t a `C:\Windows\System32` mappába.

### VapourSynth
- [VapourSynth](https://github.com/vapoursynth/vapoursynth/releases)
- [VapourSynth-Classic](https://github.com/AmusementClub/vapoursynth-classic/releases)
- [VapourSynth Editor mod](https://github.com/YomikoR/VapourSynth-Editor/releases)
- [VapourSynth Editor 2](https://bitbucket.org/gundamftw/vapoursynth-editor-2/downloads/) | [Doom9](https://forum.doom9.org/showthread.php?t=181708)
- [Portable FATPACK](https://github.com/theChaosCoder/vapoursynth-portable-FATPACK/releases)

# Audió
- [deew (Dolby Encoding Engine Wrapper)](https://github.com/pcroland/deew)
- [qaac, fdkaac, sox](https://cloud01.opsdata.ch/index.php/s/CWptD6kwGSSisHi)
- [Audacity](https://drive.google.com/file/d/1D_RFVYeRzGLObhrLnMYm3SNZfcAOL-jO)
  - ffmpeg libek letöltése innen: [LINK](https://github.com/88keyz/Zeranoe/releases/tag/20200831-4a11a6f-w32-shared)
  - ffmpeg beállítása ez alapján: [LINK](https://manual.audacityteam.org/man/installing_ffmpeg_for_windows.html)
- [Adobe Audition](https://ncore.pro/torrents.php?action=details&id=3249667)
- [audiostretch, aacenc, audiocomp, downmix bash/zsh snippets](https://github.com/encoding-hun/snippets)

# Felirat
- [SubtitleEdit](https://nikse.dk/SubtitleEdit/) | [GitHub](https://github.com/SubtitleEdit/subtitleedit/releases)
- [VisualSubSync-Enhanced](https://github.com/Red5goahead/VisualSubSync-Enhanced/releases)
- [Gaupol](https://otsaloma.io/gaupol/)
- AegiSub
  - [Daydream Cafe Edition](https://github.com/Ristellise/AegisubDC/releases)
  - [TypesettingTools](https://github.com/TypesettingTools/Aegisub) | [buildek](https://thevacuumof.space/builds/)
  - [official](https://github.com/Aegisub/Aegisub/releases) *(régi!)*
- [Notepad++](https://notepad-plus-plus.org/downloads/)
- Subtitle WorkShop
  - [6.0e](https://sourceforge.net/projects/subtitle-workshop-classic) | [mirror](https://www.videohelp.com/software/Subtitle-Workshop)
  - [6.0b official](http://subworkshop.sourceforge.net/) *(régi!)*

# NFO
- [PabloDraw](http://picoe.ca/products/pablodraw)
- [Moebius](https://github.com/blocktronics/moebius/releases)
- [neovim](https://github.com/neovim/neovim/releases)
  - A helyes megjelenítéshez a `~/.config/nvim/init.vim` fájlba rakjuk be a következő sort: `autocmd BufReadPre *.nfo :setlocal fileencodings=cp437,utf-8`

# Comparison
- [compup-nc](https://github.com/pcroland/compup-nc) *(comparison feltöltő nCore-ra és BitHUmenre)*

# Guides
- [Aicha - Advanced Encoding Guide](https://silentaperture.gitlab.io/mdbook-guide)
- [UHDBits - The Encoding Guide](https://encoding-guide.neocities.org/)
- [Irrational-Encoding-Wizardry - Fansubbing Guide](https://guide.encode.moe/)
- [x264 settings](http://www.chaneru.com/Roku/HLS/X264_Settings.htm)
- [BodoiCuHo -  x264 Encoding Guide](https://bodoicuho.ucoz.ru/) *(outdated)*
