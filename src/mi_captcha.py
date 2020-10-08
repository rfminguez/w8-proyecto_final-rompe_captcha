from captcha.image import ImageCaptcha
import string
import random


class Captcha:
    def __init__(self, n_characters = 4, output_dir = "./"):
        self.n_characters = n_characters
        self.output_dir = output_dir
        self.image = ImageCaptcha()
        self.available_characters = self.generate_available_characters()
        self.data = self.generate_random_data()

    def generate_available_characters(self):
        '''
        Devuelve una cadena con todas las letras mayúsculas y números del 1 al 9.
        '''
        return string.ascii_uppercase + string.digits

    def generate_random_data(self):
        try:
            return "".join([random.choice(self.available_characters) for i in range(self.n_characters)])
        except Exception as e:
            print(f"Problema generando caracteres aleatorios: {e}")

    def generate_filename(self):
        return self.output_dir + self.data + ".png"

    def save(self):
        try:
            self.image.generate(self.data)
            self.image.write(self.data, self.generate_filename())
        except Exception as e:
            print(f"Problema guardando la imagen: {e}")
