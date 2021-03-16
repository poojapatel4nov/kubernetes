# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 01:58:08 2020

@author: dinepatel
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Welcome..Dinesh!"

if __name__ == "__main__":
    app.run()
    
    