let seconds = 0;
let milliseconds = 0;

const Seconds = document.getElementById("seconds");
const milliSeconds = document.getElementById("milliseconds");

const Start = document.getElementById("start");
const Stop = document.getElementById("stop");
const Reset = document.getElementById("reset");

let intervalId;

const Delete = document.querySelector('#delete');
const All = document.querySelector('#all');

Start.onclick = function(){
    clearInterval(intervalId)
    intervalId = setInterval(Timer, 10)
}

function Timer(){
    milliseconds++;
    milliSeconds.textContent = milliseconds > 9 ? milliseconds : '0' + milliseconds    
    
    if(milliseconds > 99){
        seconds++;
        Seconds.textContent = seconds > 9 ? seconds : '0' + seconds
        milliseconds = 0
        milliSeconds = "00"
    }
}

Stop.onclick = function(){
    clearInterval(intervalId)
    Record();
}

Reset.onclick = function(){
    clearInterval(intervalId)
    milliseconds = 0;
    seconds = 0;
    milliSeconds.textContent = "00"
    Seconds.textContent = "00"
}

Delete.onclick = function(){
    deleted();
}

All.onclick = function(){
    checkAll();
}

function Record(){
    var tr = document.createElement("tr");
    var input = document.createElement("input");

    input.setAttribute("type","checkbox");
    input.setAttribute("class","check");

    var td01 = document.createElement("td");
    td01.appendChild(input);

    var td02 = document.createElement("td");
    td02.innerHTML = (seconds > 9 ? seconds : '0' + seconds) + ":" + (milliseconds > 9 ? milliseconds : '0' + milliseconds);

    tr.appendChild(td01);
    tr.appendChild(td02);

    document.querySelector('#body').appendChild(tr);
}

function checkAll(){
    var Box = document.querySelectorAll('#body .check');
    if(All.checked){
        for (var i in Box){
            Box[i].checked = true; 
        }
    }
    else{
        for (var i in Box){
            Box[i].checked = false; 
        }
    }
}

function deleted(){
    var list = document.getElementById('body');
    var checkbox = document.querySelectorAll('#body .check');

    for (var i in checkbox){
        if(checkbox[i].checked) list.removeChild(checkbox[i].parentNode.parentNode);
    }
}