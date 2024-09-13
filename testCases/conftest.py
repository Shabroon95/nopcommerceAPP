from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):       # this will get the value from hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return browser value to setup staticmethod
    return request.config.getoption("--browser")

#####pytest HTML REPORT
    # Configure metadata for HTML reports if using pytest-html
import pytest

# This hook configures the metadata for pytest-html reports
def pytest_configure(config):
    # If pytest-html plugin is available, configure metadata
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Shabroon'

# This hook allows modifying the environment information in the report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # Remove unwanted environment variables
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Optional hook for customizing the header of the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    # Set the title of the HTML report
    report.title = "NopCommerce Automation Test Report"

# Optional hook to add a custom environment info in the summary
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project Name: nop Commerce", f"Module Name: Customers", f"Tester: Shabroon"])
