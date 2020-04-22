#!/bin/bash

jupyter nbconvert index.ipynb
jupyter nbconvert  ./notebook/*.ipynb
mv ./notebook/*.html ./html
