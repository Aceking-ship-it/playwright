def test_fail(page: Page):
    page.goto("https://www.daum.net")
    assert "daum" in page.url