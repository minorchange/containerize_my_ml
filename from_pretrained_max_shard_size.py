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


def load_custom_cached_tokenizer_and_model(
    from_pretr_mod_fu, from_pretr_tok_fu, model_id, custom_model_cache_path
):
    try:
        print("----> Trying to load from file")
        tokenizer = from_pretr_tok_fu(custom_model_cache_path)
        model = from_pretr_mod_fu(custom_model_cache_path)
        print("----> Loaded from file")
        return model, tokenizer
    except:
        print("----> Loading from file did not work")
        print("----> Loading from web")
        tokenizer = cache_with_max_shard_size(
            from_pretrained_fu=from_pretr_tok_fu,
            model_id=model_id,
            custom_model_folder=custom_model_cache_path,
        )
        model = cache_with_max_shard_size(
            from_pretrained_fu=from_pretr_mod_fu,
            model_id=model_id,
            custom_model_folder=custom_model_cache_path,
        )
        clear_model_cache(model_id)
        print("----> Loaded from web and saved to file")
        return model, tokenizer
