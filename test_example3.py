def test_fail(page: Page):
    page.goto("https://playwright.dev/")
    assert "google" in page.url