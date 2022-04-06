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
var data_1 = for_data_1;
console.log(data_1);
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
                text:' Google Форма',
                font:{
                    size:'40',
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
                    size:'40',
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





var data_3 = [60,20,30] 
var labels_3 = ['Серийное производство','Видео игры и фильмы','макеты для материальных моделй']
var backgroundColor_3 = ['rgba(85,192,191,0.4)','rgba(252,137,163,0.4)','rgba(114,185,237,0.4)']
var borderColor_3 = ['rgba(85,192,191,1)','rgba(252,137,163,1)','rgba(50,185,237,1)']
var graph_3 = new Graph(labels_3,data_3,backgroundColor_3,borderColor_3);

const config_3 = {
    type: 'doughnut',
    data: graph_3.CreateDatasOfGraph(),
    options: {
        maintainAspectRatio: false,
        plugins: {
            title:{
                display: true,
                font:{
                    weight:'bold',
                    size:'40',
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

const ctx_3 = document.querySelector('#canvasFU').getContext('2d');
let chart_3 = new Chart(ctx_3, config_3);




var data_4 = [60,20,30] 
var labels_4 = ['Серийное производство','Видео игры и фильмы','макеты для материальных моделй']
var backgroundColor_4 = ['rgba(85,192,191,0.4)','rgba(252,137,163,0.4)','rgba(114,185,237,0.4)']
var borderColor_4 = ['rgba(85,192,191,1)','rgba(252,137,163,1)','rgba(50,185,237,1)']
var graph_4 = new Graph(labels_4,data_4,backgroundColor_4,borderColor_4);

const config_4 = {
    type: 'doughnut',
    data: graph_4.CreateDatasOfGraph(),
    options: {
        maintainAspectRatio: false,
        plugins: {
            title:{
                display: true,
                font:{
                    weight:'bold',
                    size:'40',
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

const ctx_4 = document.querySelector('#canvasTBU').getContext('2d');
let chart_4 = new Chart(ctx_4, config_4);