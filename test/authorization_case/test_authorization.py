def test_main_login_313(app):
    app.session.login(username="user1", password="qwe123")
    assert app.assert_authorization.assert_login() == "Центр боевого управления"

