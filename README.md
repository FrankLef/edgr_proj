# edgr_proj

<!-- badges: start -->
[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
<!-- badges: end -->

## Deprecated project

> This project is deprecated. The rss feed returned by the SEC give a
status code 403 which means all is good. But eh files are empty.

## Introduction

The template is based on avideo by [Alexander Falk](https://www.youtube.com/watch?v=2Oe9ZqXVGME)
which was done in 2014 and is modified with this coding project.

Download XBRL files from EDGAR. This is done in 2 steps:

* Download the rss feed providing the specs to retrieve the xbrl files.
* Download the xbrl using the specs provided by the rss feed.

The rss files are located at the [SEC](https://www.sec.gov/Archives/edgar/monthly)
and give the url addresses of the xbrl files at EDGAR.

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
