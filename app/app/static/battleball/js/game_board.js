window.onload = function(){
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


var arr = [     ['E', 'E', 'E', 'E', 'E', 'E'],
                ['0h', 'E', 'E', '1h', 'E', 'E'],
                ['E', '2h', 'E', '4h', 'E'],
                ['6h', 'E', '9h', 'E', '10h', 'E'],
                ['E', 'E', 'E', 'E', 'X'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'B', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['6a', 'E', '9a', 'E', '10a', 'E'],
                ['E', '2a', 'E', '4a', 'E'],
                ['Oa', 'E', 'E', '1a', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E', 'E']      ];


//This is the main function and will paint in the football field
function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');

    gameboard(ctx, arr);
  }
}

//This function will create a board with no pieces on it
function gameboard(ctx) {
    for (var i = 1; i <= (field_width-1); i+=2)
        for (var j = 0; j <= long_row; j++) move(i, j, arr[i][j], ctx);
    for (i = 2; i <= (field_width-1); i+=2)
        for (j = 0; j <= short_row; j++) move(i, j, arr[i][j], ctx);
    for (i = 0; i <= field_width; i+=field_width)
        for (j = 0; j <= long_row; j++) move(i, j, arr[i][j], ctx);

}
//This function will take in a row and column.
//The columns start from the left and the rows start from the bottom.
//The output is the x, y coordinates of the upper left pixel of the square and the size of the square
function coordinates(col, row) {
  var o = new Object({});
    o.x= sqSize*col;
    if(col%2 !== 0 || col === 0 || col === field_width) {
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