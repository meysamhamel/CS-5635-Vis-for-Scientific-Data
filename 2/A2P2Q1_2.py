from paraview.simple import *
import paraview.simple as pvs

#Meysam Hamel
#Part 2

is_A2P2Q1_2 = True  


arrow1 = Arrow(TipResolution=16)
arrow2 = Arrow(TipResolution=16)
arrow3 = Arrow(TipResolution=16)
arrow4 = Arrow(TipResolution=16)
arrow5 = Arrow(TipResolution=16)
arrow6 = Arrow(TipResolution=16)
arrow7 = Arrow(TipResolution=16)
arrow8 = Arrow(TipResolution=16)
arrow9 = Arrow(TipResolution=16)
arrow10 = Arrow(TipResolution=16)
arrow11 = Arrow(TipResolution=16)
arrow12 = Arrow(TipResolution=16)
arrow13 = Arrow(TipResolution=16)
arrow14 = Arrow(TipResolution=16)
arrow15 = Arrow(TipResolution=16)
arrow16 = Arrow(TipResolution=16)

m_tran1 = Transform(Input = arrow1)
m_tran2 = Transform(Input = arrow2)
m_tran3 = Transform(Input = arrow3)
m_tran4 = Transform(Input = arrow4)
m_tran5 = Transform(Input = arrow5)
m_tran6 = Transform(Input = arrow6)
m_tran7 = Transform(Input = arrow7)
m_tran8 = Transform(Input = arrow8)
m_tran9 = Transform(Input = arrow9)
m_tran10 = Transform(Input = arrow10)
m_tran11 = Transform(Input = arrow11)
m_tran12 = Transform(Input = arrow12)
m_tran13 = Transform(Input = arrow13)
m_tran14 = Transform(Input = arrow14)
m_tran15 = Transform(Input = arrow15)
m_tran16 = Transform(Input = arrow16)

degree = 0
m_tran1.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran2.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran3.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran4.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran5.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran6.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran7.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran8.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran9.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran10.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran11.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran12.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran13.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran14.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran15.Transform.Rotate = [0., degree, 0.]
degree += 22.5
m_tran16.Transform.Rotate = [0., degree, 0.]



if is_A2P2Q1_2:
    Show(Shrink(m_tran1))
    Show(ExtractEdges(m_tran1))

    Show(Shrink(m_tran2))
    Show(ExtractEdges(m_tran2))

    Show(Shrink(m_tran3))
    Show(ExtractEdges(m_tran3))

    Show(Shrink(m_tran4))
    Show(ExtractEdges(m_tran4))

    Show(Shrink(m_tran5))
    Show(ExtractEdges(m_tran5))

    Show(Shrink(m_tran6))
    Show(ExtractEdges(m_tran6))

    Show(Shrink(m_tran7))
    Show(ExtractEdges(m_tran7))

    Show(Shrink(m_tran8))
    Show(ExtractEdges(m_tran8))

    Show(Shrink(m_tran9))
    Show(ExtractEdges(m_tran9))

    Show(Shrink(m_tran10))
    Show(ExtractEdges(m_tran10))

    Show(Shrink(m_tran11))
    Show(ExtractEdges(m_tran11))

    Show(Shrink(m_tran12))
    Show(ExtractEdges(m_tran12))

    Show(Shrink(m_tran13))
    Show(ExtractEdges(m_tran13))

    Show(Shrink(m_tran14))
    Show(ExtractEdges(m_tran14))

    Show(Shrink(m_tran15))
    Show(ExtractEdges(m_tran15))

    Show(Shrink(m_tran16))
    Show(ExtractEdges(m_tran16))
else:
    Show(m_tran1)
    Show(m_tran2)
    Show(m_tran3)
    Show(m_tran4)
    Show(m_tran5)
    Show(m_tran6)
    Show(m_tran7)
    Show(m_tran8)
    Show(m_tran9)
    Show(m_tran10)
    Show(m_tran11)
    Show(m_tran12)
    Show(m_tran13)
    Show(m_tran14)
    Show(m_tran15)
    Show(m_tran16)

Render()

