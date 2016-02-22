#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib
import sys
import re

const_url = 'http://www.douyutv.com/directory/all'

def findImgUrl(srcHtml):
	matchRgex = '".+\.jpg"'
	imgre = re.compile(matchRgex)
	imglist = re.findall(imgre, srcHtml)
	x = 0
	for imgurl in imglist:
		imgurl = imgurl[1:-1]
		print(imgurl)
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1


def getHtml(url):
	codeType = sys.getfilesystemencoding()
	page = urllib.urlopen(url)
	html = page.read()
	print(html.decode('utf-8').encode(codeType))
	findImgUrl(html)
	return html

#codeType = sys.getfilesystemencoding()
#html = getHtml(const_url).decode('utf-8').encode(codeType)

#outFile = open('htmlContent.txt', 'w')
#if(outFile != None):
#	outFile.write(html)

#print(html)

#const_url = raw_input('please enter the html that you want catch it:')
#print(const_url)
getHtml(const_url)



