#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Arrow'
arrow1 = Arrow()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1564, 818]

# show data in view
arrow1Display = Show(arrow1, renderView1)

# trace defaults for the display properties.
arrow1Display.Representation = 'Surface'
arrow1Display.ColorArrayName = [None, '']
arrow1Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow1Display.SelectOrientationVectors = 'None'
arrow1Display.ScaleFactor = 0.1
arrow1Display.SelectScaleArray = 'None'
arrow1Display.GlyphType = 'Arrow'
arrow1Display.GlyphTableIndexArray = 'None'
arrow1Display.DataAxesGrid = 'GridAxesRepresentation'
arrow1Display.PolarAxes = 'PolarAxesRepresentation'
arrow1Display.GaussianRadius = 0.05
arrow1Display.SetScaleArray = [None, '']
arrow1Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow1Display.OpacityArray = [None, '']
arrow1Display.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on arrow1Display
arrow1Display.Orientation = [0.0, 0.0, 22.5]

# Properties modified on arrow1Display.PolarAxes
arrow1Display.PolarAxes.Orientation = [0.0, 0.0, 22.5]

# create a new 'Arrow'
arrow2 = Arrow()

# show data in view
arrow2Display = Show(arrow2, renderView1)

# trace defaults for the display properties.
arrow2Display.Representation = 'Surface'
arrow2Display.ColorArrayName = [None, '']
arrow2Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow2Display.SelectOrientationVectors = 'None'
arrow2Display.ScaleFactor = 0.1
arrow2Display.SelectScaleArray = 'None'
arrow2Display.GlyphType = 'Arrow'
arrow2Display.GlyphTableIndexArray = 'None'
arrow2Display.DataAxesGrid = 'GridAxesRepresentation'
arrow2Display.PolarAxes = 'PolarAxesRepresentation'
arrow2Display.GaussianRadius = 0.05
arrow2Display.SetScaleArray = [None, '']
arrow2Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow2Display.OpacityArray = [None, '']
arrow2Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Arrow'
arrow3 = Arrow()

# show data in view
arrow3Display = Show(arrow3, renderView1)

# trace defaults for the display properties.
arrow3Display.Representation = 'Surface'
arrow3Display.ColorArrayName = [None, '']
arrow3Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow3Display.SelectOrientationVectors = 'None'
arrow3Display.ScaleFactor = 0.1
arrow3Display.SelectScaleArray = 'None'
arrow3Display.GlyphType = 'Arrow'
arrow3Display.GlyphTableIndexArray = 'None'
arrow3Display.DataAxesGrid = 'GridAxesRepresentation'
arrow3Display.PolarAxes = 'PolarAxesRepresentation'
arrow3Display.GaussianRadius = 0.05
arrow3Display.SetScaleArray = [None, '']
arrow3Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow3Display.OpacityArray = [None, '']
arrow3Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on arrow3Display
arrow3Display.Orientation = [0.0, 0.0, 45.0]

# Properties modified on arrow3Display.PolarAxes
arrow3Display.PolarAxes.Orientation = [0.0, 0.0, 45.0]

# create a new 'Arrow'
arrow4 = Arrow()

# show data in view
arrow4Display = Show(arrow4, renderView1)

# trace defaults for the display properties.
arrow4Display.Representation = 'Surface'
arrow4Display.ColorArrayName = [None, '']
arrow4Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow4Display.SelectOrientationVectors = 'None'
arrow4Display.ScaleFactor = 0.1
arrow4Display.SelectScaleArray = 'None'
arrow4Display.GlyphType = 'Arrow'
arrow4Display.GlyphTableIndexArray = 'None'
arrow4Display.DataAxesGrid = 'GridAxesRepresentation'
arrow4Display.PolarAxes = 'PolarAxesRepresentation'
arrow4Display.GaussianRadius = 0.05
arrow4Display.SetScaleArray = [None, '']
arrow4Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow4Display.OpacityArray = [None, '']
arrow4Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on arrow4Display
arrow4Display.Orientation = [0.0, 0.0, 67.5]

# Properties modified on arrow4Display.PolarAxes
arrow4Display.PolarAxes.Orientation = [0.0, 0.0, 67.5]

# create a new 'Arrow'
arrow5 = Arrow()

# show data in view
arrow5Display = Show(arrow5, renderView1)

# trace defaults for the display properties.
arrow5Display.Representation = 'Surface'
arrow5Display.ColorArrayName = [None, '']
arrow5Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow5Display.SelectOrientationVectors = 'None'
arrow5Display.ScaleFactor = 0.1
arrow5Display.SelectScaleArray = 'None'
arrow5Display.GlyphType = 'Arrow'
arrow5Display.GlyphTableIndexArray = 'None'
arrow5Display.DataAxesGrid = 'GridAxesRepresentation'
arrow5Display.PolarAxes = 'PolarAxesRepresentation'
arrow5Display.GaussianRadius = 0.05
arrow5Display.SetScaleArray = [None, '']
arrow5Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow5Display.OpacityArray = [None, '']
arrow5Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on arrow5Display
arrow5Display.Orientation = [0.0, 0.0, 90.0]

