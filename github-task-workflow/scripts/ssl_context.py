#!/usr/bin/env python3
"""SSL Context helper for macOS/ServBay Python certificate issues."""

import ssl
import os
import certifi


def create_ssl_context():
    """Create an SSL context that uses certifi certificates.
    
    This fixes SSL certificate verification issues on macOS with 
    Python installations like ServBay that don't use system certificates.
    """
    context = ssl.create_default_context(cafile=certifi.where())
    return context


def patch_urllib():
    """Monkey-patch urllib to use certifi certificates."""
    import urllib.request
    
    original_urlopen = urllib.request.urlopen
    
    def patched_urlopen(url, data=None, timeout=None, *args, **kwargs):
        if 'context' not in kwargs:
            kwargs['context'] = create_ssl_context()
        return original_urlopen(url, data, timeout, *args, **kwargs)
    
    urllib.request.urlopen = patched_urlopen
