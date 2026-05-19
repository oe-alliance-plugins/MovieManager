# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext

PluginLanguageDomain = "MovieManager"


def localeInit():
	localedir = resolveFilename(SCOPE_PLUGINS, "Extensions/MovieManager/locale")
	gettext.bindtextdomain(PluginLanguageDomain, localedir)


def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t


def ngettext(singular, plural, n):
	t = gettext.dngettext(PluginLanguageDomain, singular, plural, n)
	if t in (singular, plural):
		t = gettext.ngettext(singular, plural, n)
	return t


localeInit()
language.addCallback(localeInit)

__version__ = "2.0.2"
