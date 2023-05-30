from .base_page import BasePage

#заглушка потому что методы добавили в base_page
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
