"""Deprecated import support. Auto-generated by import_shims/generate_shims.sh."""
# pylint: disable=redefined-builtin,wrong-import-position,wildcard-import,useless-suppression,line-too-long

from import_shims.warn import warn_deprecated_import

warn_deprecated_import('rss_proxy.urls', 'lms.djangoapps.rss_proxy.urls')

from lms.djangoapps.rss_proxy.urls import *
