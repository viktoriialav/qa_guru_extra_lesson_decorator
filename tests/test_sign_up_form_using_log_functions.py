from project_tests.models.apps import app
from project_tests.utils.functions import given_sign_up_form_opened


def test_sign_up():
    given_sign_up_form_opened()
    app.sign_up_form.fill_name('Tom', surname='Smith')
    app.sign_up_form.fill_email('example@gmail.com')
    app.sign_up_form.fill_password('qwerty')
    app.sign_up_form.submit()
    app.dashboard.go_to_profile()


def test_sign_up_2():
    given_sign_up_form_opened()
    (app.sign_up_form
     .fill_name('Tom', surname='Smith')
     .fill_email('example@gmail.com')
     .fill_password('qwerty')
     .submit())
    app.dashboard.go_to_profile()
