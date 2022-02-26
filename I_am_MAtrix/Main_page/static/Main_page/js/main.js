"use strict";

if(document.getElementById("past").firstElementChild){
  var pastEl = document.getElementById("past").firstElementChild;
  console.log(pastEl);
  pastEl.innerHTML = 'previous'.toUpperCase();
}
if(document.getElementById("future").firstElementChild){
  var futureEl = document.getElementById("future").firstElementChild;
  console.log(futureEl);
  futureEl.innerHTML = 'next'.toUpperCase();
}

function GetListOfLinks(){
  const getList = document.body.querySelector(".list_of_links").firstElementChild.querySelectorAll('a');
  return getList;
}
let listOfLinks = GetListOfLinks();
console.log(listOfLinks[0].href)
console.log(document.location.href);
for(let i = 0;i < listOfLinks.length;i++){
  if(listOfLinks[i].href != listOfLinks[0].href || listOfLinks[i].href != listOfLinks[listOfLinks.length - 1].href){
    if(listOfLinks[i].href == document.location.href){
      pastEl.href = listOfLinks[i-1].href;
      futureEl.href = listOfLinks[i+1].href;
    }
  }
  else if(listOfLinks[0].href == document.location.href){
    pastEl.href = listOfLinks[listOfLinks.length - 1].href;
    futureEl.href = listOfLinks[i+1].href;
  }
  else if(listOfLinks[listOfLinks.length - 1].href == document.location.href){
    pastEl.href = listOfLinks[i - 1].href;
    futureEl.href = listOfLinks[0].href;
  }
}


let a = window.innerWidth;
let b = window.innerHeight;
console.log(`width ${a}`);
console.log(`height ${b}`);
if(document.querySelector(".canvas") != null) {
  let canv = document.querySelectorAll(".canvas");
  for(let i of canv){
    i.getContext("2d");
    const data = {
        datasets: [{
            data: [10, 20, 30],
            backgroundColor:[
              '#E4556A',
              '#E4D394',
              '#67ACE4'
            ],
            borderColor:'white',
            borderWidth:5
        }],

        labels: [
            'Red',
            'Yellow',
            'Blue'
        ]
    };

    const config =  new Chart(i,{
      type: 'doughnut',
      data: data,
      options: {
        plugins: {
          legend: {
            title:{
              text:'Telegram Bot',
              display: true,
              font:{
                size:65,
                weight:'bold',
              }
            },
            labels:{
              boxWidth:100,
              font:{
                size:65,
                weight: 'bold'
              }
            }
          }
        }
      }
    })
  }
}
