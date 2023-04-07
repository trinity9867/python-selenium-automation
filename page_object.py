class Page:

    def __init__(self):
        self.url = 'www.amazon.com'

        def open(self):
            print('Url opening', self.url)

        def close(self):
            print('Closing the page', self.url)




p = Page()
# p.open_url()
# p.close()


p.open_url()
p.close()


print(p.url)