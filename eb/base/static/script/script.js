var xArray = [50,60,70,80,90,100,110,120,130,140,150];
var yArray = [7,8,8,9,9,9,10,11,14,14,15];

// Define Data
var data = [{
  x: xArray,
  y: yArray,
  mode: "lines",
  type: "scatter"
}];

// Define Layout
var layout = {
  xaxis: {range: [40, 160], title: "Square Meters"},
  yaxis: {range: [5, 16], title: "Price in Millions"},
  title: "House Prices vs Size"
};

const config = {
    displayModeBar: false, // this is the line that hides the bar.
  };
  
function cost(unit){
  if(unit<=100)
      return 0;
  else if(unit<=200){
    
      unit -= 100;
      return (unit*1.5)+20
  }
  else if(unit <=500){
      unit -= 200;
      return (unit*3)+200+30
  }
  else{
      unit -= 500;
      return (unit*6.6)+1730+50
  }
}

// Display using Plotly
Plotly.newPlot("myPlot", data, layout, config);
domine = document.getElementById('domine').innerText;
var vul, i = 0,table = document.getElementById('data');
$.getJSON('/api/getmt-613:0',(json)=>{
  for(let i = 0; i<Object.create(json).length;i++){
    let date = new Date(json[i]['date']);
  let unit = json[i]['unit'];
  let row = table.insertRow(i+1);
  row.insertCell(0).innerText = date.getDate()+'/'+(date.getMonth()+1)+'/'+date.getFullYear();
  row.insertCell(1).innerText = unit;
  row.insertCell(2).innerText = cost(unit);
  if(i == 0){
    row.insertCell(3).innerText=0
    row.insertCell(4).innerText=0
    row.insertCell(5).innerText=0 
  }
  else{
    let days = (date-new Date(json[i-1]['date']))/(1000 * 60 * 60 * 24);
    row.insertCell(3).innerText=days
    row.insertCell(4).innerText=Math.round((unit-json[i-1]['unit'])/days*1000)/1000
    row.insertCell(5).innerText= Math.round(cost(unit)/days*1000)/1000
  }
  }
  })


let  count =0;
for(i in vul){
  

}

console.log(domine)