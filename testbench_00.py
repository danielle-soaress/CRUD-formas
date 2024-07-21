from package.maths.Shapes import *
from package.maths.CartesianPlane import CartesianPlane
from package.maths.Shape import *
from package.maths.Point import Point
from package.maths.Line import *

def workspace():
    try:
        print('Esse arquivo de teste foi feito para testar o Plano Cartesiano')
        
        plane = CartesianPlane()

        rect = Rectangle('myRect', Point('p1',4,1), Point('p2', 2,3), Point('p3',4,3), Point('p4', 2,1), '#000')
        triangle = Triangle('myTriangle', Point('p1', 3,4),Point('p2', 5,6),Point('p3', 7,4), '#000')
        circle = Circle('myCircle', Point('p1', 3,4), 3 , '#000')
        p1 = Point('myPoint', 2, 2, '#000')
        l1 = Line('myLine', Point('l1_p1', 2, 2), Point('l1_p2', 4, 7), '#000')
        s1 = LineSegment('Segment', Point('s1_p1', 4, 2), Point('s1_p2', 14, 17), '#000')
        
        entities = [rect, triangle, circle, p1]

        print(f'\n\nfiguras: ')

        plane.setEntities(entities)

        for entity in plane.getEntities():
            print(entity.getName() + ' - ' + entity.__class__.__name__)

        # ------------- deletando uma figura

        print(f'\n\ndeletando a figura myRect')

        plane.deleteEntity('myRect')

        for entity in plane.getEntities():
            print(entity.getName() + ' - ' + entity.__class__.__name__)

        # ------------- deletando todas as figuras

        print(f'\n\nremovendo todas as figuras')

        plane.reset()

        for entity in plane.getEntities():
            print(entity.getName() + ' - ' + entity.__class__.__name__)
        
        if len(plane.getEntities()) == 0:
            print('plano cartesiano vazio!')

        # ------------- adicionando duas figuras individualmente

        print(f'\n\nadicionando 2 figuras: myLine e myLineSegment')

        plane.addEntity(l1)
        plane.addEntity(s1)

        for entity in plane.getEntities():
            print(entity.getName() + ' - ' + entity.__class__.__name__)

        # ------------- adicionando uma figura já existente

        print(f'\n\nadicionando myLine - uma figura já existente')

        plane.addEntity(l1)

        for entity in plane.getEntities():
            print(entity.getName() + ' - ' + entity.__class__.__name__)

        # ------------- adicionando uma figura já existente

        print(f'\n\nadicionando mais um objeto Line e pegando todos os objetos da classe Line')
        l2 = Line('myLine2', Point('l1_p1', 3, 4), Point('l1_p2', 5, 6), '#000')
        plane.addEntity(l2)
        figuras = list(map(lambda x: x.getName(), plane.getAllClassEntities(Line)))
        print(figuras)

    except InvalidAction as e:
        print(e.message)
    except InvalidName as e:
        print(e.message)

if (__name__ == "__main__"):
    workspace()
