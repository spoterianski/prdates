#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
from datetime import date
from datetime import timedelta


class DayPrinter(object):
	"""
	DayPrinter this is small tool for printing day (yyyymmdd) between to dates
	"""
	def __init__(self):
		self.rxDate = re.compile('(?P<year>\d{4})-{,1}(?P<month>\d{2})-{,1}(?P<day>\d{2})')
		self.delta_d = timedelta(days = 1)
		self.delta_w = timedelta(days = 7)
		self.delta_w2 = timedelta(days = 6)


	def Print(self, mode, begin, end):
		match_begin = self.rxDate.match(begin)
		match_end = self.rxDate.match(end)
		if match_begin is None or match_end is None:
			return 1

		bday = date(int(match_begin.group('year')),\
					int(match_begin.group('month')),\
					int(match_begin.group('day')))

		eday = date(int(match_end.group('year')),\
					int(match_end.group('month')),\
					int(match_end.group('day')))

		
		if mode == 'd':
			day = bday
			while day <= eday:
				print day.strftime('%Y%m%d')
				day += self.delta_d
		
		elif mode == 'w':
			day = bday - (self.delta_d * bday.weekday())
			while day <= eday:
				print day.strftime('%Y%m%d') + ' ' + (day + self.delta_w2).strftime('%Y%m%d')
				day += self.delta_w
		return 0


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Print day between two dates')
	parser.add_argument('-m', '--mode', choices='dwm', help='Print mode: d - day, w - week, m - month (default=d)', default='d')
	parser.add_argument('-b', '--begin', help='Begin date', required=True)
	parser.add_argument('-e', '--end', help='End date', required=True)
	args = parser.parse_args()

	day_printer = DayPrinter()
	if day_printer.Print(args.mode, args.begin, args.end) != 0:
		parser.print_usage()
