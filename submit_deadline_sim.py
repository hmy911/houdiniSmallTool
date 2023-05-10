#!/usr/bin/python
import os, sys, re
import json
import optparse
import subprocess
import shutil

def createDir(createPath):
    if not os.path.exists(createPath):
        print('os.makedirs(%s)'% createPath)
        os.makedirs(createPath)

def job_info(info_txt):
    job_info_file = r'{}\job_info.job'.format(os.getenv('TEMP'))
    with open(job_info_file, 'w') as job_file:
        job_file.write(info_txt)
    return job_info_file

def plugin_info(info_txt):
    plugin_info_file = r'{}\plugin_info.job'.format(os.getenv('TEMP'))
    with open(plugin_info_file, 'w') as job_file:
        job_file.write(info_txt)
    return plugin_info_file


def submit_to_deadline(job_info_txt, plugin_info_txt):
    # Change deadline exe root
    deadline_cmd = r"C:\Program Files\Thinkbox\Deadline10\bin\deadlinecommand.exe"
    job_file = job_info(job_info_txt)
    info_file = plugin_info(plugin_info_txt)
    command = '{deadline_cmd} "{job_file}" "{info_file}"'.format(**vars())
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    lines_iterator = iter(process.stdout.readline, b"")
    for line in lines_iterator:
        print(line)
        sys.stdout.flush()

def GetInfoTxtHoudini(batchname, name, fullnamepath, outputDriver, framerange, pool, priority, version, chunkSize, machineLimit, comment):
    job_info_txt = ("BatchName=%s\nComment=%s\nChunkSize=%s\nFrames=%s\nMachineLimit=%s\nGroup=houdini_19\nName=%s\nOverrideTaskExtraInfoNames=False\nPlugin=Houdini\nPool=%s\nPriority=%s\nSecondaryPool=all\nUserName=%s\n") % (batchname, comment, chunkSize, framerange, machineLimit,name,pool,priority,os.environ.get("USERNAME"))
    # executable = cmd.split()[0]
    # arg = cmd.replace(executable,'')
    # fullnamepath = 
    # outputDriver = 
    plugin_info_txt = "SceneFile=%s\nOutputDriver=%s\nShell=default\nShellExecute=False\nSingleFramesOnly=False\nVersion=%s\n"%(fullnamepath,outputDriver, version)
    return str(job_info_txt.strip()), str(plugin_info_txt)

def getHipPathCopyTo(src, dst):
    filename0 = hou.hipFile.path()
    src = '%s:' % src
    dst = '%s:' % dst
    filename1 = filename0.split('/')
    filenameNew = os.path.join(dst,'\\',*filename1[1:])
    filenameNew = filenameNew.replace('\\','/')
    tmp = filenameNew.split('/')
    tmp = tmp[1:-1]
    filenamedir = os.path.join(*tmp)
    filenamedir = '%s/%s'%(dst,filenamedir)
    createDir(filenamedir)
    shutil.copyfile(filename0, filenameNew) 
    print(filenameNew+'     ---- ok')
    print(filenamedir)
    return filenamedir

###---------------------------------------------------------------------------------

def main(batchname, filedir, filename, outputDriver, framerange, pool, priority, version, chunkSize, machineLimit, comment):
    name = '%s__%s'%(filename,outputDriver)
    fullnamepath = os.path.join(filedir,filename)
    job_info_txt, plugin_info_txt = GetInfoTxtHoudini(batchname, name, fullnamepath, outputDriver, framerange, pool, priority, version, chunkSize, machineLimit, comment)
    print(job_info_txt)
    print(plugin_info_txt)
    submit_to_deadline(job_info_txt, plugin_info_txt)
    print('submit_to_deadline!!!!!!!!!!!!')

# get seleted node # get frame range 
nodes = hou.selectedNodes()
filedir  = getHipPathCopyTo('D', 'J')
filename = hou.hipFile.basename()
tmp = filename.split('_')
# batchname = '%s_%s_%s'%(tmp[0],tmp[1],tmp[2])
batchname = '_'.join(tmp[:2])
print("batchname:")
print(batchname)
for node in nodes:
    if(node.type().name() != 'fetch'):
        fstart = node.parm('f1').eval()
        fend   = node.parm('f2').eval()
    else:
        sourceNode = hou.node(node.parm('source').eval())
        fstart = sourceNode.parm('f1').eval()
        fend   = sourceNode.parm('f2').eval()
    # framerange = '%i-%i' % (fstart-2, fend+2)
    framerange = '%i-%i' % (fstart, fend)
    rop = node.path()
    main(batchname, filedir, filename, rop, framerange, 'sim', 90, '19.0', 100000, 10, 'auto_SIM' )    
    # main( batchname,filedir, filename, rop, framerange, 'fx', 90, '19.0', 2, 20, 'auto_MESH' )
    print('done---------------------------------------done')

#single machine for sim


