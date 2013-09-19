"""

    Fixed text column

    Copyright 2006 Red Innovation

    Licensed under GPL.

"""

from __future__ import nested_scopes
__author__ = "Mikko Ohtamaa <mikko@redinnovation.com>"
__docformat__ = 'reStructuredText'

from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from Products.DataGridField.Column import Column

class FixedColumn(Column):
    """ Column with non-changeable text

    Useful with DataGridField.fixed_row property in some use cases.
    """
    security = ClassSecurityInfo()

    def __init__(self, label, col_description=None, default=None,
                 default_method=None, visible=True, required=False):
        """ Create a column

            @param visible Hide column from displaying by setting this to False
        """
        Column.__init__(self, label, col_description=col_description,
                        default=default, default_method=default_method,
                        required=required)
        self.visible = visible

    security.declarePublic('getMacro')
    def getMacro(self):
        """ Return macro used to render this column in view/edit """
        return "datagrid_fixed_cell"


# Initializes class security
InitializeClass(FixedColumn)
