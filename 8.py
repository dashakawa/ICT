widget = int(input())
gizmos = int(input())
mass = widget* 75 + gizmo * 112
if mass > 1000:
    print("Total Mass:", f'{mass/1000:.3f}',"kg")
else:
    print("Total Mass:", mass,"g")