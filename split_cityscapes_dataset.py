import os, shutil, glob

label_dataset_path = "D:\data\cityspace\gtFine_trainvaltest\gtFine"
gt_dataset_path = "D:\data\cityspace\leftImg8bit_trainvaltest\leftImg8bit"
output_path = "D:\data\cityspace\pix2pix"

assert os.path.isdir(label_dataset_path)
assert os.path.isdir(gt_dataset_path)
if not os.path.isdir(output_path):
    os.makedirs(output_path)

gt_train_path = os.path.join(gt_dataset_path, "train")
# gt_val_path = os.path.join(gt_dataset_path, "val")
# gt_test_path = os.path.join(gt_dataset_path, "test")

label_train_path = os.path.join(label_dataset_path, "train")
label_val_path = os.path.join(label_dataset_path, "val")
# label_test_path = os.path.join(label_dataset_path, "test")

assert os.path.isdir(gt_train_path)
# assert os.path.isdir(gt_val_path)
assert os.path.isdir(label_train_path)
assert os.path.isdir(label_val_path)

output_train_img_path = os.path.join(output_path, "train_img")
output_train_inst_path = os.path.join(output_path, "train_inst")
output_train_label_path = os.path.join(output_path, "train_label")
output_test_inst_path = os.path.join(output_path, "test_inst")
output_test_label_path = os.path.join(output_path, "test_label")

if not os.path.isdir(output_train_img_path):
    os.makedirs(output_train_img_path)

if not os.path.isdir(output_train_inst_path):
    os.makedirs(output_train_inst_path)

if not os.path.isdir(output_train_label_path):
    os.makedirs(output_train_label_path)

if not os.path.isdir(output_test_inst_path):
    os.makedirs(output_test_inst_path)

if not os.path.isdir(output_test_label_path):
    os.makedirs(output_test_label_path)


def copy_files(target_dir, output_path, pattern=None):
    dirs = glob.glob(os.path.join(target_dir, "*"))
    for d in dirs:
        p = "*.png" if pattern is None else "*%s.png" % pattern
        target_files = glob.glob(os.path.join(d, p))
        for target_file in target_files:
            shutil.copy(target_file, os.path.join(output_path, os.path.basename(target_file)))


copy_files(gt_train_path, output_train_img_path)
copy_files(label_train_path, output_train_inst_path, "instanceIds")
copy_files(label_train_path, output_train_label_path, "labelIds")

copy_files(label_val_path, output_test_inst_path, "instanceIds")
copy_files(label_val_path, output_test_label_path, "labelIds")
