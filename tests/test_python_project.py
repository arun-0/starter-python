from python_project import greeting


def test_greeting() -> None:
    assert greeting() == "Hello from python-project!"
