import time


def test_open_modal(main_page):
    main_page.goto(main_page.URL)
    main_page.click(main_page.MODAL_OPEN_BTN)
    assert "modal" in main_page.driver.page_source
    time.sleep(10)
