from app.brewsite import hello_world


def test_hello_world():
    assert "Hello World!" in hello_world()