# Properties modified on arrow5Display.PolarAxes
arrow5Display.PolarAxes.Orientation = [0.0, 0.0, 90.0]

# create a new 'Arrow'
arrow6 = Arrow()

# set active source
SetActiveSource(arrow6)

# show data in view
arrow6Display = Show(arrow6, renderView1)

# trace defaults for the display properties.
arrow6Display.Representation = 'Surface'
arrow6Display.ColorArrayName = [None, '']
arrow6Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow6Display.SelectOrientationVectors = 'None'
arrow6Display.ScaleFactor = 0.1
arrow6Display.SelectScaleArray = 'None'
arrow6Display.GlyphType = 'Arrow'
arrow6Display.GlyphTableIndexArray = 'None'
arrow6Display.DataAxesGrid = 'GridAxesRepresentation'
arrow6Display.PolarAxes = 'PolarAxesRepresentation'
arrow6Display.GaussianRadius = 0.05
arrow6Display.SetScaleArray = [None, '']
arrow6Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow6Display.OpacityArray = [None, '']
arrow6Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow6Display = Show(arrow6, renderView1)

# Properties modified on arrow6Display
arrow6Display.Orientation = [0.0, 0.0, 112.5]

# Properties modified on arrow6Display.PolarAxes
arrow6Display.PolarAxes.Orientation = [0.0, 0.0, 112.5]

# create a new 'Arrow'
arrow7 = Arrow()

# create a new 'Arrow'
arrow8 = Arrow()

# create a new 'Arrow'
arrow9 = Arrow()

# create a new 'Arrow'
arrow10 = Arrow()

# create a new 'Arrow'
arrow11 = Arrow()

# create a new 'Arrow'
arrow12 = Arrow()

# create a new 'Arrow'
arrow13 = Arrow()

# create a new 'Arrow'
arrow14 = Arrow()

# create a new 'Arrow'
arrow15 = Arrow()

# create a new 'Arrow'
arrow16 = Arrow()

# set active source
SetActiveSource(arrow7)

# show data in view
arrow7Display = Show(arrow7, renderView1)

# trace defaults for the display properties.
arrow7Display.Representation = 'Surface'
arrow7Display.ColorArrayName = [None, '']
arrow7Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow7Display.SelectOrientationVectors = 'None'
arrow7Display.ScaleFactor = 0.1
arrow7Display.SelectScaleArray = 'None'
arrow7Display.GlyphType = 'Arrow'
arrow7Display.GlyphTableIndexArray = 'None'
arrow7Display.DataAxesGrid = 'GridAxesRepresentation'
arrow7Display.PolarAxes = 'PolarAxesRepresentation'
arrow7Display.GaussianRadius = 0.05
arrow7Display.SetScaleArray = [None, '']
arrow7Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow7Display.OpacityArray = [None, '']
arrow7Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow10Display = Show(arrow10, renderView1)

# trace defaults for the display properties.
arrow10Display.Representation = 'Surface'
arrow10Display.ColorArrayName = [None, '']
arrow10Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow10Display.SelectOrientationVectors = 'None'
arrow10Display.ScaleFactor = 0.1
arrow10Display.SelectScaleArray = 'None'
arrow10Display.GlyphType = 'Arrow'
arrow10Display.GlyphTableIndexArray = 'None'
arrow10Display.DataAxesGrid = 'GridAxesRepresentation'
arrow10Display.PolarAxes = 'PolarAxesRepresentation'
arrow10Display.GaussianRadius = 0.05
arrow10Display.SetScaleArray = [None, '']
arrow10Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow10Display.OpacityArray = [None, '']
arrow10Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow11Display = Show(arrow11, renderView1)

# trace defaults for the display properties.
arrow11Display.Representation = 'Surface'
arrow11Display.ColorArrayName = [None, '']
arrow11Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow11Display.SelectOrientationVectors = 'None'
arrow11Display.ScaleFactor = 0.1
arrow11Display.SelectScaleArray = 'None'
arrow11Display.GlyphType = 'Arrow'
arrow11Display.GlyphTableIndexArray = 'None'
arrow11Display.DataAxesGrid = 'GridAxesRepresentation'
arrow11Display.PolarAxes = 'PolarAxesRepresentation'
arrow11Display.GaussianRadius = 0.05
arrow11Display.SetScaleArray = [None, '']
arrow11Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow11Display.OpacityArray = [None, '']
arrow11Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow12Display = Show(arrow12, renderView1)

