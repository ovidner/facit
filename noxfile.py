import nox

nox.options.reuse_existing_virtualenvs = True

PYTHON_VERSIONS = ["3.11", "3.10", "3.9"]
OPENMDAO_VERSIONS = [
    "3.27",
    "3.26",
    "3.25",
]


@nox.session(venv_backend="conda")
@nox.parametrize("python", PYTHON_VERSIONS)
@nox.parametrize("openmdao", OPENMDAO_VERSIONS)
def tests_conda(session, python, openmdao):
    session.conda_install(f"python={python}", f"openmdao={openmdao}")
    session.install(".", "--no-deps")
    # FIXME: actually run tests
    session.run("python", "-c", "import facit")
