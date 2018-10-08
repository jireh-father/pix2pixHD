import numpy as np
from PIL import Image
import glob, os

target_dir = "/home/data4/source/pix2pixHD/datasets/shirt/train_B"
output_dir = "/home/data4/source/pix2pixHD/datasets/shirt/train_B_resize"
assert os.path.isdir(target_dir)
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

image_filenames = glob.glob(os.path.join(target_dir, "*.jpg"))
image_size = 512
for fn in image_filenames:
    im = Image.open(fn)
    old_size = im.size  # old_size[0] is in (width, height) format
    desired_size = image_size
    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])
    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it

    new_im = Image.new("RGB", (desired_size, desired_size), "white")
    new_im.paste(im, ((desired_size - new_size[0]) // 2,
                      (desired_size - new_size[1]) // 2))
    new_im.save(os.path.join(output_dir, os.path.basename(target_dir)))
    img = np.asarray(new_im)
