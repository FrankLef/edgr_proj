# edgr_proj

<!-- badges: start -->
[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
<!-- badges: end -->

## Introduction

EDGAR data extraction

## How to use

The entry point is in `..\src\__main__.py` with a command line that will use
the `dispatch.py` file to dispatch actions required by `__main__.py`.

You just need to be in the project directory

    cd edgr_proj

and use the command

    python src <args> <option>

where `<args>` and `<options>` are the arguments and options defined in
`__main__.py`. You will usually have to change them to suit your needs.

The help on the `<args>` and `<options>` is found as usual by invoking

    python src -h
