# prdates.py
### This is small tool for printing string "yyyymmdd" between two dates

In my work I'm often use dates as string "yyyymmdd" and I decided to write a small utility for convenient print a date range in between two dates.

Usage:

```bash
 prdates.py [-b|--begin] [begin date] [-e|--end] [end date] [-m|--mode] [d|w|m]

 -b or --begin - Begin date in YYYYMMDD format
 -e or --end - End date in  YYYYMMDD format
 -m or --mode - Range: d - day, w - week, m - month
```

Examples: 

```bash
./prdates.py -b 20120101 -e 20130201 -m m - print month ranges between 2012.01.01 and 2013.02.01
./prdates.py -b 20120101 -e 20130201 -m w - print week ranges between 2012.01.01 and 2013.02.01
./prdates.py -b 20120101 -e 20130201 -m d - print dates between 2012.01.01 and 2013.02.01

```
2013 by Sergey Poterianski