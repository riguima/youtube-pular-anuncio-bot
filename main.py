from youtube_pular_anuncio_bot.browser import Browser

if __name__ == '__main__':
    browser = Browser(headless=False)
    while True:
        try:
            browser.try_skip_ad()
        except KeyboardInterrupt:
            break
