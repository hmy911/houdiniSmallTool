import os,sys,re

def selectGeometryToObjLevel(fxNode):
    fxNodeName = fxNode.name()
    # print fxNodeName
    fxNodeFullpath = fxNode.path()
    print (type(fxNodeName) ,fxNodeName)
    fx1 = hou.node('/obj').createNode('geo','%s' % fxNodeName)
    fx2 = fx1.createNode('object_merge')
    fx2.parm('objpath1').set(fxNodeFullpath)
    fx1.setColor(hou.Color((0,0.5,0)))
    fx2.setColor(hou.Color((0,0.5,0)))

fxNodes = hou.selectedNodes()
for each in fxNodes:
    selectGeometryToObjLevel(each)

