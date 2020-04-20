def test_main_login_313(app):
    app.session.login(username="user1", password="qwe123")
    assert app.assert_authorization.assert_login() == "Центр боевого управления"


def test_home_button_2527(app):
    app.session.login(username="user1", password="qwe123")
    app.session.open_neo()
    app.session.home_button()
    assert app.assert_authorization.assert_login() == "Центр боевого управлениz"


def test_logout_button_2270(app):
    app.session.login(username="user1", password="qwe123")
    app.session.open_neo()
    app.session.logout_button()
    assert app.assert_authorization.assert_logout() == "ВОЙТИ"
