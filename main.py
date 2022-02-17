import webview


class Api:
    def __init__(self):
        self.window = None

    def window_control(self, action, width, height):
        if action == "close":
            self.window.destroy()

        elif action == "restore":
            window.resize(1050, 600)

        elif action == "maximize":     
            window.resize(width, height)

        else:
            window.minimize()

    def NextPage(self, page_name):
        window.load_url(f'./templates/{page_name}')
    
    def shop_info(self, shop_name, address, phone_num, email, website):
        self.shop_name = shop_name; self.address = address; self.phone_num = phone_num
        self.email = email; self.website = website
    
    def get_info(self):
        return {
            "shop_name": self.shop_name, 
            "address": self.address, 
            "phone_num": self.phone_num, 
            "email": self.email, 
            "website": self.website
        }

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        'Smart Billing App', './templates/first_page.html', js_api=api, frameless=True,
        width=1050, height=600, easy_drag=False
    )
    api.window = window
    webview.start(debug=True)
