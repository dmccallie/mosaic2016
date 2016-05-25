from flask import Flask
from flask import render_template
from flask import jsonify
from flask import Response
from flask import send_file

app = Flask(__name__)

@app.route('/mosaic2016')
def mosaic2016():
	return render_template('index.html')

@app.route('/generate')
def generate():
	tiles, tileEdge, numRows, numCols = generateTiles()
	return render_template('generate.html', tileEdge=tileEdge, tileList = tiles, numRows=numRows, numCols=numCols)

@app.route('/ivankballs')
def ivankballs():
	return render_template('ivank_balls.html')

@app.route('/threecube')
def threecubecanvas():
	return render_template('threecube.html')

@app.route('/threecubecanvas')
def threecube():
	return render_template('threecubecanvas.html')

@app.route('/css3d_periodictable')
def css3d_periodictable():
	return render_template('css3d_periodictable.html')

@app.route('/css3d_images')
def css3d_images():
	return render_template('css3d_images.html')

@app.route('/cardsTween')
def cardsTween():
	return render_template('cardsTween.html')

@app.route('/cardsTweenLite')
def cardsTweenLite():
	return render_template('cardsTweenLite.html')

@app.route('/cardsTweenLite2')
def cardsTweenLite2():
	return render_template('cardsTweenLite2.html')

@app.route('/cardsTweenLoader')
def cardsTweenLoader():
	return render_template('cardsTweenLoader.html')

@app.route('/testUVmanipulation')
def testUVmanipulation():
	return render_template('testUVmanipulation.html')

@app.route('/cardsTweenSlabsUV')
def cardsTweenSlabsUV():
	return render_template('cardsTweenSlabsUV.html')

@app.route('/mosaicOneSide')
def mosaicOneSide():
	return render_template('mosaicOneSide.html')

@app.route('/slabmap', methods = ['GET'])
def get_slabMap():
	#load the slab map and return (it's already JSON)
	mapFile = open("./static/tiles/slabmap.json", 'r')
	resp = Response(mapFile.read(), status=200, mimetype='application/json')
	return(resp)
	#return jsonify(mapFile.read())
	mapFile.close()

@app.route('/imagemap/<imagename>', methods = ['GET'])
def get_imageMap(imagename):
	#load the map of this image's tiles (already in JSON form)
	imageFile = open("/Users/david/Documents/MosaicTemp/smugmug_dump_tiles/" + imagename + ".json", 'r')
	#print("returning ", imageFile.read())
	resp = Response(imageFile.read(), status=200, mimetype='application/json')
	return(resp)
	#return jsonify(mapFile.read())
	imageFile.close()

@app.route('/image/<imagename>', methods = ['GET'])
def get_image(imagename):
	#load the map of this image's tiles (already in JSON form)
	imageFile = open("/Users/david/Documents/MosaicTemp/smugmug_dump_tiles/" + imagename + "-sized.jpg", 'r')
	#print("returning ", imageFile.read())
	return send_file(imageFile, mimetype='image/jpeg')
	

def generateTiles():
	#test generation via templates
	# shoot for 9x9 at 64x64 tiles

	tileList = []
	#img1 = "https://davidmccallie.s3.amazonaws.com/CRW_4779-sized.jpg"
	img1 = "/static/IMG_2516.jpg"
	img2 = "/static/CRW_6843.jpg"
	tileEdge = 32
	numRows = 32
	numCols = 32

	for row in range(0,numRows):
		for col in range(0,numCols):
			aTile = {}
			aTile['row'] = row
			aTile['col'] = col
			aTile['y'] = row*tileEdge
			aTile['x'] = col*tileEdge
			aTile['frontImg'] = img1
			aTile['backImg'] = img2
			tileList.append(aTile)
	return tileList, tileEdge, numRows, numCols


def line(x0, y0, x1, y1):
	"Bresenham's line algorithm (from rosettacode.org)"
	#x0,y0 = starting coord, x1, y1 = end -- make sure they fit!
	#returns list of points (tile coords)
	points = []
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	x, y = x0, y0
	sx = -1 if x0 > x1 else 1
	sy = -1 if y0 > y1 else 1
	if dx > dy:
		err = dx / 2.0
		while x != x1:
			points.append((x,y))
			err -= dy
			if err < 0:
				y += sy
				err += dx
			x += sx
	else:
		err = dy / 2.0
		while y != y1:
			points.append((x,y))
			err -= dx
			if err < 0:
				x += sx
				err += dy
			y += sy        
	points.append((x,y))

if __name__ == '__main__':
	app.debug = True
	app.run()

