# Basic Flask App

This small repo demonstrates a proper file structure for a Flask app. The folders named *static* and *templates* are required.

**Routes** and **static files** are handled correctly in all `src` and `href` attributes in the template files.

The template file `base.html` is used as a shell by the other three HTML templates. This means they insert content into `base.html` according to Jinja2 template rules.

After installing all dependencies, run the app by entering its folder and typing:

`$ python routes.py`
