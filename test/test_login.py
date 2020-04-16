def test_main_login(app):
    app.session.login(username="user1", password="qwe123")
    assert app.assert_helper.assert_login() == "Центр боевого управления"

