from project_tests.utils.allure import step


class SignUpForm:
    @step
    def fill_name(self, first_name, surname):
        return self

    @step
    def fill_email(self, value):
        return self

    @step
    def fill_password(self, value):
        return self

    @step
    def submit(self):
        return self
