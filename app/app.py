import webview

class BrowserApi:
    def __init__(self):
        self.window = None

    def strAppend(self):
        self.window.evaluate_js(
            r"""
            var add_elem = document.createElement('p');
            add_elem.textContent = 'Hello world!';
            document.getElementById("append_area").appendChild(add_elem);
            """
            )

def threadFunction(window):
    print(window)

def main():
    with open("app/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    BA = BrowserApi()
    #apiクラスにwindowを渡しておくことで後から利用しやすくする
    BA.window = webview.create_window(title   = "Test App",
                                       html   = html,
                                       js_api = BA,
                                       width  = 1440,
                                       height = 900)

    webview.start(threadFunction, BA.window, debug=True)

if __name__ == "__main__":
    main()
