"""Export newly generated OPAQUE DOTS slides; add original brand/phone."""
import sys
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'production-assets'
number = int(sys.argv[1])
returned = Image.open(sys.argv[2]).convert('RGBA')
opaque = Image.new('RGBA', returned.size, '#F0F1EB')
opaque.alpha_composite(returned)
original = opaque.convert('RGB')
fitted = ImageOps.contain(original, (1080, 1350), Image.Resampling.LANCZOS)
canvas = Image.new('RGB', (1080, 1350), '#F0F1EB')
canvas.paste(fitted, ((1080-fitted.width)//2, (1350-fitted.height)//2))
canvas.save(ASSETS / f'slide-{number:02d}-generated-opaque.png')
if number == 9:
    # Only the new top text is used. Discard any generated lower pixels;
    # the accepted original bitmap supplies all phone, hand and UI content.
    top = canvas.crop((0, 0, 1080, 750))
    canvas = Image.open(ASSETS / 'background-dots.png').convert('RGB')
    canvas.paste(top, (0, 0))
canvas = canvas.convert('RGBA')
canvas.alpha_composite(Image.open(ASSETS / 'original-wordmark-layer.tiff'), (0, 0))
if number == 9:
    canvas.alpha_composite(Image.open(ASSETS / 'original-phone-hand-layer.tiff'), (0, 750))
canvas.convert('RGB').save(ROOT / 'outputs' / f'slide-{number:02d}.png')
