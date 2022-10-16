from ejemplo.models import Familiar

Familiar(nombre="Rosario", nacimiento="12/06/1957", numero_documento=12312312).save()
Familiar(nombre="Alberto", nacimiento="2/03/2001", numero_documento=89089087).save()
Familiar(nombre="Samuel", nacimiento="23/12/1989", numero_documento=34534567).save()
Familiar(nombre="Florencia", nacimiento="12/09/2022", numero_documento=56756743).save()

print("Se cargo con éxito los usuarios de pruebas")
