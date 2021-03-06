"use strict";

if(document.getElementById("past").firstElementChild){
  var pastEl = document.getElementById("past").firstElementChild;
  console.log(pastEl);
  pastEl.innerHTML = '<'.toUpperCase();
}
if(document.getElementById("future").firstElementChild){
  var futureEl = document.getElementById("future").firstElementChild;
  console.log(futureEl);
  futureEl.innerHTML = '>'.toUpperCase();
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
    if(document.location.href == listOfLinks[1].href){
      pastEl.href = listOfLinks[i - 1].href;
      futureEl.href = listOfLinks[i + 2].href;
      break;
    }
    else if(document.location.href == listOfLinks[3].href){
      pastEl.href = listOfLinks[i - 2].href;
      futureEl.href = listOfLinks[i + 1].href;
      break;
    }
    else{
      pastEl.href = listOfLinks[i - 1].href;
      futureEl.href = listOfLinks[i + 1].href;
      break;
    }
  }
}
if( document.querySelectorAll(".video")){
  var video = document.querySelectorAll(".video");
}
class WorkWithInputCB{
  constructor(inputObj, workingObj){
    this.inputObj = inputObj;
    this.workingObj = workingObj;
  }

  windowHeight = window.innerHeight;
  headHeight = document.querySelector(".head").offsetHeight;
  activeCB = false;
  buttonLA = document.querySelector('.button_links')

  ShowMenu() {
    if (this.activeCB == false) {
      this.activeCB = true;
      let minusHeight = (this.windowHeight - this.headHeight)+ "px";
      this.workingObj.style.height = minusHeight;
      this.buttonLA.style.transform = 'rotate(360deg)';
      this.buttonLA.style.transitionDuration= '0.5s';
      this.workingObj.style.transitionDuration= '0.5s';
    } else {
      this.activeCB = false;
      this.workingObj.style.height = 5 + "px";
      this.buttonLA.style.transform = 'rotate(0deg)';
      this.buttonLA.style.transitionDuration= '0.5s'
      this.workingObj.style.transitionDuration= '0.5s';
    }
  }

  WorkWithTopOfHeader(){
    let nameOfPage = document.querySelector(".name_of_page");
    listOfLinkWorking.style.top = this.headHeight  + "px";
    nameOfPage.style.marginTop = this.headHeight + 80 +'px';
  }

}
var menuBurgerChecker = document.querySelector("#check-burger");
var listOfLinkWorking = document.querySelector(".list_of_links");
var workWithCB = new WorkWithInputCB(menuBurgerChecker, listOfLinkWorking);
workWithCB.WorkWithTopOfHeader();
