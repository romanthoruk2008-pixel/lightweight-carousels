"""Extract original approved phone pixels for the requested real-UI insertion.

The source is the owner-approved LW-CAR-0001 ending. The phone is kept at its
original scale and tilt: no UI rendering, retyping, warping, or aspect change.
This preparation happens before the new ending is generated.
"""
from pathlib import Path
from PIL import Image, ImageDraw

assets = Path(__file__).resolve().parent
checkout = assets.parents[2]
source_path = checkout / 'carousels/LW-CAR-0001/outputs/slide-08.png'
source = Image.open(source_path).convert('RGBA')
# Fixed contour around the existing phone bezel; the original hand/background
# are outside this matte. Preserve all source pixels inside the screen.
points = [
    (493, 528), (526, 525), (572, 530), (836, 566), (862, 573),
    (885, 590), (900, 611), (909, 638), (910, 666), (904, 710),
    (823, 1350), (346, 1350), (348, 1290), (360, 1180),
    (378, 1050), (397, 896), (410, 795), (419, 713),
    (424, 657), (433, 607), (446, 570), (467, 543),
]
scale = 4
mask = Image.new('L', (1080 * scale, 1350 * scale), 0)
ImageDraw.Draw(mask).polygon([(x * scale, y * scale) for x, y in points], fill=255)
mask = mask.resize((1080, 1350), Image.Resampling.LANCZOS)
source.putalpha(mask)
source.save(assets / 'approved-phone-pixels.png')
print('Original phone pixels prepared at 1:1 scale; final placement translates y by +200px.')
