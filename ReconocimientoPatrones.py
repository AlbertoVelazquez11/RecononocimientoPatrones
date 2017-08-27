import Victima
print "Favor de regitrar los datos siguientes:"
print "DATOS PERSONALES.-"
datosPersonales = Victima.datos

datosPersonales[ "ID" ] = raw_input("ID: ")
datosPersonales[ "nombre" ] = raw_input( "Nombre: " )
datosPersonales[ "edad" ] = raw_input( "Edad: " )
datosPersonales[ "genero" ] = raw_input( "Genero: " )
datosPersonales[ "numero_personas" ][ 0 ] = raw_input( "Numero de personas: " )
datosPersonales[ "correo" ] = raw_input( "Correo: " )
datosPersonales[ "telefono" ] = raw_input( "Telefono: " )
datosPersonales[ "domicilio" ][ 0 ] = raw_input( "Calle: " )
datosPersonales[ "domicilio" ][ 1 ] = raw_input( "Numero: " )
datosPersonales[ "domicilio" ][ 2 ] = raw_input( "Colonia: " )
'''
datosPersonales[ "ID" ] = "123"
datosPersonales[ "nombre" ] = "Alberto"
datosPersonales[ "edad" ] = "25"
datosPersonales[ "genero" ] = "Masculino"
datosPersonales[ "numero_personas" ][ 0 ] = "0"
datosPersonales[ "correo" ] = "alberto@hotmail.com"
datosPersonales[ "telefono" ] = "6672365835"
datosPersonales[ "domicilio" ][ 0 ] = "vesubio"
datosPersonales[ "domicilio" ][ 1 ] = "2072"
datosPersonales[ "domicilio" ][ 2 ] = "Montesierra"
for dato in datosPersonales :
	print dato + ": "
	print datosPersonales[dato]'''
Victima.Guardar( datosPersonales )