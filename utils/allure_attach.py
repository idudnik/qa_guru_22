import allure
import requests


from selene import browser

def bstack_video(session_id):
    from config import config as app_config
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(app_config.userName, app_config.accessKey)
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML
    )


def page_source_xml():
    xml = browser.driver.page_source
    allure.attach(body=xml, name='screen xml dump', attachment_type=allure.attachment_type.XML, extension='.xml')


def screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )
