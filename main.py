import os
import sys
import webview

def get_html_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'index.html')
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

if __name__ == '__main__':
    window = webview.create_window(
        title='מחולל מסננים מקצועי - Dynamics NAV / Business Central',
        url=get_html_path(),
        width=1050,
        height=820,
        resizable=True
    )
    webview.start()
