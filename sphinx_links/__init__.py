#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
import docutils
from docutils.parsers.rst.roles import set_classes
from .collection import LINKS

SETTING_LINKS = 'links_collection'


class CaseInsensitiveDict(dict):

    """Basic case insensitive dict with strings only keys."""

    proxy = {}

    def __init__(self, data):
        self.proxy = dict((k.lower(), k) for k in data)
        for k in data:
            self[k] = data[k]

    def __contains__(self, k):
        return k.lower() in self.proxy

    def __delitem__(self, k):
        key = self.proxy[k.lower()]
        super(CaseInsensitiveDict, self).__delitem__(key)
        del self.proxy[k.lower()]

    def __getitem__(self, k):
        key = self.proxy[k.lower()]
        return super(CaseInsensitiveDict, self).__getitem__(key)

    def get(self, k, default=None):
        return self[k] if k in self else default

    def __setitem__(self, k, v):
        super(CaseInsensitiveDict, self).__setitem__(k, v)
        self.proxy[k.lower()] = k


def external_links(links={}):
    def role(
        role, rawtext, text,
        lineno, inliner, options={}, content=[]
    ):
        """
        Example:

            See code there :l:`Nginx`.
        """
        merged_links = dict(LINKS.items() + links.items())
        link = CaseInsensitiveDict(merged_links)[text.lower()]
        set_classes(options)
        node = docutils.nodes.reference(
            rawtext,
            docutils.utils.unescape(text),
            refuri=link,
            **options
        )
        return [node], []
    return role


def add_role(app, env, docname):
    links = getattr(env.app.config, SETTING_LINKS, {})
    app.add_role('l', external_links(links))


def setup(app):
    app.add_config_value(SETTING_LINKS, {}, False)
    app.connect('env-before-read-docs', add_role)
