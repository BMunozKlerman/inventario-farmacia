import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from sevencs.agent import (  # noqa: E402
    AgentNotAvailable,
    AgentProfile,
    build_invocation,
    load_registry,
    select_profile,
)

ROOT = Path("/repo")

CODEX = AgentProfile(
    name="codex",
    command="codex",
    exec_args=["exec", "--ephemeral", "-C", "{root}"],
    prompt_mode="stdin",
    stdin_arg="-",
    image_mode="flag",
    image_arg=["-i", "{image}"],
    login_check=["login", "status"],
)

CLAUDE = AgentProfile(
    name="claude",
    command="claude",
    exec_args=["-p", "--add-dir", "{root}"],
    prompt_mode="stdin",
    image_mode="prompt_paths",
)

GEMINI = AgentProfile(
    name="gemini",
    command="gemini",
    exec_args=["-p"],
    prompt_mode="arg",
    image_mode="prompt_paths",
)

REGISTRY = {"detection_order": ["codex", "claude", "gemini"],
            "agents": {"codex": CODEX, "claude": CLAUDE, "gemini": GEMINI}}


def which_for(*available):
    installed = {name: "/usr/local/bin/" + name for name in available}
    return lambda command: installed.get(Path(command).name)


class SelectProfileTest(unittest.TestCase):
    def test_uses_the_first_installed_agent_in_detection_order(self):
        profile, executable = select_profile(REGISTRY, env={}, which=which_for("claude", "gemini"))
        self.assertEqual("claude", profile.name)
        self.assertEqual("/usr/local/bin/claude", executable)

    def test_sevencs_agent_overrides_detection_order(self):
        profile, _ = select_profile(
            REGISTRY, env={"SEVENCS_AGENT": "gemini"}, which=which_for("codex", "gemini")
        )
        self.assertEqual("gemini", profile.name)

    def test_sevencs_agent_command_replaces_the_executable(self):
        _, executable = select_profile(
            REGISTRY,
            env={"SEVENCS_AGENT": "codex", "SEVENCS_AGENT_COMMAND": "/opt/mi-codex"},
            which=which_for(),
        )
        self.assertEqual("/opt/mi-codex", executable)

    def test_raises_when_no_configured_agent_is_installed(self):
        with self.assertRaises(AgentNotAvailable) as raised:
            select_profile(REGISTRY, env={}, which=which_for())
        message = str(raised.exception)
        self.assertIn("codex", message)
        self.assertIn("SEVENCS_AGENT", message)
        self.assertIn("config/agents.json", message)

    def test_raises_when_the_requested_agent_is_unknown(self):
        with self.assertRaises(AgentNotAvailable) as raised:
            select_profile(REGISTRY, env={"SEVENCS_AGENT": "inexistente"}, which=which_for("codex"))
        self.assertIn("inexistente", str(raised.exception))

    def test_raises_when_the_requested_agent_is_known_but_missing(self):
        with self.assertRaises(AgentNotAvailable):
            select_profile(REGISTRY, env={"SEVENCS_AGENT": "codex"}, which=which_for("claude"))


class BuildInvocationTest(unittest.TestCase):
    def test_expands_root_and_sends_the_prompt_through_stdin(self):
        invocation = build_invocation(CODEX, "/usr/local/bin/codex", "haz algo", ROOT)
        self.assertEqual(
            ["/usr/local/bin/codex", "exec", "--ephemeral", "-C", "/repo", "-"], invocation.argv
        )
        self.assertEqual("haz algo", invocation.stdin)

    def test_repeats_the_image_flag_for_each_image(self):
        invocation = build_invocation(
            CODEX,
            "codex",
            "lee",
            ROOT,
            images=[ROOT / "evidence/p01.png", ROOT / "evidence/p02.png"],
        )
        self.assertEqual(
            ["codex", "exec", "--ephemeral", "-C", "/repo",
             "-i", "/repo/evidence/p01.png", "-i", "/repo/evidence/p02.png", "-"],
            invocation.argv,
        )
        self.assertEqual("lee", invocation.stdin)

    def test_appends_relative_image_paths_to_the_prompt_when_there_is_no_image_flag(self):
        invocation = build_invocation(
            CLAUDE, "claude", "lee", ROOT, images=[ROOT / "evidence/p01.png"]
        )
        self.assertEqual(["claude", "-p", "--add-dir", "/repo"], invocation.argv)
        self.assertIn("evidence/p01.png", invocation.stdin)
        self.assertTrue(invocation.stdin.startswith("lee"))

    def test_passes_the_prompt_as_the_last_argument_in_arg_mode(self):
        invocation = build_invocation(GEMINI, "gemini", "haz algo", ROOT)
        self.assertEqual(["gemini", "-p", "haz algo"], invocation.argv)
        self.assertIsNone(invocation.stdin)

    def test_omits_the_stdin_separator_when_the_profile_does_not_declare_one(self):
        invocation = build_invocation(CLAUDE, "claude", "haz algo", ROOT)
        self.assertNotIn("-", invocation.argv)


class LoadRegistryTest(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry(
            Path(__file__).resolve().parents[1] / "config" / "agents.json"
        )

    def test_reads_the_detection_order_and_every_declared_agent(self):
        self.assertEqual(["codex", "claude", "gemini"], self.registry["detection_order"])
        for name in self.registry["detection_order"]:
            self.assertIn(name, self.registry["agents"])

    def test_no_autodetected_profile_bypasses_the_permission_system(self):
        for name in self.registry["detection_order"]:
            self.assertNotIn("bypassPermissions", self.registry["agents"][name].exec_args)
            self.assertNotIn(
                "--dangerously-skip-permissions", self.registry["agents"][name].exec_args
            )

    def test_the_unattended_profile_is_opt_in_and_never_autodetected(self):
        self.assertIn("claude-unattended", self.registry["agents"])
        self.assertNotIn("claude-unattended", self.registry["detection_order"])

    def test_only_codex_declares_a_login_check(self):
        self.assertEqual(["login", "status"], self.registry["agents"]["codex"].login_check)
        self.assertIsNone(self.registry["agents"]["claude"].login_check)


if __name__ == "__main__":
    unittest.main()
