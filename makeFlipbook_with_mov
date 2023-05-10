
import os,subprocess
import hou

# houdini run flipbook seq image , make sub folder
# make mov from image foler


def runFlipbook(fstart, fend):
    cur_desktop = hou.ui.curDesktop()
    scene = cur_desktop.paneTabOfType(hou.paneTabType.SceneViewer)
    flipbook_options = scene.flipbookSettings().stash()
    hip_file = hou.hipFile
    path_name = hip_file.name()
    file_name = hip_file.basename()
    spli_file_name = file_name.split('.')
    spli_path_name = path_name.split("/")
    new_dir_path = '/'.join(spli_path_name[:-1])+"/"+'flipbook/temp' 
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    frame_range = hou.playbar.playbackRange()
    fstart = int(frame_range[0])
    fend   = int(frame_range[1])
    flipbook_options.frameRange( (int(frame_range[0]),int(frame_range[1])) )
    flipbook_options.output(new_dir_path + "/" + spli_file_name[0] + ".$F4.jpg" )
    flipbook_options.outputZoom(100)
    flipbook_options.useResolution(1)
    scaleres = float(0.5)
    ressx = 1920
    ressy = 1080    
    #flipbook_options.resolution((ressx,ressy))
    flipbook_options.resolution((ressx,ressy))
    flipbook_options.cropOutMaskOverlay(1)
    scene.flipbook(scene.curViewport(), flipbook_options)

def run(ffmpegexe, movname, startframe):
    hip_file = hou.hipFile
    path_name = hip_file.name()
    file_name = hip_file.basename()
    spli_file_name = file_name.split('.')
    spli_path_name = path_name.split("/")
    new_dir_path = '/'.join(spli_path_name[:-1])+"/"+'flipbook/temp' 
    fullnamepath = new_dir_path + "/" +spli_file_name[0]+ ".%04d.jpg"
    outputmovpath = '/'.join(spli_path_name[:-1])+"/"+'flipbook'
    outputmov = '%s/%s.mov'%(outputmovpath, spli_file_name[0])
    fmt = '%s -start_number %s -i %s -c:v libx264 -vf fps=25 -pix_fmt yuv420p -movflags faststart -safe 0 -s 1920x1080  %s' % (ffmpegexe, startframe, fullnamepath, outputmov)
    subprocess.Popen(fmt)
    os.startfile(outputmovpath)

frame_range = hou.playbar.playbackRange()
fstart = int(frame_range[0]+1)
fend   = int(frame_range[1]-1)

runFlipbook(fstart, fend)
ffmpegexe = 'D:/ffmpeg.exe'   # https://ffmpeg.org/download.html  download it
run(ffmpegexe ,'test', fstart)

