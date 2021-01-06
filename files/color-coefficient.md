### Using x264’s color coefficient flagging properly
OK so you have a HD transport stream, you encode it and don’t use colormatrix() in Avisynth because you realized back in 2008 or so that doing so was kind of a dumb idea. Now you want to tell decoders what color coefficients the video uses so it will (hopefully) look correct everywhere, even if you downscale it so ffdshow’s/Haali’s resolution-based autodetection fails. What to do?

The answer to this is obviously “flag it in the h264 bitstream” (if you’re one of those scrubs who still use Xvid just ignore the issue, nobody cares about Xvid anymore). The problem with this answer is that nobody understand what the hell vui.txt actually means. However, in some recent conversation in #darkhold Kovensky linked to a paste where pengvado/akupenguin explained it in more detail.

More specifically:
* **–COLORMATRIX** specifies what coefficients are used when converting YUV to RGB. This is the one you want to use.
* **–COLORPRIM** specifies what color primaries (see for example the Wikipedia page about sRGB) the RGB uses. Setting this properly most likely requires knowledge of the studio equipment used to master the stream and/or its settings, so just leave it undefined. No one without a color calibrated monitor would ever notice or care, even if decoders/renderers actually supported this.
* **–TRANSFER** specifies the gamma curve used for the RGB. Like –colorprim, setting this correctly probably requires knowledge you don’t have, so don’t set it at all. Again, only people with calibrated studio monitors will ever notice or care.

**TL;DR:** Use `--colormatrix bt709` if your source is a HD transport stream; `--colormatrix bt470bg` if it is an SD transport stream.
