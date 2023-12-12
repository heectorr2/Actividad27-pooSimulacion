from colorama import Fore, Style
class Curso:
    def __init__(self, id_curso, nombre, creditos, anos_de_estudio):
        self.id_curso = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def mostrar_ficha(self):
        print(f"{Fore.CYAN}Ficha del Curso {self.nombre}:{Style.RESET_ALL}")
        print(f"ID: {self.id_curso}")
        print(f"Créditos: {self.creditos}")
        print(f"Años de Estudio: {self.anos_de_estudio}")
        print("-----------------------")

class Alumno:
    def __init__(self, id_alumno, nombre, email, telefono):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.email = email
        self.telefono= telefono

    def mostrar_ficha(self):
        print(f"{Fore.YELLOW}Ficha del Alumno {self.nombre}:{Style.RESET_ALL}")
        print(f"ID: {self.id_alumno}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print("-----------------------")

class Matricula:
    matriculas_realizadas = []

    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso
        Matricula.matriculas_realizadas.append(self)

    @classmethod
    def mostrar_matriculas_realizadas(cls):
        print(f"{Fore.GREEN}Matrículas realizadas en el centro:{Style.RESET_ALL}")
        for matricula in cls.matriculas_realizadas:
            print(f"ID Matrícula: {matricula.id_matricula}")
            print(f"Fecha de Matrícula: {matricula.fecha_matricula}")
            print(f"ID Alumno: {matricula.id_alumno}")
            print(f"ID Curso: {matricula.id_curso}")
            print("-----------------------")
try:
#  instancias de las clases
    curso1 = Curso(1, "Matemáticas", 4, 2)
    curso2 = Curso(2, "Programación", 3, 3)

    alumno1 = Alumno(1, "Pepe", "pepe@gmail.com", 603457141)
    alumno2 = Alumno(2, "Josefa", "josefa@gmail.com", 609123454)

    matricula1 = Matricula(1, "2023-01-01", alumno1.id_alumno, curso1.id_curso)
    matricula2 = Matricula(2, "2023-01-02", alumno2.id_alumno, curso1.id_curso)
    matricula3 = Matricula(3, "2023-01-03", alumno2.id_alumno, curso2.id_curso)

    curso1.mostrar_ficha()
    curso2.mostrar_ficha()

    alumno1.mostrar_ficha()
    alumno2.mostrar_ficha()

    Matricula.mostrar_matriculas_realizadas()
except ValueError as e:
    print(f"Error al crear la instancia: {e}")
except Exception as e:
    print(f"Error desconocido: {e}")
