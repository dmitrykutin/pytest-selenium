import time


def test_open_modal(main_page):
    main_page.goto(main_page.URL)
    main_page.open_modal()
    assert main_page.is_modal_visible()
    main_page.close_modal()
    main_page.scroll_down(500)
    time.sleep(10)