# trace defaults for the display properties.
arrow12Display.Representation = 'Surface'
arrow12Display.ColorArrayName = [None, '']
arrow12Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow12Display.SelectOrientationVectors = 'None'
arrow12Display.ScaleFactor = 0.1
arrow12Display.SelectScaleArray = 'None'
arrow12Display.GlyphType = 'Arrow'
arrow12Display.GlyphTableIndexArray = 'None'
arrow12Display.DataAxesGrid = 'GridAxesRepresentation'
arrow12Display.PolarAxes = 'PolarAxesRepresentation'
arrow12Display.GaussianRadius = 0.05
arrow12Display.SetScaleArray = [None, '']
arrow12Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow12Display.OpacityArray = [None, '']
arrow12Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow13Display = Show(arrow13, renderView1)

# trace defaults for the display properties.
arrow13Display.Representation = 'Surface'
arrow13Display.ColorArrayName = [None, '']
arrow13Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow13Display.SelectOrientationVectors = 'None'
arrow13Display.ScaleFactor = 0.1
arrow13Display.SelectScaleArray = 'None'
arrow13Display.GlyphType = 'Arrow'
arrow13Display.GlyphTableIndexArray = 'None'
arrow13Display.DataAxesGrid = 'GridAxesRepresentation'
arrow13Display.PolarAxes = 'PolarAxesRepresentation'
arrow13Display.GaussianRadius = 0.05
arrow13Display.SetScaleArray = [None, '']
arrow13Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow13Display.OpacityArray = [None, '']
arrow13Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow14Display = Show(arrow14, renderView1)

# trace defaults for the display properties.
arrow14Display.Representation = 'Surface'
arrow14Display.ColorArrayName = [None, '']
arrow14Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow14Display.SelectOrientationVectors = 'None'
arrow14Display.ScaleFactor = 0.1
arrow14Display.SelectScaleArray = 'None'
arrow14Display.GlyphType = 'Arrow'
arrow14Display.GlyphTableIndexArray = 'None'
arrow14Display.DataAxesGrid = 'GridAxesRepresentation'
arrow14Display.PolarAxes = 'PolarAxesRepresentation'
arrow14Display.GaussianRadius = 0.05
arrow14Display.SetScaleArray = [None, '']
arrow14Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow14Display.OpacityArray = [None, '']
arrow14Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow15Display = Show(arrow15, renderView1)

# trace defaults for the display properties.
arrow15Display.Representation = 'Surface'
arrow15Display.ColorArrayName = [None, '']
arrow15Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow15Display.SelectOrientationVectors = 'None'
arrow15Display.ScaleFactor = 0.1
arrow15Display.SelectScaleArray = 'None'
arrow15Display.GlyphType = 'Arrow'
arrow15Display.GlyphTableIndexArray = 'None'
arrow15Display.DataAxesGrid = 'GridAxesRepresentation'
arrow15Display.PolarAxes = 'PolarAxesRepresentation'
arrow15Display.GaussianRadius = 0.05
arrow15Display.SetScaleArray = [None, '']
arrow15Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow15Display.OpacityArray = [None, '']
arrow15Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow16Display = Show(arrow16, renderView1)

# trace defaults for the display properties.
arrow16Display.Representation = 'Surface'
arrow16Display.ColorArrayName = [None, '']
arrow16Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow16Display.SelectOrientationVectors = 'None'
arrow16Display.ScaleFactor = 0.1
arrow16Display.SelectScaleArray = 'None'
arrow16Display.GlyphType = 'Arrow'
arrow16Display.GlyphTableIndexArray = 'None'
arrow16Display.DataAxesGrid = 'GridAxesRepresentation'
arrow16Display.PolarAxes = 'PolarAxesRepresentation'
arrow16Display.GaussianRadius = 0.05
arrow16Display.SetScaleArray = [None, '']
arrow16Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow16Display.OpacityArray = [None, '']
arrow16Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow7Display = Show(arrow7, renderView1)

# show data in view
arrow8Display = Show(arrow8, renderView1)

# trace defaults for the display properties.
arrow8Display.Representation = 'Surface'
arrow8Display.ColorArrayName = [None, '']
arrow8Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow8Display.SelectOrientationVectors = 'None'
arrow8Display.ScaleFactor = 0.1
arrow8Display.SelectScaleArray = 'None'
arrow8Display.GlyphType = 'Arrow'
arrow8Display.GlyphTableIndexArray = 'None'
arrow8Display.DataAxesGrid = 'GridAxesRepresentation'
arrow8Display.PolarAxes = 'PolarAxesRepresentation'
arrow8Display.GaussianRadius = 0.05
arrow8Display.SetScaleArray = [None, '']
arrow8Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow8Display.OpacityArray = [None, '']
arrow8Display.OpacityTransferFunction = 'PiecewiseFunction'

