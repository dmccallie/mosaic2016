from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/mosaic2016')
def mosaic2016():
	return render_template('index.html')

@app.route('/generate')
def generate():
	tiles = generateTiles()
	return render_template('generate.html', tileList = tiles)

def generateTiles():
	#test generation via templates
	# shoot for 9x9 at 64x64 tiles

	tileList = []
	img1 = "https://davidmccallie.s3.amazonaws.com/CRW_4779-sized.jpg"
	img2 = "/static/CRW_6843.jpg"
	tileEdge = 64

	for row in range(0,9):
		for col in range(0,9):
			aTile = {}
			aTile['row'] = row
			aTile['col'] = col
			aTile['y'] = row*tileEdge
			aTile['x'] = col*tileEdge
			aTile['frontImg'] = img1
			aTile['backImg'] = img2
			tileList.append(aTile)
	return tileList

if __name__ == '__main__':
	app.debug = True
	app.run()

