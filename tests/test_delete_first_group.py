import time


def test_delete_first_group(app):
    app.session.login(login='admin', password='secret')
    app.group.delete()
    app.session.logout()
    time.sleep(1)
