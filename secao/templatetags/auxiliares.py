from django import template


register = template.Library()


@register.filter(name='getValor')
def getValor(chave,dicionario):
  
    return dicionario[chave]