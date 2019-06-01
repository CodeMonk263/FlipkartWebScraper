.. FlipkartWebScraper documentation master file, created by
   sphinx-quickstart on Sun Jun  2 01:09:47 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FlipkartWebScraper's documentation!
==============================================

This is the documentation for the Web Scraping project for the SmartCampus Inductions.

Modules that were used
----------------------

1. scrapy
2. pickle
3. CrawlerProcess
4. os
5. sys

Classes that were used (user-defined)
-------------------------------------

1. FlipkartwebscraperItem
2. laptopsSpider

Goals achieved
--------------

1. Can scrapy single html pages by finding specific div tags using css selector
2. Can follow links for websites with pagination such as Flipkart
3. Can also pickle the scraped data
4. Can also read back the pickled data and return as dictionary
5. Can read command line attributes and take input such as name of pickle directory and no of laptops to be scraped


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
