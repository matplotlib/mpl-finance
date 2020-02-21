[![Build Status](https://travis-ci.org/matplotlib/mpl-finance.svg?branch=master)](https://travis-ci.org/matplotlib/mpl-finance)

# This package is deprecated.  Please go here for the new version: https://github.com/matplotlib/mplfinance

---

## To Install:
## [`pip install --upgrade mplfinance`](https://pypi.org/project/mplfinance/)

---

<br><br><br><br>

## Background
My name is Daniel Goldfarb.  In November 2019, I became the maintainer of `matplotlib/mpl-finance`, and immediately began work on a new version of the module, with an all new API.   The old API is still available in the new package, and will likely remain so for several months, at least until we are confident that the new API provides all of the old API's functionality (and more).  **This package is now deprecated.  [Please follow the above links to the new module.](https://github.com/matplotlib/mplfinance)**   (This deprecated package  consisted of code extracted from the deprecated `matplotlib.finance` module along with a few examples of usage.  The code was un-maintained for over three years.)

## Purpose
It's good to have a single statement of purpose, to guide development.  The original documention for the (now twice deprecated) `matplotlib.finance` says that it was a set of functions "*for collecting, analyzing and plotting financial data.*"  --- I disagree with the "*for collecting*" part: **&nbsp;&nbsp; `mplfinance` is part of `matplotlib`.**  &nbsp;&nbsp;Therefore, I would say **the primary purpose of mplfinance is the visualization of financial data.**  However, since analyzing financial data often involves visualization (for example moving averages, oscillators, bollinger bands, etc.) let's say this **also includes analyzing financial data** (at least to the extent that such analysis involves visualization).  Putting this into a single statement to guide development going forward:

---
**The `mplfinance` package provides utilities for the visualization, and visual analysis, of financial data**

---

Let's leave the collection and acquistion of financial data to other packages.  We will focus on visualization, and visual analysis, while other packages can focus on various ways of acquiring the data.  That said, we can certainly provide APIs for interfacing with packages that acquire financial data, in order to more easily and directly visualize and analyze that data.

**For more information, please see the following links:**

- **[`pip install --upgrade mplfinance`](https://pypi.org/project/mplfinance/)**
- **[The New API](https://github.com/matplotlib/mplfinance#newapi)**
- **[Latest Release Info](https://github.com/matplotlib/mplfinance#release)**
- **[Some Background History About This Package](https://github.com/matplotlib/mplfinance#history)**
- **[Old API Availability](https://github.com/matplotlib/mplfinance#oldapi)**
- **[README](https://github.com/matplotlib/mplfinance/blob/master/README.md)**

