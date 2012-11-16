#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

"""
################################################################################


This file stores globals used in tests and doctests,
just import all variables from here and enjoy.

################################################################################
"""

import ConfigParser
import os
import re
import sys
from copy import deepcopy
from pprint import pprint

from zope.component import adapts, getMultiAdapter, getAdapter, getAdapters
from zope import interface, schema
from zope.interface import implementedBy, providedBy
from zope.interface.verify import verifyObject
from zope.traversing.adapters import DefaultTraversable
import zope
from plone.testing import z2

from Acquisition import aq_inner, aq_parent, aq_self

from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

zope.component.provideAdapter(DefaultTraversable, [None])
cwd = os.path.dirname(__file__)

def get_interfaces(o):
    return [o for o in o.__provides__.interfaces()]

def errprint(msg):
    """Writes 'msg' to stderr and flushes the stream."""
    sys.stderr.write(msg)
    sys.stderr.flush()

def pstriplist(s):
    print '\n'.join([a.rstrip() for a in s.split('\n') if a.strip()])

class Request(zope.publisher.browser.TestRequest):
    def __setitem__(self, name, value):
        self._environ[name] = value
# alias
TestRequest = Request
def make_request(url='http://nohost/@@myview',form=None, *args,  **kwargs):
    r = Request(environ = {'SERVER_URL': url, 'ACTUAL_URL': url}, form=form, *args, **kwargs)
    zope.interface.alsoProvides(r, zope.annotation.interfaces.IAttributeAnnotatable)
    return r

from collective.datatablesviews.testing import (
    Browser,
    PLONE_MANAGER_ID,
    PLONE_MANAGER_NAME,
    PLONE_MANAGER_PASSWORD,
    SITE_OWNER_NAME,
    SITE_OWNER_PASSWORD,
    TEST_USER_ID,
    TEST_USER_NAME,
    TEST_USER_ROLES,
)


# vim:set et sts=4 ts=4 tw=80:
