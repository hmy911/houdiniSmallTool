import hou

def copyBBOXCENTER():
	selnodes = hou.selectedNodes()
	src = selnodes[0]
	dst = selnodes[1]
	bbbxxx = src.geometry().boundingBox()
	bbbxxx.sizevec()
	bbbxxx.center()
	dst.parm('sizex').set( bbbxxx.sizevec()[0] )
	dst.parm('sizey').set( bbbxxx.sizevec()[1] )
	dst.parm('sizez').set( bbbxxx.sizevec()[2] )
	dst.parm('tx').set( bbbxxx.center()[0] )
	dst.parm('ty').set( bbbxxx.center()[1] )
	dst.parm('tz').set( bbbxxx.center()[2] )

copyBBOXCENTER()
