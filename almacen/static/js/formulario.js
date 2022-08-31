function validar(){

    /*creo una variable de tipo booleano que en principio tendrá un valor true(verdadero),
    y que se convertirá en false(falso) cuando la condición no se cumpla*/
    var todo_correcto = true;

    /*El primer campo a comprobar es el del nombre. Lo traemos por id y verificamos
    la condición, en este caso, por ejemplo, le decimos que tiene que tener más de dos dígitos
    para que sea un nombre válido. Si no tiene más de dos dígitos, la variable todo_correcto
    devolverá false.*/

     if(document.getElementById('nombre').value == '[A-Za-z]{2,15}') { 
            msg.innerText = 'Debes escribir un nombre en letras'; 
            todo_correcto = false;
          }

    /*Hacemos lo mismo con el campo dirección. En este caso le pediremos al usuario que
    introduzca al menos 10 caracteres.*/
    if(document.getElementById('Email').value.length ){
        todo_correcto = false;
    }

    /*Para comprobar el email haremos uso de una expresión regular. Esto es una secuencia
    de caracteres que nos dirá si el valor ingresado por el usuario tiene estructura de
    correo electrónico. Lo que hacemos es obtener el value del campo de texto destinado
    al email, y le aplicamos el método test() del objeto global RegExp(que nos permite
    trabajar con expresiones regulares).*/
    var expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;
    var email = document.form1.email.value;
    if (!expresion.test(email)){
        todo_correcto = false;
    }

    var valor = document.getElementById("Telefono").value;
    var num = document.form1.telefono.value;
    if( !(/^\+\d{2,3}\s\d{9}$/.test(num))) {
    todo_correcto = false;
    }


    var valor = document.getElementById("campo").value
    if( valor == null || valor.length == 0 || /^\s+$/.test(valor) ) {
        todo_correcto = false;
    }

    /*Por último, y como aviso para el usuario, si no está todo bién, osea, si la variable
    todo_correcto ha devuelto false al menos una vez, generaremos una alerta advirtiendo
    al usuario de que algunos datos ingresados no son los que esperamos.*/
    if(!todo_correcto){
    alert('Algunos campos no están correctos, vuelva a revisarlos');
    todo_correcto = false;
    }
    return todo_correcto;

    
}
