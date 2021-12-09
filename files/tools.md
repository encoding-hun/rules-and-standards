# Videó
- [MKVToolNix](https://mkvtoolnix.download/downloads.html)
- [MakeMKV](https://www.makemkv.com/)
- [DGDemux](http://rationalqm.us/dgdemux/binaries/)
- x264
  - [tMod r3065](https://emma.cloud.tabdigital.eu/s/SK5WoB6mmcwtLJn) | [mirror](https://drive.google.com/file/d/1GwOfLl8Vdf0H0jgDYA5QvkGUpeAN8U-0)
  - [tMod r3075](https://github.com/jpsdr/x264/releases)
- [AvsPmod](https://github.com/gispos/AvsPmod/releases)
- [ffmpeg](https://ffmpeg.org/download.html)
- [VideoReDo TVSuite](https://ncore.pro/torrents.php?action=details&id=3248269)

## AviSynth+
- [AviSynth+ official build](https://github.com/AviSynth/AviSynthPlus/releases) | [3.7.1 béták](https://forum.doom9.org/showthread.php?t=181351)
- [Avisynth+ 3.7.0 (r3474) clang build](https://cloud01.opsdata.ch/index.php/s/xeMjWNC6biXcoeC) | [mirror](https://drive.google.com/drive/folders/1oJunPPq9C30d-ZIb_7RgXaFFaGujMoJY)
  - ~15%-kal gyorsabb az official buildnél.
  - A telepítéséhez először telepítsük az official buildet, majd futtassuk az `avisynth_updater.bat` fájlt admin módban.
- [AviSynth+ plugin pack](https://gitlab.com/uvz/AviSynthPlus-Plugins-Scripts) | [pluginok és scriptek listája](https://docs.google.com/spreadsheets/d/1-R-LZ2U5y6N6gV40PuYWQvXBzKCeGZ8iGDmQGpT85Jw)
- [DevIL 1.8.0 SDK](http://openil.sourceforge.net/download.php)
  - 32 bites AviSynth+ esetén másoljuk a `lib\x86\Release`-ben található `DevIL.dll`-t a `C:\Windows\SysWOW64` mappába.
  - 64 bites AviSynth+ esetén másoljuk a `lib\x64\Release`-ben található `DevIL.dll`-t a `C:\Windows\System32` mappába.

## VapourSynth
- [VapourSynth](https://github.com/vapoursynth/vapoursynth/releases)
- [VapourSynth Editor mod](https://github.com/YomikoR/VapourSynth-Editor/releases)
- [VapourSynth Editor 2](https://bitbucket.org/gundamftw/vapoursynth-editor-2/downloads/) | [Doom9](https://forum.doom9.org/showthread.php?t=181708)

# Audió
- [qaac, fdkaac, sox](https://cloud01.opsdata.ch/index.php/s/CWptD6kwGSSisHi)
- [Sony Sound Forge Pro v11.0.299](https://ncore.pro/torrents.php?action=details&id=1728976)
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
  - [official](https://github.com/Aegisub/Aegisub/releases) (régi!)
- [Notepad++](https://notepad-plus-plus.org/downloads/)
- [Subtitle Workshop](http://subworkshop.sourceforge.net/) | [VideHelp - újabb](https://www.videohelp.com/software/Subtitle-Workshop)

# NFO
- [PabloDraw](http://picoe.ca/products/pablodraw)
- [Moebius](https://github.com/blocktronics/moebius/releases)
- [neovim](https://github.com/neovim/neovim/releases)
  - A helyes megjelenítéshez a `~/.config/nvim/init.vim` fájlba rakjuk be a következő sort: `autocmd BufReadPre *.nfo :setlocal fileencodings=cp437,utf-8`
