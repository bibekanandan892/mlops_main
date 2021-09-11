import os
from glob import glob



data_dirs = ["Training_Batch_Files" , "Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + "/*.csv")
    # print(files)
    for filePath in files:
        # print(filePath)

        print(f"dvc add {filePath}")
        os.system(f"git rm -r --cached {filePath}")
        stop='stop tracking '
        os.system(f"git commit -m {stop} {filePath}")
        os.system(f"dvc add {filePath}")

print("\n #### all files added to dvc ####\ndvc")