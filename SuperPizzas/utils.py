from dotenv import dotenv_values
from typing import Union
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


EnvSettingTypes = (str, bool, int, float, list)
EnvSetting = Union[str, bool, int, float, list]


def get_env_value(env: dict, key: str, default: EnvSetting = None):
    """get & cast a given value from a dictionary, or return the default"""
    if key in env:
        value = env[key]
    else:
        return default

    ExpectedType = type(default)
    assert (
        ExpectedType in EnvSettingTypes
    ), f"Tried to set unsupported environemnt variable {key} to {ExpectedType}"

    def raise_typerror():
        raise TypeError(
            f"Got bad environment variable {key}={value}" f" (expected {ExpectedType})"
        )

    if ExpectedType is str:
        return value
    elif ExpectedType is bool:
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        else:
            raise_typerror()
    elif ExpectedType is int:
        if value.isdigit():
            return int(value)
        else:
            raise_typerror()
    elif ExpectedType is float:
        try:
            return float(value)
        except ValueError:
            raise_typerror()
    elif ExpectedType is list:
        return value.split(",")


def unique_env_settings(env: dict, defaults: dict) -> dict:
    """return all the new valid env settings in a dictionary of settings"""
    existing_settings = {
        setting_name: val
        for setting_name, val in (defaults or env).items()
        if not setting_name.startswith("_") and setting_name.isupper()
    }
    if not defaults:
        return existing_settings

    new_settings = {}
    for setting_name, default_val in existing_settings.items():
        loaded_val = get_env_value(env, setting_name, default_val)

        if loaded_val != default_val:
            new_settings[setting_name] = loaded_val

    return new_settings


def load_env_settings(
    dotenv_path: str = None, env: dict = None, defaults: dict = None
) -> dict:
    """load settings from a dotenv file or os.environ by default"""
    assert not (dotenv_path and env), "Only pass env or dotenv_path, not both"

    env_values = (env or {}).copy()
    defaults = (defaults or {}).copy()
    if dotenv_path:
        env_values = dotenv_values(dotenv_path=dotenv_path)

    return unique_env_settings(env_values, defaults)


# Decorator. Verifies user permissions
def verify_position(allowed_positions):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            initial_request = request
            if hasattr(request, "request"):  # is a CBV
                request = request.request
            try:
                user = request.user
                if not (user.position in allowed_positions):
                    raise PermissionDenied
            except AttributeError:
                messages.error(request, "Para acceder a la página debe iniciar sesión")
                return redirect("inicio")

            return view_method(initial_request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper
