"""Adaptador de CLI de agente IA: cualquier agente que acepte un prompt y devuelva un exit code."""

import json
import os
import shutil
import subprocess
from pathlib import Path

IMAGE_PROMPT_HEADER = "\n\nImágenes de entrada (léelas desde el workspace):\n"


class AgentNotAvailable(RuntimeError):
    pass


class AgentProfile:
    def __init__(self, name, command, exec_args, prompt_mode="stdin", stdin_arg=None,
                 image_mode="prompt_paths", image_arg=None, login_check=None):
        self.name = name
        self.command = command
        self.exec_args = list(exec_args)
        self.prompt_mode = prompt_mode
        self.stdin_arg = stdin_arg
        self.image_mode = image_mode
        self.image_arg = list(image_arg) if image_arg else []
        self.login_check = list(login_check) if login_check else None


class Invocation:
    def __init__(self, argv, stdin):
        self.argv = argv
        self.stdin = stdin


def load_registry(config_path):
    with open(config_path, encoding="utf-8") as handle:
        document = json.load(handle)
    agents = {name: AgentProfile(name=name, **spec) for name, spec in document["agents"].items()}
    return {"detection_order": list(document["detection_order"]), "agents": agents}


def select_profile(registry, env=None, which=shutil.which):
    env = os.environ if env is None else env
    agents = registry["agents"]
    requested = env.get("SEVENCS_AGENT")
    override = env.get("SEVENCS_AGENT_COMMAND")

    if requested:
        if requested not in agents:
            raise AgentNotAvailable(
                "Agente '{}' desconocido. Declarados en config/agents.json: {}.".format(
                    requested, ", ".join(sorted(agents))
                )
            )
        profile = agents[requested]
        executable = override or which(profile.command)
        if not executable:
            raise AgentNotAvailable(
                "El agente '{}' no está en el PATH. Instálalo o apunta SEVENCS_AGENT_COMMAND "
                "a su ejecutable.".format(requested)
            )
        return profile, executable

    for name in registry["detection_order"]:
        profile = agents[name]
        executable = override or which(profile.command)
        if executable:
            return profile, executable

    raise AgentNotAvailable(
        "No se encontró ningún CLI de agente IA en el PATH. Se buscó: {}. "
        "Instala uno, elige otro con SEVENCS_AGENT=<nombre>, apunta SEVENCS_AGENT_COMMAND a un "
        "ejecutable propio, o agrega tu agente a config/agents.json.".format(
            ", ".join(registry["detection_order"])
        )
    )


def build_invocation(profile, executable, prompt, root, images=()):
    argv = [executable]
    root_text = str(root)
    argv += [argument.replace("{root}", root_text) for argument in profile.exec_args]

    images = list(images)
    if images and profile.image_mode == "flag":
        for image in images:
            argv += [argument.replace("{image}", str(image)) for argument in profile.image_arg]
    elif images:
        prompt += IMAGE_PROMPT_HEADER + "\n".join(
            "- " + _relative_to(image, root) for image in images
        )

    if profile.prompt_mode == "arg":
        return Invocation(argv + [prompt], None)
    if profile.stdin_arg:
        argv.append(profile.stdin_arg)
    return Invocation(argv, prompt)


def run_prompt(profile, executable, prompt, root, images=()):
    invocation = build_invocation(profile, executable, prompt, root, images)
    completed = subprocess.run(
        invocation.argv, input=invocation.stdin, encoding="utf-8", cwd=str(root)
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "{} falló con código {}".format(profile.name, completed.returncode)
        )


def check_login(profile, executable):
    if not profile.login_check:
        return
    completed = subprocess.run(
        [executable] + profile.login_check,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "El agente '{}' no tiene una sesión activa. Ejecuta: {} {}".format(
                profile.name, profile.command, " ".join(profile.login_check)
            )
        )


def _relative_to(path, root):
    try:
        return Path(path).relative_to(root).as_posix()
    except ValueError:
        return Path(path).as_posix()
