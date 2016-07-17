# DEVELOPER NOTES

### TODO

- Ada 'ignore_list' is uncomplete (functions.py module, 'load_language' method): single quotes are used to access object variables, but in certain situations, valid code is detected as strings or chars, being deleted. This must be fixed.
- Floating point operation search is EXTREMELY lax: it detects arithmetic operations of any type, not float only. This must be adjusted.
- Test in deep all languages with several examples.

### BUG-TRACKING

### MISCELLANEOUS

