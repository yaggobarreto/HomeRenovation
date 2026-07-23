from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Paths de https://lucide.dev (licença ISC), viewBox 0 0 24 24
ICONES = {
    'house': '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8" />'
             '<path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6'
             'A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />',
    'hammer': '<path d="m15 12-9.373 9.373a1 1 0 0 1-3.001-3L12 9" />'
              '<path d="m18 15 4-4" />'
              '<path d="m21.5 11.5-1.914-1.914A2 2 0 0 1 19 8.172v-.344a2 2'
              ' 0 0 0-.586-1.414l-1.657-1.657A6 6 0 0 0 12.516 3H9l1.243 '
              '1.243A6 6 0 0 1 12 8.485V10l2 2h1.172a2 2 0 0 1 1.414.586'
              'L18.5 14.5" />',
    'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />'
             '<path d="M16 3.128a4 4 0 0 1 0 7.744" />'
             '<path d="M22 21v-2a4 4 0 0 0-3-3.87" />'
             '<circle cx="9" cy="7" r="4" />',
    'piggy-bank': '<path d="M11 17h3v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-3a'
                  '3.16 3.16 0 0 0 2-2h1a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1h-1'
                  'a5 5 0 0 0-2-4V3a4 4 0 0 0-3.2 1.6l-.3.4H11a6 6 0 0 0-6'
                  ' 6v1a5 5 0 0 0 2 4v3a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1z" />'
                  '<path d="M16 10h.01" />'
                  '<path d="M2 8v1a2 2 0 0 0 2 2h1" />',
    'calendar-check-2': '<path d="M8 2v4" /><path d="M16 2v4" />'
                         '<path d="M21 14V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v'
                         '14a2 2 0 0 0 2 2h8" /><path d="M3 10h18" />'
                         '<path d="m16 20 2 2 4-4" />',
    'bar-chart-3': '<path d="M3 3v16a2 2 0 0 0 2 2h16" />'
                   '<path d="M18 17V9" /><path d="M13 17V5" />'
                   '<path d="M8 17v-3" />',
    'shopping-bag': '<path d="M16 10a4 4 0 0 1-8 0" />'
                    '<path d="M3.103 6.034h17.794" />'
                    '<path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 '
                    '2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2'
                    ' 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z" />',
    'heart': '<path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0'
             'A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2'
             ' 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5" />',
    'arrow-right': '<path d="M5 12h14" /><path d="m12 5 7 7-7 7" />',
    'plus': '<path d="M5 12h14" /><path d="M12 5v14" />',
    'pencil': '<path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a'
              '2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32'
              'a2 2 0 0 0 .83-.497z" /><path d="m15 5 4 4" />',
    'trash-2': '<path d="M10 11v6" /><path d="M14 11v6" />'
               '<path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" />'
               '<path d="M3 6h18" />'
               '<path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />',
    'external-link': '<path d="M15 3h6v6" /><path d="M10 14 21 3" />'
                      '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a'
                      '2 2 0 0 1 2-2h6" />',
    'check-circle-2': '<circle cx="12" cy="12" r="10" />'
                       '<path d="m9 12 2 2 4-4" />',
    'menu': '<path d="M4 5h16" /><path d="M4 12h16" /><path d="M4 19h16" />',
    'leaf': '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 '
            '4.18 2 8 0 5.5-4.78 10-10 10Z" />'
            '<path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12" />',
}


@register.filter
def startswith(texto, prefixo):
    if not prefixo:
        return False
    return str(texto).startswith(prefixo)


@register.simple_tag
def icon(nome, classe='icone'):
    caminho = ICONES.get(nome, '')
    svg = (
        f'<svg class="{classe}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{caminho}</svg>'
    )
    return mark_safe(svg)
