import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"失败截图已保存到 {screenshot_path}")

    driver.quit()

# 记录测试结果，用于截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
