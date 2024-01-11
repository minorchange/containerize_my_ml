import glob
import json
import re
from collections import OrderedDict
from transformers import TRANSFORMERS_CACHE


import os
import shutil


def delete_child_folders_containing_substring(
    parent_folder, substring, protect_substring="bkp"
):
    for root, dirs, files in os.walk(parent_folder):
        for folder in dirs:
            if substring in folder and protect_substring not in folder:
                folder_path = os.path.join(root, folder)
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path}")


def clear_model_cache(model_name):
    cache_folder = TRANSFORMERS_CACHE
    delete_child_folders_containing_substring(
        parent_folder=cache_folder, substring=model_name
    )


def cache_with_max_shard_size(from_pretrained_fu, model_id, custom_model_folder):
    obj = from_pretrained_fu(model_id)
    obj.save_pretrained(custom_model_folder, max_shard_size="200MB")
    return obj


# modelRegex = "huggingface\.co\/(.*)(pytorch_model\.bin$|resolve\/main\/tf_model\.h5$)"

# cachedModels = {}
# cachedTokenizers = {}
# for file in cache_folder:
#     with open(file) as j:
#         data = json.load(j)
#         isM = re.search(modelRegex, data["url"])
#         if isM:
#             cachedModels[isM.group(1)[:-1]] = file
#         else:
#             cachedTokenizers[data["url"].partition("huggingface.co/")[2]] = file

# cachedTokenizers = OrderedDict(sorted(cachedTokenizers.items(), key=lambda k: k[0]))

# print()
