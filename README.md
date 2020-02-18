[![Build Status](https://travis-ci.org/matplotlib/mpl-finance.svg?branch=master)](https://travis-ci.org/matplotlib/mpl-finance)

# New Version
## This package is being deprecated in 2020.  Please go here for the new version: https://github.com/matplotlib/mplfinance

To understand somewhat of the history and where we are going with this package, please see the rest of this README below, as well as the README for the new package.

<br><br><br><br>

## Introduction
My name is Daniel Goldfarb.  Last month (November 2019) I became the maintainer of `matplotlib/mpl-finance`.  This module consists of code extracted from the deprecated `matplotlib.finance` module along with a few examples of usage.  The code has been mostly un-maintained for the past three years.

## Purpose
It's good to have a single statement of purpose, to guide development.  The original documention says `matplotlib.finance` is a set of functions "*for collecting, analyzing and plotting financial data.*"  --- I disagree with the "*for collecting*" part: **&nbsp;&nbsp; `mplfinance` is part of `matplotlib`.**  &nbsp;&nbsp;Therefore, I would say **the primary purpose of mplfinance is the visualization of financial data.**  However, since analyzing financial data often involves visualization (for example moving averages, oscillators, bollinger bands, etc.) let's say this **also includes analyzing financial data** (at least to the extent that such analysis involves visualization).  Putting this into a single statement to guide development going forward:

---
**The `mplfinance` package provides utilities for the visualization, and visual analysis, of financial data**

---

Let's leave the collection and acquistion of financial data to other packages.  We will focus on visualization, and visual analysis, while other packages can focus on various ways of acquiring the data.  That said, we can certainly provide APIs for interfacing with packages that acquire financial data, in order to more easily and directly visualize and analyze that data.

For more information, please see the following links:

- **[The New API](https://github.com/matplotlib/mplfinance#newapi)**
- **[Latest Release Info](https://github.com/matplotlib/mplfinance#release)**
- **[Some Background History About This Package](https://github.com/matplotlib/mplfinance#history)**
- **[Old API Availability](https://github.com/matplotlib/mplfinance#oldapi)**
- **[README](https://github.com/matplotlib/mplfinance/blob/master/README.md)**

