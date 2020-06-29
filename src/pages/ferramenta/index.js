const divTableName = document.querySelector('.table-name');
const divPreSetting = document.querySelector('.pre-settings');
const divAnalizator = document.querySelector('.analizator');
const sectionButtonsCol = document.querySelector('.buttons-col');
const tableName = document.querySelector('.inputTableName');
const txtAreaRelatorio = document.querySelector('.textAreaRelatorio');

const matriz=[];
const configAnalise = [];
let array=[];


function toSettingsPage(){
  returnPython()
  divTableName.classList.add('hidden');
  divPreSetting.classList.remove('hidden');
}

function goBackToStart(analizator){
  if(analizator){
    divTableName.classList.remove('hidden');
    divPreSetting.classList.add('hidden');
    divAnalizator.classList.add('hidden');
    matriz = []
    sectionButtonsCol.removeChild('section')
  }else{
    divTableName.classList.remove('hidden');
    divPreSetting.classList.add('hidden');
  }

}

function runAnalise(){
  divPreSetting.classList.add('hidden');
  divAnalizator.classList.remove('hidden');

  const opts = ['nulo','preenchido','repetido']

  for(let i = 0; i < array[1].length; i++){
    if(array[1][i]){
      const option = document.getElementById(`${array[1][i]}`);
      configAnalise.push([array[1][i],option.value]);
    }
    
  }

  const filteredOpts = []
  const badIds = []

  for (let i = 0; i < configAnalise.length; i++){
    for (opt of opts){
      if(configAnalise[i][1].indexOf(opt) >= 0){
        filteredOpts.push(configAnalise[i])
      }
    }
  }

  for(let i = 0; i < array[1].length -1; i++){
    for (let j = 0; j < filteredOpts.length; j++){
      if(array[1][i] == filteredOpts[j][0]){
        for(let z = 0; z < array[i+2].length; z++){
          if(filteredOpts[j][1] == 'nulo'){
            if(!array[i+2][z] || array[i+2][z].indexOf("empty") >=0){
              badIds.push(z)
            }
            
          }else if(filteredOpts[j][1] == 'preenchido'){
            if(array[i+2][z] && array[i+2][z].indexOf('empty') < 0){
              badIds.push(z)
            }
          }
        }
      }
    }
  }


  const textArray = [];
  for(let k = 0; k < badIds.length -1; k++){
    let textRelatorio = ''
    for(let i = 2; i < array[1].length +1; i++){
      
      for(let j = 0; j < array[i].length; j++){
        if(j === badIds[k]){
          textRelatorio += ` ${array[i][j]} `
        }      
      }
    }
    textArray.push(`Linha ${badIds[k]+2} - ${textRelatorio}`);
    textRelatorio = ''
  }

  textMetadado = 'Metadados: ';
  for(let i = 0; i < array[1].length -1; i++){
    textMetadado += ` ${array[1][i]} `
  }

  textConfigs = '\n\nConfigurações setadas:\n'
  for(let i = 0; i < filteredOpts.length; i++){
    textConfigs += `\n${filteredOpts[i][0]} não deve estar ${filteredOpts[i][1]}\n\n`
    for(let j = 0; j < array[1].length; j++){
      if(filteredOpts[i][0] == array[1][j]){
        textConfigs += `${filteredOpts[i][0]} se encontra na ${j+1} posição de cada linha `;
      }
    }
  }

  const texto = document.createTextNode(`Ao todo foram encontrados ${badIds.length -1} Linha problematicas:\n`);
  const nodeMetadado = document.createTextNode('\n\n' + textMetadado);
  const nodeConfig = document.createTextNode(textConfigs + '\n\nLinhas problematica');

  txtAreaRelatorio.appendChild(texto);
  txtAreaRelatorio.appendChild(nodeMetadado);
  txtAreaRelatorio.appendChild(nodeConfig);
   
  for(item of textArray){
    const textoRelatorio = document.createTextNode('\n' + item);
    txtAreaRelatorio.appendChild(textoRelatorio);
  }  
}

function metadadoOpts(data){
  array = data
  for(let word = 0; word < array[1].length -1; word++){
    const select = document.createElement('select');
    const id = document.createAttribute('id');
    id.value = array[1][word];
    select.setAttributeNode(id);

    const metadado = document.createTextNode(array[1][word]);
    const nulo = document.createTextNode('nulo');
    const repetido = document.createTextNode('repetido');
    const preenchido = document.createTextNode('preenchido');

    const optMetadado = document.createElement('option');
    const optNull = document.createElement('option');
    const optRepetidos = document.createElement('option');
    const optPreenchidos = document.createElement('option');

    optMetadado.appendChild(metadado);
    optNull.appendChild(nulo);
    optRepetidos.appendChild(repetido);
    optPreenchidos.appendChild(preenchido);

    const opts  = [optMetadado,optNull,optPreenchidos,optRepetidos];
    for (let i = 0; i< opts.length; i++){
      select.appendChild(opts[i]);
    }

    sectionButtonsCol.appendChild(select);
  }  
}

function returnPython() {

  const { PythonShell } = require('python-shell');
  const path = require('path');

  const ops = {
    scriptPath: path.join(__dirname, '../../engine/'),
    args: [tableName.value]
  };

  const analise = new PythonShell('matrizXlsx.py', ops);

  analise.on('message', function(message){
    const data = message.split('|');

    for(let i = 0; i< data.length; i++){
      const newData = data[i].split(',');
      matriz.push(newData);
    }
    metadadoOpts(matriz);
  })

}

function openButton() {
  document.querySelector('.options').classList.toggle('invisible');
}
