window.onload = function(){
    var request = new XMLHttpRequest();
    request.open('GET', 'http://localhost:8000/battleball/board/1/game/', false);  // `false` makes the request synchronous
    request.send(null);

    if (request.status === 200) {
        json = JSON.parse(request.responseText);
    }
    arr = json.game.board;
    draw();
}

//These variables can be changed to create a bigger/smaller field
var field_width = 12;
var sqSize = 100;
var border = 25;
var long_row = 5;

//these variables should not be changed
var hsqSize = sqSize/2;
var short_row = long_row-1;

/*
var arr = [     ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'B', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E']      ];
*/

document.addEventListener("DOMContentLoaded", draw, false);

//This is the main function and will paint in the football field
function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');

    gameboard(ctx, arr);
    canvas.addEventListener("mousedown", getPosition, false);
  }
}

//Returns the coordinates of the mouse
function getPosition(event) {
    x = event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
    y = event.clientY + document.body.scrollTop + document.documentElement.scrollTop;
    clickpos = position(x, y)

    alert("x: " + clickpos.col + "  y: " + clickpos.row);
}

//This function will create a board with no pieces on it
function gameboard(ctx) {
    for (var i = 1; i <= (field_width-1); i+=2)
        for (var j = 0; j <= long_row; j++) move(i, j, arr[i][j], ctx);
    for (i = 2; i <= (field_width-1); i+=2)
        for (j = 0; j <= short_row; j++) move(i, j, arr[i][j], ctx);
    for (i = 0; i <= field_width; i+=field_width)
        for (j = 0; j <= long_row; j++) move(i, j, arr[i][j], ctx);

    for(i = 0; i < pieces; i++) move(i, -1, '0h', ctx);
    
    for(i=field_width-pieces+1; i<=field_width; i++) move(i, -1, '0a', ctx);

}

//This function will take in the desired spot and piece indicator to move the piece to that location
function move(col, row, ind, ctx) {
    ctx.strokeStyle = 'white';
    var team = ind.charAt(ind.length-1)
    if (col === 0 && ind =='E') ctx.fillStyle = '#09D';
    else if (col == field_width && ind =='E') ctx.fillStyle = '#F55';
    else if (ind == 'E') ctx.fillStyle = '#6C0';
    else if (ind == 'B') ctx.fillStyle = 'yellow';
    else if (ind == 'X') ctx.fillStyle = 'black';
    else if (team == 'h') ctx.fillStyle = 'blue';
    else if (team == 'a') ctx.fillStyle = 'red';

    var piece = coordinates(col, row);
    ctx.fillRect(border + piece.x, border + piece.y, sqSize, piece.size);
    ctx.strokeRect(border + piece.x, border + piece.y, sqSize, piece.size);
}

//This function will take in a row and column.
//The columns start from the left and the rows start from the bottom.
//The output is the x, y coordinates of the upper left pixel of the square and the size of the square
function coordinates(col, row) {
    var o = new Object({});
    o.x= sqSize*col;
    if(col%2 !== 0 || col === 0 || col === field_width || row < 0) {
        if(row==long_row) {
            o.y = 0;
            o.size = hsqSize;
        }
        else {
            o.y = -(row-short_row)*sqSize + hsqSize;
            if(row === 0) o.size = hsqSize;
            else o.size = sqSize;
        }
    }
    else {
        o.y = -(row-short_row)*sqSize;
        o.size = sqSize;
    }

    return o;
}

function position(posx, posy) {
    var o = new Object({});
    o.col = Math.floor((posx-border)/sqSize);
    var board_bottom = long_row*sqSize+border;
    var yfix = -(posy - border - long_row*sqSize);
    var edge_right = (field_width+1)*sqSize+border;
    if(posy <= board_bottom && posy >= border) {
        if(o.col%2 !== 0 || o.col === 0 || o.col === field_width) {
            if(yfix < hsqSize) o.row = 0;
            else o.row = Math.floor((yfix+hsqSize)/sqSize);
        }
        else o.row = Math.floor(yfix/sqSize);
    }
    else if (posy <= board_bottom+sqSize+hsqSize && posy >= board_bottom+hsqSize &&
              ((posx >= border && posx <=border+sqSize*pieces) ||
                (posx <= edge_right && posx >= edge_right - pieces*sqSize))
            ) o.row = -2;
    else o.row = -1;
    return o;
}
