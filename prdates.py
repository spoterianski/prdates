#!/usr/bin/env python
# coding: utf-8
# 2013 by Sergey Poterianski
#
import argparse
import re
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class PrintDates:
	"""
	PrintDates - this is small tool for printing string yyyymmdd between two dates
	"""
	def __init__(self):
		self.rx_date = re.compile('(?P<year>\d{4})-{,1}(?P<month>\d{2})-{,1}(?P<day>\d{2})')
		self.delta_day = timedelta(days = 1)
		self.delta_week = timedelta(days = 7)
		self.delta_fdays6 = timedelta(days = 6)
		

	def Print(self, mode, begin, end):
		match_begin = self.rx_date.match(begin)
		match_end = self.rx_date.match(end)
		if match_begin is None or match_end is None:
			return 1

		bday = date(int(match_begin.group('year')),\
					int(match_begin.group('month')),\
					int(match_begin.group('day')))

		eday = date(int(match_end.group('year')),\
					int(match_end.group('month')),\
					int(match_end.group('day')))

		
		if mode == 'd':
			# print day
			day = bday
			while day <= eday:
				print day.strftime('%Y%m%d')
				day += self.delta_day
		elif mode == 'w':
			# print week range
			day = bday - (self.delta_day * bday.weekday())
			while day <= eday:
				print day.strftime('%Y%m%d') + ' ' + (day + self.delta_fdays6).strftime('%Y%m%d')
				day += self.delta_week
		elif mode == 'm':
			# print month range
			day = bday.replace(day=1)
			while day <= eday:
				print day.strftime('%Y%m%d') + ' ' + (day + relativedelta(months=1) - \
					relativedelta(days=1)).strftime('%Y%m%d')
				day += relativedelta(months=1)
		return 0


if __name__ == '__main__':
	# parce command arguments
	parser = argparse.ArgumentParser(description='PrintDays - this is small'\
		' tool for printing string yyyymmdd between two dates')
	parser.add_argument('-m', '--mode', choices='dwm', help='Print mode: d - day, '\
		'w - week, m - month (default=d)', default='d')
	parser.add_argument('-b', '--begin', help='Begin date', required=True)
	parser.add_argument('-e', '--end', help='End date', required=True)
	args = parser.parse_args()

	# print date ranges
	pdates = PrintDates()
	if pdates.Print(args.mode, args.begin, args.end) != 0:
		parser.print_usage()
	

