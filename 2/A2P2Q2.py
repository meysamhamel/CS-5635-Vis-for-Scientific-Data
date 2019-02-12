from paraview.simple import *
#   Author: Meysam Hamel
#   UID: U0914328


reader = OpenDataFile("C:\Users\MeySam\Documents\Spring 2018\CS6635\Assignmet2\data02/2d.vti")
UpdatePipeline()  # create chart

#   
plot = PlotOverLine(Input = reader)

map_3d = WarpByScalar(Input = reader, ScaleFactor = 1.3)

Show(reader)
Show(plot)
Show(map_3d)
Render()
