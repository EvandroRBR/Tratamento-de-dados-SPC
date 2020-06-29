

// const voz = window.speechSynthesis;
// const fala = new SpeechSynthesisUtterance("Olá meu nome é cleisa, bem vindo ao analizator, estou aqui para te ajudar");
// fala.lang = "pt-BR";
// voz.speak(fala);



function getAnalise(file) {

  const { PythonShell } = require('python-shell');
  const path = require('path');

  const ops = {
    scriptPath: path.join(__dirname, '../engine/'),
    args: [file]
  };

  const analise = new PythonShell('relatorio.py', ops);

  const div = document.querySelector('.content');

  analise.on('message', function(message) {
    const data = message.split(',');

    for (let i = 0; i < data.length; i++){

      const h4 = document.createElement('p');
      const textNode = document.createTextNode(data[i]);
      h4.appendChild(textNode);
      div.appendChild(h4);     
    }; 

    div.appendChild(document.createElement('br'));

  });
}

function openButton() {
  document.querySelector('.options').classList.toggle('invisible');
}