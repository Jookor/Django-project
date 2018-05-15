from django import template

register = template.Library()

#@register.filter(name='cut')
def scut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
#Eka parametri määrittää sen millä functio kutsutaan ja seuraava parametri on itse functio
register.filter('leikkaa',scut)
