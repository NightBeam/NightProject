'use strict';

class Graph{
    constructor(labels, data, backgroundColor,borderColor){
        this.labels = labels;
        this.data = data;
        this.backgroundColor = backgroundColor;
        this.borderColor = borderColor;
    }


    CreateDatasOfGraph(){
        let data = {
            datasets: [{
            data: this.data,
            backgroundColor: this.backgroundColor,
            borderColor: this.borderColor,
            borderWidth: 5,
        }],
        
        labels: this.labels,
        };
        return data;
    }
}

const requestToCanvasOfForms = document.querySelector('#canvasF');
const v1 = Number(requestToCanvasOfForms.getAttribute('v1'));
const v2 = Number(requestToCanvasOfForms.getAttribute('v2'));
const v3 = Number(requestToCanvasOfForms.getAttribute('v3'));
var data_1 = [v1,v2,v3] 
var labels_1 = ['Твердотельная','Полигональная','Скульптинг']
var backgroundColor_1 = ['rgba(85,192,191,0.4)','rgba(252,137,163,0.4)','rgba(114,185,237,0.4)']
var borderColor_1 = ['rgba(85,192,191,1)','rgba(252,137,163,1)','rgba(114,185,237,1)']
var graph_1 = new Graph(labels_1,data_1,backgroundColor_1,borderColor_1);

const config_1 = {
    type: 'doughnut',
    data: graph_1.CreateDatasOfGraph(),
    options: {
        maintainAspectRatio: false,
        plugins: {
            title:{
                display: true,
                text:'Форма',
                font:{
                    size:'80',
                    weight:'bold',
                    family:'monospace'
                }
            },
            legend: {
                display: false,
                position:'bottom',
                labels:{
                    boxHeight: 100,
                    boxWidth: 50,
                    font:{
                        size: 60,
                        weight: 'bold',
                        family:'monospace'
                    }
                }
            }
        }
    }
};

const ctx_1 = document.querySelector('#canvasF').getContext('2d');
let chart_1 = new Chart(ctx_1, config_1);


var data_2 = [60,20,30] 
var labels_2 = ['Твердотельная','Полигональная','Скульптинг']
var backgroundColor_2 = ['rgba(85,192,191,0.4)','rgba(252,137,163,0.4)','rgba(114,185,237,0.4)']
var borderColor_2 = ['rgba(85,192,191,1)','rgba(252,137,163,1)','rgba(50,185,237,1)']
var graph_2 = new Graph(labels_2,data_2,backgroundColor_2,borderColor_2);

const config_2 = {
    type: 'doughnut',
    data: graph_2.CreateDatasOfGraph(),
    options: {
        maintainAspectRatio: false,
        plugins: {
            title:{
                display: true,
                text:'Телеграм Бот',
                font:{
                    weight:'bold',
                    size:'80',
                    family:'monospace'
                }
            },
            legend: {
                display: false,
                position:'bottom',
                labels:{
                    boxHeight: 100,
                    boxWidth: 50,
                    font:{
                        size: 60,
                        weight: 'bold',
                        family:'monospace'
                    }
                }
            }
        }
    }
};

const ctx_2 = document.querySelector('#canvasTB').getContext('2d');
let chart_2 = new Chart(ctx_2, config_2);