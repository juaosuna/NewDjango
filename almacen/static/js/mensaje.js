window.onload = function () {

                var ejemplo = document.getElementById('ejemplo');

                ejemplo.addEventListener("click", ejecutarEjemplo);

}


function ejecutarEjemplo () {

var msg = '';

var formularios = document.forms;

for (var i=0; i<formularios.length;i++){

                for (var j=0; j<formularios[i].elements.length; j++){

                               msg = msg + '\n\nElemento '+j+ ' del formulario '+(i+1)+ ' tiene id: '+ formularios[i].elements[j].id;

                               msg = msg + ' y name: ' + formularios[i].elements[j].name;

                }

}

alert (msg);

}
