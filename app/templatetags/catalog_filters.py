from django import template
import locale
from decimal import Decimal


register = template.Library()
@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'IG_NG.utf8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    value =abs(int(value))   
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=True)

register.simple_tag(takes_context=True)(currency)

