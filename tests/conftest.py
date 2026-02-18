import pytest
import threading
import http.server
import socketserver
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# ----------------------------
# Constants for the server
# ----------------------------
BASE_URL = "http://localhost:8000/index.html"
PORT = 8000
DIRECTORY = "app/static"


# ----------------------------
# 1️⃣ Run server in background thread
# ----------------------------
@pytest.fixture(scope="session", autouse=True)
def start_server():
    handler = http.server.SimpleHTTPRequestHandler

    def run_server():
        # Open directory and start server
        import os

        os.chdir(DIRECTORY)
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            httpd.serve_forever()

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    # take some time for the server to start
    import time

    time.sleep(0.5)

    yield  # the server will keep running in the background until all tests are done,
    # then the daemon thread will exit automatically


# ----------------------------
# 2️⃣ Browser options, command line args, use like:
# pytest --browser=chrome (default), or --browser=firefox, or --browser=edge
# ----------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome, firefox, or edge",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


# ----------------------------
# 3️⃣ Selenium WebDriver fixture
# ----------------------------
@pytest.fixture(scope="session")
def driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.quit()


# ----------------------------
# 4️⃣ Open page for each test
# ----------------------------
@pytest.fixture
def page(driver):
    driver.get(BASE_URL)
    yield driver


# ----------------------------
# 5️⃣ Page Object. We create an instance of MainPage for each test, and it uses the 'page' fixture.
# ----------------------------
@pytest.fixture
def main_page(page):
    return MainPage(page)
