def test_amazon_title(driver):
    driver.get("https://www.amazon.com")
    assert "Amazon" in driver.title
