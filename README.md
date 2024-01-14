- Hola mi Nombre es Leticia.
- El programa ya nos lo habian entregado con estructura y con algunos datos que ya capturaba como son:El nombre,la edad e incluso la formula(calculo de msas corporal,lo que me toco fue
- Realizar el ingrfeso de los apellidos paterno y materno y decidi crear funciones para las validaciones de los campos en blanco y la validación de números enteros y números flotantes.
- agregue validaciones extras como que la altura no fuera mayor a 2 metros y la captura de esta fuera con punto decimal,pues si no se colocaba manejaba una altura fuera de rango y el calculo
- de peso salia erroneo.

- lo que me dejo de experiencia es la captura de datos y las diferentes validadciones con altura .
- En lo personal creo que voy aprendiendo mucho de una manera muy practica

- Funcionalidad del programa

- Funcion calculadora(): ejecuta toda la logica que implica la captura de datos y el calculo del IMC
- Funcion validarCadena(): valida si el texto proporcionado esta vacio y regresa un booleano
- Funcion validarPesoAltura(): valida que los datos ingresados para Peso y Altura sean numeros flotantes y no cadenas de texto(String)
- Funcion validarEdad(): valida que los datos ingresados para edad sean numeros enteros y no cadenas de texto.(string)
- Funcion validarAltura(): Esta envia la cadena recibida a la funcion validarPesoAltura() para saber si es un dato flotante valido y si es asi tenemos una validacion para saber si es mayor a 2 metros ya que de no ser asi los calculos seran erroneos
- para datos como ejemplo(165 o 178) que ya como flotantes serian 165.0 o bien 178.0 y eso hace que el calculo nos diga que estamos en "Delgadez severa"
