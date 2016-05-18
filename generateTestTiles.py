from PIL import Image, ImageFont, ImageDraw

tileSize = 256,256
slabSize = 8192,8192  #16x16 tiles
tilesPerSlabEdge = slabSize[0] / tileSize[0]

outputDirectory = "./static/tiles/"
font = ImageFont.truetype("./static/DroidSans-Bold.ttf", size=40)

textSize = font.getsize("1234")
ulc = (tileSize[0]/2 - textSize[0]/2, tileSize[0]/2 - textSize[1]/2 - 8)
boxUlc = (ulc[0]-2, ulc[1]-1)
box = [ boxUlc,
	   (boxUlc[0]+textSize[0]+5, boxUlc[1]),
	   (boxUlc[0]+textSize[0]+5, boxUlc[1]+textSize[1]+10),
	   (boxUlc[0], boxUlc[1]+textSize[1]+10),
	   (boxUlc[0], boxUlc[1]) ]

outerBox = [(0,0),
			(tileSize[0]-1,0),
			(tileSize[0]-1, tileSize[1]-1),
			(0, tileSize[1]-1),
			(0,0)]


slabCount = 0
slabItem = 0
numRows = 70
numCols = 70

curSlabR = Image.new("RGB", slabSize, "white")
curSlabB = Image.new("RGB", slabSize, "white")
curSlabG = Image.new("RGB", slabSize, "white")

for row in range(0,numRows):
	for col in range(0,numCols):
	
		tileR = Image.new("RGB", tileSize, "red")
		tileB = Image.new("RGB", tileSize, "black")
		tileG = Image.new("RGB", tileSize, "green")		
		
		drawR = ImageDraw.Draw(tileR)
		drawB = ImageDraw.Draw(tileB)
		drawG = ImageDraw.Draw(tileG)

		tileNum = row*numCols + col
		label = str(tileNum)

		textSize = font.getsize(label)
		ulc = (tileSize[0]/2 - textSize[0]/2, tileSize[0]/2 - textSize[1]/2 - 8)
		drawR.text(ulc, label, font=font, fill="white")
		drawR.line(box, "white", width=3)
		drawR.line(outerBox, "white", width=1)

		drawB.text(ulc, label, font=font, fill="white")
		drawB.line(box, "white", width=3)
		drawB.line(outerBox, "white", width=1)

		drawG.text(ulc, label, font=font, fill="white")
		drawG.line(box, "white", width=3)
		drawG.line(outerBox, "white", width=1)

		#tileR.save(outputDirectory + "tile-red-" + label + ".png")
		#tileB.save(outputDirectory + "tile-black-" + label + ".png")

		#add to curSlab
		slabCol = slabItem % tilesPerSlabEdge
		slabRow = slabItem // tilesPerSlabEdge
		corner = (slabCol*tileSize[0], slabRow*tileSize[1])
		curSlabR.paste(tileR, corner)
		curSlabB.paste(tileB, corner)
		curSlabG.paste(tileG, corner)
		slabItem = slabItem + 1
		
		if (slabItem == tilesPerSlabEdge*tilesPerSlabEdge):
			curSlabR.save(outputDirectory + "slab-red-"   + str(slabCount) + ".png")
			curSlabB.save(outputDirectory + "slab-black-" + str(slabCount) + ".png")		
			curSlabG.save(outputDirectory + "slab-green-" + str(slabCount) + ".png")

			slabCount = slabCount + 1
			slabItem = 0
			curSlabR = Image.new("RGB", slabSize, "white")
			curSlabB = Image.new("RGB", slabSize, "white")
			curSlabG = Image.new("RGB", slabSize, "white")

if (slabItem > 0):
	curSlabR.save(outputDirectory + "slab-red-"   + str(slabCount) + ".png")
	curSlabB.save(outputDirectory + "slab-black-" + str(slabCount) + ".png")	
	curSlabG.save(outputDirectory + "slab-green-" + str(slabCount) + ".png")

