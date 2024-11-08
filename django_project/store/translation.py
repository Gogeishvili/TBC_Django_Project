from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'title')

translator.register(Product, NewsTranslationOptions)