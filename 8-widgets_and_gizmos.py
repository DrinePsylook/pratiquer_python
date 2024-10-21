# 8 - Widgets and Gizmos

nb_widget = int(input("Combien de widgets avez-vous ? "))
nb_gizmo = int(input("Combien de gadgets avez-vous ? "))

weight_widget = 75
weight_gizmo = 112

total_weight = (nb_widget * weight_widget) + (nb_gizmo * weight_gizmo)

print(f"Le poids total des pièces est de {total_weight}")