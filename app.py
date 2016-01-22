# -*- coding: iso-8859-1 -*-
import pypandoc
import sys  
from flask import *
import argparse

parser = argparse.ArgumentParser(description='This is a tool for creating beautiful Reveal.js presentations from Markdown files.')
parser.add_argument('-i','--input', help='Input file name',required=True)
args = parser.parse_args()

__author__ = 'ethylomat'

reload(sys)  
sys.setdefaultencoding('utf8')



try:
	if args.input:
		input_file = args.input
		pass
	else:
		input_file = "presentation.md"
	pass
except Exception, e:
	raise e


app = Flask(__name__, static_folder="reveal")

@app.route('/')
def presentation():
    slides_html = pypandoc.convert(input_file, 'revealjs')

    return render_template('index.html', slides_html=slides_html)


if __name__ == '__main__':
    app.run(debug=True)

#{{ url_for('css', filename='reveal.css') }}
