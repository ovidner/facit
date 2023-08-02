import nox

nox.options.reuse_existing_virtualenvs = True

PYTHON_VERSIONS = ["3.11", "3.10", "3.9"]
OPENMDAO_VERSIONS = [
    "3.27",
    "3.26",
    "3.25",
]


@nox.session(venv_backend="mamba", python=PYTHON_VERSIONS)
@nox.parametrize("openmdao", OPENMDAO_VERSIONS)
def tests(session, openmdao):
    # FIXME: Now we only use conda to install Python, and let pip do the
    # rest. Should probably use conda for everything.
    session.conda_install(
        # https://github.com/conda-forge/numpy-feedstock/issues/84
        "blas=*=openblas",
        # FIXME: workaround till we replace pygmo with pymoo
        "pygmo",
    )
    session.install(f"openmdao=={openmdao}")
    session.install("-e", ".[test]")
    session.run("pytest", *session.posargs)
