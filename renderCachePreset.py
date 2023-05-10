
nodes = hou.selectedNodes()
for node in nodes:
    parm_group = node.parmTemplateGroup()
    # parm_group.addParmTemplate(hou.StringParmTemplate('fxshot', 'fxShot',1))
    # parm_group.addParmTemplate(hou.StringParmTemplate('fxname', 'fxName',1))
    # parm_group.addParmTemplate(hou.StringParmTemplate('fxname2', 'fxName2',1))
    # parm_group.addParmTemplate(hou.IntParmTemplate('ver', 'Version', 1))
    parm_group.addParmTemplate(hou.StringParmTemplate('fxshot', 'fxShot',1))
    parm_group.addParmTemplate(hou.StringParmTemplate('fxname', 'fxName',1))    
    parm_group.addParmTemplate(hou.IntParmTemplate('ver', 'ver', 1))
    parm_group.addParmTemplate(hou.IntParmTemplate('wedge', 'Wedge', 1))
    node.setParmTemplateGroup(parm_group)
    node.parm('fxshot').set('shotcode')
    node.parm('fxname').set('$OS')
    # node.parm('fxname2').set('$OS')
    node.parm('ver').set(1)
    node.parm('wedge').set(1)
    nodeType = node.type().name()
    if nodeType == 'filecache::2.0':
        node.parm('basename').set('`chs("fxshot")`/`chs("fxname")`')
        node.parm('basedir').set('$JOB/geo')
        node.parm('version').set(node.parm('ver'))
        node.parm('sopoutput').deleteAllKeyframes()
        node.parm('sopoutput').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
        # node.parm('version').set('`chi("ver")`')        
    if nodeType == 'geometry':
        node.parm('sopoutput').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'filecache':
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'file':
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'filemerge':
        # node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/w`chs("wedge")`_0000.bgeo.sc')
    elif nodeType == 'filemerge::2.0':
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/w`$SLICE`_0000.bgeo.sc')
    elif nodeType == 'ifd':
        node.parm('vm_picture').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.exr')
        #node.parm('vm_deepresolver').set('camera')
        #node.parm('vm_dcmfilename').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`_deep/v`chs("ver")`/$F4.exr')
        node.parm('vm_image_comment').set('@$user $HIPFILE')
    elif nodeType == 'arnold':
        node.parm('ar_picture').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.exr')
    elif nodeType == 'opengl':
        node.parm('picture').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.exr')
        # node.parm('vm_deepresolver').set('camera')
        # node.parm('vm_dcmfilename').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`_deep/v`chs("ver")`/$F4.exr')
        node.parm('vm_image_comment').set('@$user $HIPFILE')
    elif nodeType == 'baketexture::3.0':
        node.parm('vm_uvoutputpicture1').set('$JOB/render/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/`chs("fxname")`_%(CHANNEL)s.%(UDIM)d.rat')
    elif nodeType == 'file':
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'vm_geo_file':
        node.parm('file').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'rop_geometry':
        node.parm('sopoutput').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.bgeo.sc')
    elif nodeType == 'usdexport':
        node.parm('lopoutput').set('$JOB/usd/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/`chs("fxname")`.usd')
    elif nodeType == 'usdimport':
        node.parm('filepath1').set('$JOB/usd/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/`chs("fxname")`.usd')
    elif nodeType == 'alembic':
        node.parm('filename').set('$JOB/geo/`chs("fxshot")`/`chs("fxname")`/v`chs("ver")`/$F4.abc')

fxNodes = hou.selectedNodes()
for each in fxNodes:
    each.setColor(hou.Color((0,0.5,0.5)))
# print("done-------------------------!")

