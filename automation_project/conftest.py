import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Lấy kết quả test
    outcome = yield
    report = outcome.get_result()

    # Chỉ xử lý khi test bị fail ở giai đoạn "call"
    if report.when == "call" and report.failed:
        # Lấy đối tượng test (class) và driver
        test_instance = getattr(item, "instance", None)
        driver = getattr(test_instance, "driver", None)

        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
