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
  if(document.location.href == listOfLinks[0].href || document.location.href == listOfLinks[listOfLinks.length - 1].href){
    if(listOfLinks[0].href == document.location.href){
      console.log(listOfLinks[i].href);
      pastEl.href = listOfLinks[listOfLinks.length - 1].href;
      futureEl.href = listOfLinks[i+1].href;
      break;
    }
    else if(listOfLinks[listOfLinks.length - 1].href == document.location.href && listOfLinks[listOfLinks.length - 1].href == listOfLinks[i].href){
      pastEl.href = listOfLinks[i - 1].href;
      futureEl.href = listOfLinks[0].href;
      break;
    }
  }
  else if(document.location.href == listOfLinks[i].href ){
    console.log(listOfLinks[i].href);
    pastEl.href = listOfLinks[i - 1].href;
    futureEl.href = listOfLinks[i + 1].href;
    break;
  }
}




let a = window.innerWidth;
let b = window.innerHeight;
console.log(`width ${a}`);
console.log(`height ${b}`);

var menuBurgerChecker = document.querySelector("#check-burger");
if(menuBurgerChecker.checked == true){
  console.log(menuBurgerChecker.checked);
}
console.log(menuBurgerChecker.checked);


