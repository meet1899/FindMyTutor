from factory import Factory, SubFactory
from .forms import H_form


class ProductFormFactory(Factory):
    class Meta:
        model = H_form

    your_email = "123@123.com"
    Request = "I want to hire you"
