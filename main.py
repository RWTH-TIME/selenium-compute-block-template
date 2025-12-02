from scystream.sdk.core import entrypoint

from utils.selenium_utils import create_chrome_driver


@entrypoint()
def exemplary_entrypoint():
    driver = create_chrome_driver()

    try:
        driver.get("http://google.com")
    except Exception as e:
        print(e)
        quit(1)
    finally:
        driver.quit()
