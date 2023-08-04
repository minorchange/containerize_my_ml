import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import inspect
from os.path import abspath, dirname, join, isfile
import yaml
import logging
import importlib.util
import sys


def load_module_from_path(path_to_py_file):
    spec = importlib.util.spec_from_file_location("module.name", path_to_py_file)
    mymodule = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = mymodule
    spec.loader.exec_module(mymodule)
    return mymodule


def check_if_containerizeconfig_exists(containerize_config_path):
    assert isfile(
        containerize_config_path
    ), f"{containerize_config_path} does not point to a file."


# def check_if_containerizeconfig_looks_as_expected(containerize_config_path):
#     m_path, m_name = read_containerizeconfig(containerize_config_path)
#     stream = open(containerize_config_path, "r")
#     data = yaml.safe_load(stream)
#     assert "model_path_relative" in data.keys()
#     assert "model_class_name" in data.keys()


def check_containerizeconfig(containerize_config_path):
    check_if_containerizeconfig_exists(containerize_config_path)
    # check_if_containerizeconfig_looks_as_expected(containerize_config_path)


def read_containerizeconfig(containerize_config_path):
    stream = open(containerize_config_path, "r")
    data = yaml.safe_load(stream)
    model_path_relative = data["model_path_relative"]
    model_path_abs = join(dirname(containerize_config_path), model_path_relative)
    model_class_name = data["model_class_name"]

    return model_path_abs, model_class_name


def get_path_of_file_containing_this_line():
    return abspath(inspect.getsourcefile(lambda: 0))


def get_containerizeconfig_path_primary():
    path_of_file_containing_this_line = get_path_of_file_containing_this_line()
    grandparent_folder = dirname(dirname(path_of_file_containing_this_line))
    containerize_config_path = join(grandparent_folder, "containerizeconfig.yaml")
    return containerize_config_path


def get_containerizeconfig_path_dummy():
    path_of_file_containing_this_line = get_path_of_file_containing_this_line()
    parent_folder = dirname(path_of_file_containing_this_line)
    dummy_cconfig_path = join(parent_folder, "dummy_containerizeconfig.yaml")
    return dummy_cconfig_path


def load_primary_model_path_and_name():
    cc_primary = get_containerizeconfig_path_primary()
    check_containerizeconfig(cc_primary)
    model_path_abs, model_class_name = read_containerizeconfig(cc_primary)
    print("primary model loaded")
    return model_path_abs, model_class_name


def load_dummy_model_path_and_name():
    cc_dummy = get_containerizeconfig_path_dummy()
    check_containerizeconfig(cc_dummy)
    model_path_abs, model_class_name = read_containerizeconfig(cc_dummy)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!! dummy model loaded !!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return model_path_abs, model_class_name


def find_model_path_and_name():
    try:
        m_path_abs, m_name = load_primary_model_path_and_name()
    except Exception as e:
        print("Could not load primary model")
        print(e.__repr__())
        m_path_abs, m_name = load_dummy_model_path_and_name()

    return m_path_abs, m_name


def get_custom_members_from_class(c):
    custom_members = [
        member for member in inspect.getmembers(c) if member[0][:2] != "__"
    ]
    return custom_members


def check_if_model_has_at_least_all_memberfunctions_that_the_minimal_containerizable_model_has(
    model_class,
):
    from containerize_my_ml.minimal_containerizable_model import containerizable_model

    containerizable_members = get_custom_members_from_class(containerizable_model)
    containerizable_m_names = [m[0] for m in containerizable_members]
    model_class_members = get_custom_members_from_class(model_class)
    mc_names = [m[0] for m in model_class_members]

    for n in containerizable_m_names:
        assert (
            n in mc_names
        ), f"Expecting the functions {containerizable_m_names} in the loaded model"


def check_predict_arg(model_class):
    fas = inspect.getfullargspec(model_class.__dict__["predict"])
    assert fas.args[0] == "self"
    assert len(fas.args) == 2, f"Only one argument expexted. Got {len(fas.args)-1}."
    arg_name = fas.args[1]
    assert (
        arg_name in fas.annotations
    ), f"Expecting type annotations for the argument for predict: {arg_name}"


def check_set_context_arg(model_class):
    fas = inspect.getfullargspec(model_class.__dict__["set_context"])
    assert fas.args[0] == "self"
    assert len(fas.args) == 2, f"Only one argument expexted. Got {len(fas.args)-1}."
    arg_name = fas.args[1]
    assert (
        arg_name in fas.annotations
    ), f"Expecting type annotations for the argument for predict: {arg_name}"


def check_if_model_class_looks_as_expected(model_class):
    check_if_model_has_at_least_all_memberfunctions_that_the_minimal_containerizable_model_has(
        model_class
    )
    check_predict_arg(model_class)
    check_set_context_arg(model_class)


def find_and_load_model():
    m_path_abs, m_name = find_model_path_and_name()
    model_module = load_module_from_path(m_path_abs)
    model_class = getattr(model_module, m_name)
    check_if_model_class_looks_as_expected(model_class)
    return model_class


def inspect_model_instance(model_instance):
    pred_fas = inspect.getfullargspec(model_instance.predict)
    pred_arg_name = pred_fas.args[1]
    pred_arg_type = pred_fas.annotations[pred_arg_name]

    setc_fas = inspect.getfullargspec(model_instance.set_context)
    setc_arg_name = setc_fas.args[1]
    setc_arg_type = setc_fas.annotations[setc_arg_name]

    model_info = {
        "pred_arg_name": pred_arg_name,
        "pred_arg_type": pred_arg_type,
        "setc_arg_name": setc_arg_name,
        "setc_arg_type": setc_arg_type,
    }

    return model_info


# mc = find_and_load_model()

# m = mc()
# print(m.predict([1, 2, 3, 4]))
