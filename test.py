from pages.mainpage import MainPage


def test_first(get_driver):
    main1 = MainPage(get_driver)
    auth_page = main1.sign_in()
    my_account = auth_page.login("liron@gmail.com", "12345678")
    main1 = my_account.home()
    searchres = main1.search("summer")

