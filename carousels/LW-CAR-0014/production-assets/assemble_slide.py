"""Planned layer assembly, without OCR, visual review or regeneration."""
import sys
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'production-assets'
number = int(sys.argv[1])
original = Image.open(sys.argv[2]).convert('RGBA')
fitted = ImageOps.contain(original, (1080, 1350), Image.Resampling.LANCZOS)
foreground = Image.new('RGBA', (1080, 1350))
foreground.alpha_composite(fitted, ((1080-fitted.width)//2, (1350-fitted.height)//2))
if number == 9:
    # Only the new top text is used. Discard any generated lower pixels;
    # the accepted original bitmap supplies all phone, hand and UI content.
    top = foreground.crop((0, 0, 1080, 650))
    foreground = Image.new('RGBA', (1080, 1350))
    foreground.alpha_composite(top)
foreground.save(ASSETS / f'slide-{number:02d}-foreground.png')
canvas = Image.open(ASSETS / 'background-dots.png').convert('RGBA')
canvas.alpha_composite(foreground)
canvas.alpha_composite(Image.open(ASSETS / 'original-wordmark-transparent.png'), (0, 0))
if number == 9:
    canvas.alpha_composite(Image.open(ASSETS / 'original-phone-hand-transparent.png'), (0, 650))
canvas.convert('RGB').save(ROOT / 'outputs' / f'slide-{number:02d}.png')
