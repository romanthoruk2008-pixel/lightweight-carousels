"""Pre-generation production layers from approved source; no output review."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
ASSETS = ROOT / 'production-assets'
source = Image.open(REPO / 'carousels/LW-CAR-0001/outputs/slide-08.png').convert('RGB')

# Fixed task background. Supersampling gives smooth 6 px diameter dots.
scale = 4
background = Image.new('RGB', (1080 * scale, 1350 * scale), '#F0F1EB')
draw = ImageDraw.Draw(background)
for y in range(0, 1350, 45):
    for x in range(0, 1080, 45):
        draw.ellipse(((x-3)*scale, (y-3)*scale, (x+3)*scale-1, (y+3)*scale-1), fill='#D4D4CC')
background.resize((1080, 1350), Image.Resampling.LANCZOS).save(ASSETS / 'background-dots.png')

# Keep original glyph pixels; make the old light background transparent.
strip = source.crop((0, 0, 1080, 110)).convert('RGBA')
pixels = np.array(strip)
alpha = (pixels[:, :, :3].mean(axis=2) < 200).astype(np.uint8) * 255
strip.putalpha(Image.fromarray(alpha))
strip.save(ASSETS / 'original-wordmark-layer.tiff', compression='tiff_deflate')

# Preserve source RGB of phone/UI/hand at original coordinates. The dark
# exterior contours form the matte; close the bottom crop and fill interiors.
layer = source.crop((0, 520, 1080, 1350)).convert('RGBA')
pixels = np.array(layer)
barrier = pixels[:, :, :3].mean(axis=2) < 160
barrier = ndimage.binary_closing(barrier, iterations=1)
barrier[-2:, 75:920] = True
filled = ndimage.binary_fill_holes(barrier)
labels, count = ndimage.label(filled)
sizes = ndimage.sum(filled, labels, range(1, count + 1))
matte = labels == (int(np.argmax(sizes)) + 1)
layer.putalpha(Image.fromarray(matte.astype(np.uint8) * 255))
layer.save(ASSETS / 'original-phone-hand-layer.tiff', compression='tiff_deflate')
