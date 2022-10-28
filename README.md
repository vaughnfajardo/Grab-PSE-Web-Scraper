# GrabPSE

October 2022 Update: The program has to be updated to reflect changes in the website. 

GrabPSE runs a Python Script that scrapes data off Investagrams.com and saves essential price-based data of Philippine Stock Exchange (PSE) listed companies locally in a comma separated value (CSV) file for personal consumption ONLY. 

# Getting Started
Prerequisites
> * BeautifulSoup
>>`pip3 install beautifulsoup`
> * Pandas
>>`pip3 install pandas`



# Usage
Upon the execution of the GrabPSE.py script, a prompt is given asking for the Philippine Stock Exchange listed company's stock ticker. 



After receiving an appropriate response, a comma separated value file containing the price data of a stock will exported.  Data below is from DITO CME Holdings Corporation ($DITO) covering 3 days of trading.

|     | Date       | Last Price |     Change    |   %Change | Open | Low| High| Volume| Net Foreign|
| --- |:----------:| :--------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| 1   | 2020-11-24 |    6.25    | -0.07          | -1.11% | 6.34 | 6.21 | 6.35 | 21.36M | 117.69K |
| 2   | 2020-11-23 |    6.32    | -0.08       | -1.25% | 6.40 | 6.27 | 6.47 | 26.17M | 3.11M |
| 3   | 2020-11-20 |    6.40    |  0.01    | 0.16% | 6.38 | 6.21 | 6.45 | 35.16M | 315.95K|


# Run Locally
* Run this command `git clone https://github.com/vaughnfajardo/GrabPSE`
* Proceed to the repository's folder `cd GrabPSE`
* Run the Python Script `python3 GrabPSE.py`

# License
Distributed under the MIT License. See `LICENSE` for more information.

# Contact
Vaughn Fajardo – @vaughnfajardo_ – vaughnnephifajardo@gmail.com


https://github.com/vaughnfajardo/GrabPSE

# Acknowledgements
Special thanks to Investagrams.com for the data




