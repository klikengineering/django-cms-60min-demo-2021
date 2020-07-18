2020.07
-------------------------------------------------------------------------------

- added a new link plugin that allows to select the link type - eg blog article, cms page, external url, etc
- added ability to add html links and iframe to CKEditor
- cms dynamic forms:
    - fixed the email variables representation and validation
    - fixed django success message that was shown on an unrelated page, seemingly on random
    - fixed the form submission success message that could have been invisible for the user, now the page scrolls to it after a POST request
- fixed spellchecker in CKEditor

### Technical

- added a wrapper for [linkit](https://github.com/dreipol/linkit) with djangocms-blog support, located at `backend.plugins.link`
- added backend.site_config example
- added django-sortedm2m for simple sorting M2M models - it's possible with django-admin-sortable2 but the complexity is unreasonable
- added test of pages on the real database that fully rollbacks a divio deployment if any page returns a 5XX code 
- updated docker base image to from 4.16 to 4.17
- fixed django translations
- fixed `<html>`'s tag `lang` attribute, it was empty before
- fixed aldryn-sso email duplication issue on divio database exporta
- disabled the ability of search engines to index the aldryn-sso login page
- dropped sentry config in settings and use the version from aldryn-django
- dropped custom ckeditor toolbar to avoid issues as missing spellchecker

#### Breaking Changes

- updated aldryn-forms from 5th to 6th version that contains a lot of fixes, eg we disabled the original Form plugin

### Documentation

- updated backend.md

2020.06
-------------------------------------------------------------------------------

- added [djangocms-socialshare](https://gitlab.com/what-digital/djangocms-socialshare) - a plugin for customizable rendering of sharing and social links icons
- added [djangocms-algolia](https://gitlab.com/victor.yunenko/djangocms-algolia)
- added [linkit](https://github.com/dreipol/linkit) that must be used for all links from now on
- fixed the `login with divio` feature that used to raise an "email duplicate error" ([divio/aldryn-sso#66](https://github.com/divio/aldryn-sso/issues/66))
- fixed the freezing of page after 5-10 CMS edits
- fixed django-cms (or aldryn-django) local caching issue

### Breaking Changes

- replaced `backend.articles` with djangocms-blog
- moved out `backend.tests.test_pages` into djangocms-helpers 2.2
- moved `backend.plugins.default` to `backend.plugins` for simplification
- deleted `bs4_card_columns`, because it appears that it requires styles and we've haven't seen a request from the client to style it