#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 5th 4:26 2026

@author: Kumar
"""

# Simple Linear Regression by Kumar

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def main():
    generate_html()

def generate_html():
    template = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Linear Regression Chart</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 24px; background-color: #f5f7fb; color: #222; }
            .chart-container { max-width: 900px; margin: 0 auto; background: #fff; border-radius: 12px; padding: 24px; box-shadow: 0 18px 40px rgba(0,0,0,.08); }
            canvas { max-width: 100%; }
            .note { font-size: 0.95rem; margin-top: 8px; color: #555; }
        </style>
    </head>
    <body>
        <div class="chart-container">
            <h1>Salary vs Years of Experience</h1>
        </div>
        <BR>Hello SLR</BR>
    </body>"""

    print (template)

if __name__ == '__main__':
    main()