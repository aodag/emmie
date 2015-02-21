# -*- coding:utf-8 -*-
import os
from webassets import Bundle, Environment

here = os.path.dirname(__file__)

all_css = Bundle(
    "bootstrap-3.3.2/css/bootstrap.min.css",
)

all_js = Bundle(
    "jquery-1.11.2.min.js",
    "bootstrap-3.3.2/js/bootstrap.min.js",
)

assets = Environment(
    directory=os.path.join(here, "static"),
    url="static",
)
assets.register("all_css", all_css)
assets.register("all_js", all_js)