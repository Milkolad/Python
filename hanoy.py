def move(height,place1, place3, place2):
    if height >= 1:
        move(height-1,place1,place2,place3)
        printf(place1,place3)
        move(height-1,place2,place3,place1)

def printf(fp,tp):
    print("Перемещаем диск с",fp,"на",tp)

move(3,"1","2","3")