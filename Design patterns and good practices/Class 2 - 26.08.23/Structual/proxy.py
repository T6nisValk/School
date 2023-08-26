class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display_image(self):
        print(f"Displaying {self.filename}")


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxy_state = None


class ProxyImage(Proxy):
    def display_image(self):
        if self.proxy_state is None:
            self.subject.load_image_from_disk()
            self.proxy_state = 1
        print(f"Display {self.subject.filename}")


proxy_image1 = ProxyImage(Image("SomeImage.jpg"))
proxy_image2 = ProxyImage(Image("SomeOtherImage.jpg"))

proxy_image1.display_image()
proxy_image1.display_image()
proxy_image2.display_image()
proxy_image2.display_image()
proxy_image1.display_image()
