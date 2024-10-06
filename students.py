estudiantes = [ 
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

def score_average(scores):
    total_sum = 0

    for score in scores:
        total_sum += score

    average = total_sum / len(scores)
    return average


def is_prime_number(age):
    for i in range(2, age):
        if age % i == 0:
            return False
    return True


def run():
    print("Los estudiantes mayores de 18 años cuyo promedio es mayor a 85 son: ")
    for student in estudiantes:
        if student["edad"] > 18 and score_average(student["calificaciones"]) > 85:
            print(student)
    
    print("Los estudiantes mayores de 18 años cuya edad es un numero primero son: ")
    for student in estudiantes:
        if student["edad"] > 18 and is_prime_number(student["edad"]):
            print(student)


if __name__ == "__main__":
    run()