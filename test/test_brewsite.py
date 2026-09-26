from app.brewsite import app, home


def test_home():
    with app.app_context():
        response = home()
        assert "Salvador Felix" in response