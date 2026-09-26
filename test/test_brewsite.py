from app.brewsite import app, home


def test_home():
    with app.test_request_context("/"):
        response = home()
        assert "Salvador Felix" in response