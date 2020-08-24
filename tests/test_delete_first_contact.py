

def test_delete_first_contact(app):
    app.session.login(login='admin', password='secret')
    app.contact.delete()
    app.session.logout()
