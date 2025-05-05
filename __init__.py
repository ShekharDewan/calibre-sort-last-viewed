license               = 'GPL v3'
copyright             = '2024–25, Guide Version'
docformat             = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

class DatestampAndViewPlugin(InterfaceActionBase):
    name                    = 'Datestamp and View (Guide)'
    description             = 'Sets #lastopened date, then opens book viewer.'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'Guide Version'
    version                 = (3, 0, 9)
    minimum_calibre_version = (5, 0, 0)

    # Point to our GUI logic class
    actual_plugin           = (
        'calibre_plugins.datestamp_view_guide.action:DatestampAndViewAction'
    )

    def is_customizable(self):
        return False
