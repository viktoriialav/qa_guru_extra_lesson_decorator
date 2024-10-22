from project_tests.models.pages.dashboard import DashBoard
from project_tests.models.pages.sign_up_form import SignUpForm


class ApplicationManager:
    def __init__(self):
        self.dashboard = DashBoard()
        self.sign_up_form = SignUpForm()


app = ApplicationManager()
