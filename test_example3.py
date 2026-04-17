def test_fail(page: Page):
    page.goto("https://www.naver.com/")
    assert "google" in page.url