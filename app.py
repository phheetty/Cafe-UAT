#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from config import *
from api import *







if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3515, debug=True, threaded=True)