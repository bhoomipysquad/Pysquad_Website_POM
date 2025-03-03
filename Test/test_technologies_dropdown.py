from Pages.Technologies_dropdown import Technologies_Dropdown


class Test_Technologies_dropdown:
    def test_technologies_dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.td = Technologies_Dropdown(self.driver)

        self.td.to_open_python_menu()
        self.td.to_open_django_menu()
        self.td.to_open_flutter_menu()
        self.td.to_open_fast_api_menu()
        self.td.to_open_react_js_menu()