# show data in view
arrow9Display = Show(arrow9, renderView1)

# trace defaults for the display properties.
arrow9Display.Representation = 'Surface'
arrow9Display.ColorArrayName = [None, '']
arrow9Display.OSPRayScaleFunction = 'PiecewiseFunction'
arrow9Display.SelectOrientationVectors = 'None'
arrow9Display.ScaleFactor = 0.1
arrow9Display.SelectScaleArray = 'None'
arrow9Display.GlyphType = 'Arrow'
arrow9Display.GlyphTableIndexArray = 'None'
arrow9Display.DataAxesGrid = 'GridAxesRepresentation'
arrow9Display.PolarAxes = 'PolarAxesRepresentation'
arrow9Display.GaussianRadius = 0.05
arrow9Display.SetScaleArray = [None, '']
arrow9Display.ScaleTransferFunction = 'PiecewiseFunction'
arrow9Display.OpacityArray = [None, '']
arrow9Display.OpacityTransferFunction = 'PiecewiseFunction'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on arrow7Display
arrow7Display.Orientation = [0.0, 0.0, 135.0]

# Properties modified on arrow7Display.PolarAxes
arrow7Display.PolarAxes.Orientation = [0.0, 0.0, 135.0]

# set active source
SetActiveSource(arrow8)

# hide data in view
Hide(arrow8, renderView1)

# set active source
SetActiveSource(arrow8)

# show data in view
arrow8Display = Show(arrow8, renderView1)

# Properties modified on arrow8Display
arrow8Display.Orientation = [0.0, 0.0, 157.0]

# Properties modified on arrow8Display.PolarAxes
arrow8Display.PolarAxes.Orientation = [0.0, 0.0, 157.0]

# Properties modified on arrow8Display
arrow8Display.Orientation = [0.0, 0.0, 157.5]

# Properties modified on arrow8Display.PolarAxes
arrow8Display.PolarAxes.Orientation = [0.0, 0.0, 157.5]

# set active source
SetActiveSource(arrow9)

# Properties modified on arrow9Display
arrow9Display.Orientation = [0.0, 0.0, 180.0]

# Properties modified on arrow9Display.PolarAxes
arrow9Display.PolarAxes.Orientation = [0.0, 0.0, 180.0]

# set active source
SetActiveSource(arrow10)

# Properties modified on arrow10Display
arrow10Display.Orientation = [0.0, 0.0, 202.5]

# Properties modified on arrow10Display.PolarAxes
arrow10Display.PolarAxes.Orientation = [0.0, 0.0, 202.5]

# set active source
SetActiveSource(arrow11)

# Properties modified on arrow11Display
arrow11Display.Orientation = [0.0, 0.0, 225.0]

# Properties modified on arrow11Display.PolarAxes
arrow11Display.PolarAxes.Orientation = [0.0, 0.0, 225.0]

# set active source
SetActiveSource(arrow12)

# Properties modified on arrow12Display
arrow12Display.Orientation = [0.0, 0.0, 247.5]

# Properties modified on arrow12Display.PolarAxes
arrow12Display.PolarAxes.Orientation = [0.0, 0.0, 247.5]

# set active source
SetActiveSource(arrow13)

# Properties modified on arrow13Display
arrow13Display.Orientation = [0.0, 0.0, 270.0]

# Properties modified on arrow13Display.PolarAxes
arrow13Display.PolarAxes.Orientation = [0.0, 0.0, 270.0]

# set active source
SetActiveSource(arrow14)

# Properties modified on arrow14Display
arrow14Display.Orientation = [0.0, 0.0, 292.5]

# Properties modified on arrow14Display.PolarAxes
arrow14Display.PolarAxes.Orientation = [0.0, 0.0, 292.5]

# set active source
SetActiveSource(arrow15)

# Properties modified on arrow15Display
arrow15Display.Orientation = [0.0, 0.0, 315.0]

# Properties modified on arrow15Display.PolarAxes
arrow15Display.PolarAxes.Orientation = [0.0, 0.0, 315.0]

# set active source
SetActiveSource(arrow16)

# Properties modified on arrow16Display
arrow16Display.Orientation = [0.0, 0.0, 337.5]

# Properties modified on arrow16Display.PolarAxes
arrow16Display.PolarAxes.Orientation = [0.0, 0.0, 337.5]

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.782828458001629, 0.07676772431472786, 3.5401508937101402]
renderView1.CameraFocalPoint = [0.782828458001629, 0.07676772431472786, 0.0]
renderView1.CameraParallelScale = 0.5172040216672718

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).