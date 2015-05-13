window.onload = function(){
    //var request = new XMLHttpRequest();
    //request.open('GET', 'http://localhost:8000/battleball/board/1/game/', false);  // `false` makes the request synchronous
    //request.send(null);

    //if (request.status === 200) {
    //    json = JSON.parse(request.responseText);
    //}
    //arr = json.game.board;
    draw();
};

//These variables can be changed to create a bigger/smaller field
var field_width = 12,
    sqSize = 100,
    border = 25,
    long_row = 5,
    selectedPiece = null,
    ctx = null,
    canvas = null,
    HOME_TEAM = 0,
    AWAY_TEAM = 1,
    tackle = false,
    pieces = new Image(),
    football = new Image(),
    moves = -1,
    home_pieces = 2,
    away_pieces = 2,
    home_score = 0,
    away_score = 0,
    touchdown = false,
    fumble = false,
    fumble_pos = 0;
    currentTurn = HOME_TEAM,
    endGame = false;

//these variables should not be changed
var hsqSize = sqSize/2,
    short_row = long_row-1;


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

var home = [
                {"type": 0,
                 "injured": 0,
                 "name": "running back",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 8,
                 "position": {"xpos": 2, "ypos": 1}},
                {"type": 1,
                 "injured": 0,
                 "name": "lineman",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 1,
                 "position": {"xpos": 2, "ypos": 3}}
            ];
var away =  [
                {"type": 0,
                 "injured": 0,
                 "name": "running back",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 8,
                 "position": {"xpos": 10, "ypos": 3}},
                {"type": 1,
                 "injured": 0,
                 "name": "lineman",
                 "psize": 1,
                 "has_ball": false,
                 "roll_size": 1,
                 "position": {"xpos": 10, "ypos": 1}}
            ];


document.addEventListener("DOMContentLoaded", draw, false);

//This is the main function and will paint in the football field
function draw() {
    canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        ctx = canvas.getContext('2d');
        pieces.src = '/static/battleball/images/pieces.png';
        gameboard();
        canvas.addEventListener("click", getPosition, false);
        canvas.addEventListener("dblclick", roll_dice, false);
        print_turn();
    }
    else alert("Canvas not supported!");
    //set score
   $("#score").text(home_score + ' - ' + away_score);
}

function print_turn() {
    clear_print_turn();
    var turn;
    var mytext = "Turn: ";
    if (currentTurn === 0) {
        turn = "Home Team";
        ctx.fillStyle="blue";
    }
    else {
        turn = "Away Team";
        ctx.fillStyle="red";
    }
    mytext += turn;
    ctx.font = "30px Arial";
    ctx.fillText(mytext, border, long_row*sqSize+sqSize);
}

function clear_print_turn() {
    ctx.fillStyle = "white";
    ctx.fillRect(border, long_row*sqSize+hsqSize,300,100);
}

function print_move() {
    clear_print_move();
    var mytext = "Moves left: ";
    if (currentTurn === 0) ctx.fillStyle="blue";
    else ctx.fillStyle="red";
    mytext += moves;
    ctx.font = "30px Arial";
    ctx.fillText(mytext, border+400, long_row*sqSize+sqSize);
}

function clear_print_move() {
    ctx.fillStyle = "white";
    ctx.fillRect(border+400, long_row*sqSize+hsqSize,300,100);
}

//Returns the coordinates of the mouse
function getPosition(event) {
    if(endGame === false) {
        var rect = canvas.getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        
        //select block that has been clicked
        var clickedBlock = position(x, y);
        print_turn();
        // Check to see if block contains a piece
        if (selectedPiece === null) {
            checkIfPieceClicked(clickedBlock);
        }
        else if (tackle) processTackle(clickedBlock);
        else if (fumble) processFumble(clickedBlock);
        // if there is a selected piece, move it
        else if (moves >= 0) {
            print_move();
            processMove(clickedBlock);
        }
        else {
            removeSelection(selectedPiece);
            checkIfPieceClicked(clickedBlock);
        }
    }
}

function roll_dice(event) {
    if(selectedPiece !== null && moves === -1 && endGame === false) {
        moves = roll(selectedPiece.roll_size);
        print_move();
    }
}

function roll(roll_size) {
    /*
    This function creates a random number from 1- roll size
   */
    var proll = Math.floor((Math.random() * roll_size) + 1);
    return proll;
}

//This function will create a board
function gameboard() {
    // fill in long rows
    var i, j;
    for (i = 1; i <= (field_width-1); i+=2)
        for (j = 0; j <= long_row; j++) fill_space(i, j, arr[i][j]);
    // fill in short rows
    for (i = 2; i <= (field_width-1); i+=2)
        for (j = 0; j <= short_row; j++) fill_space(i, j, arr[i][j]);
    // fill in endzones
    for (i = 0; i <= field_width; i+=field_width)
        for (j = 0; j <= long_row; j++) fill_space(i, j, arr[i][j]);

    for (i = 0; i<home.length; i++) {
        if (home[i].injured != 2) {
            arr[home[i].position.xpos][home[i].position.ypos] =  home[i].type+'h';
            fill_space(home[i].position.xpos, home[i].position.ypos, home[i].type+'h');
        }
    }

    for (i = 0; i<away.length; i++) {
        if (away[i].injured != 2) {
            arr[away[i].position.xpos][away[i].position.ypos] =  i+'a';
            fill_space(away[i].position.xpos, away[i].position.ypos, i+'a');
        }
    }
}


function fill_space(col, row, square_identifier) {
    /* 
   This function will take in the desired spot and piece indicator 
   and create a space

   Input: col = column that the square will will occupy
          row = row that the square will occupy
          square_identifier = E, X, B, #a, identifies what type of square
                               is created

    Output: Canvas Generated baord

    */
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 1;
    var team = square_identifier.charAt(square_identifier.length-1);
    var ind = square_identifier.charAt(0);
    // Select color of space
    if (col === 0 && square_identifier === 'E') ctx.fillStyle = '#09D';
    else if (col == field_width && square_identifier === 'E') ctx.fillStyle = '#F55';
    else if (square_identifier === 'E' || square_identifier === 'B') ctx.fillStyle = '#6C0';
    else if (square_identifier === 'X') ctx.fillStyle = 'black';
    else if (team === 'h'){ 
        ctx.fillStyle = 'blue';
        }
    else if (team === 'a'){
         ctx.fillStyle = 'red';
         }
    


    // get pieces coordinate and size
    var piece = coordinates(col, row);

    //place space on board
    ctx.fillRect(border + piece.x, border + piece.y, sqSize, piece.size);
    ctx.strokeRect(border + piece.x, border + piece.y, sqSize, piece.size);
    //place sprite
    if(square_identifier === 'B'){
        ctx.drawImage(pieces,0,195,120,128 ,border + piece.x, border + piece.y, sqSize, piece.size);
    }
    if(square_identifier === 'X'){
        ctx.drawImage(pieces,120,195,92,105 ,border + piece.x, border + piece.y, sqSize, piece.size);
    }
    if (team === 'h'){
        if(home[ind].has_ball){
            ctx.drawImage(pieces,3*66,2*66,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
        }
        else{
        ctx.drawImage(pieces,0,2*66,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
        }
    }
    else if (team === 'a'){
        if(away[ind].has_ball){
            ctx.drawImage(pieces,3*66,60,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
        }
        else{
        ctx.drawImage(pieces,1*66,60,66,66,border + piece.x, border + piece.y, sqSize, piece.size);
        }
    }
}

function coordinates(col, row) {
    /*
    This function will take in a row and column.
    The columns start from the left and the rows start from the bottom.
    The output is the x, y coordinates of the upper left pixel of the square and the size of the square
    */
    var o = new Object({});
    o.x= sqSize*col;
    // If enzone or long row
    if(col%2 !== 0 || col === 0 || col === field_width || row < 0) {
        // if top space
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
    // If short row
    else {
        o.y = -(row-short_row)*sqSize;
        o.size = sqSize;
    }

    return o;
}

function position(posx, posy) {
    /*
    This function returns the coordinate of the space selected
    */
    var o = new Object({});

    // Gets y coordinate
    o.col = Math.floor((posx-border)/sqSize);

    var board_bottom = long_row*sqSize+border;
    var yfix = -(posy - border - long_row*sqSize);
    if(posy <= board_bottom && posy >= border) {
        if(o.col%2 !== 0 || o.col === 0 || o.col === field_width) {
            if(yfix < hsqSize) o.row = 0;
            else o.row = Math.floor((yfix+hsqSize)/sqSize);
        }
        else o.row = Math.floor(yfix/sqSize);
    }
    else o.row = -1;
    return o;
}


function checkIfPieceClicked(clickedBlock) {
    var pieceAtBlock = getPieceAtBlock(clickedBlock);
    if (pieceAtBlock !== null && moves === -1)
        selectPiece(pieceAtBlock);
}

function getPieceAtBlock(clickedBlock) {
    var team;
    if(tackle){
        team = (currentTurn === HOME_TEAM ? away : home);
    }
    else{
        team = (currentTurn === HOME_TEAM ? home : away);
    }

    return getPieceAtBlockForTeam(team, clickedBlock);
}

function getPieceAtBlockForTeam(teamOfPieces, clickedBlock) {
    /*
    Input: teamOfPieces = the team of the piece we are checking
           clickedBlock = coordinates of the clicked block
    Returns the piece located at a space, otherwise returns null
    */
    var curPiece = null,
        iPieceCounter = 0,
        pieceAtBlock = null;

    for (iPieceCounter = 0; iPieceCounter < teamOfPieces.length; iPieceCounter++) {

        curPiece = teamOfPieces[iPieceCounter];

        if (curPiece.injured === 0 && curPiece.position.xpos === clickedBlock.col &&
            curPiece.position.ypos === clickedBlock.row) {
                curPiece.itr = iPieceCounter;
                pieceAtBlock = curPiece;
                iPieceCounter = teamOfPieces.length;
        }
    }

    return pieceAtBlock;
}


function selectPiece(pieceAtBlock) {
    /*
    Input: pieceAtBlock = piece that is at the selected block

    Output: Global variable 'selectedPiece' set to pieceAtBlock
            white border areound the piece
    */
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 4;

    var piece = coordinates(pieceAtBlock.position.xpos, pieceAtBlock.position.ypos);
    ctx.strokeRect(border + piece.x+2, border + piece.y+2, sqSize-4, piece.size-4);

    // selected piece is global
    selectedPiece = pieceAtBlock;
}

function removeSelection(selectedPiece) {
    /*
    Input: selectedPiece = global selectedPiece variable

    Functionality: Removes white border from selected piece
    */
    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos,
        arr[selectedPiece.position.xpos][selectedPiece.position.ypos]);
    // add line to draw sprite
}

function processMove(clickedBlock) {
    /* 
       When a piece is selected this function checks whether
       There is a piece at the location clicked
       if there is it removes the current selection and selects the next piece
       Otherwise if the move is allowed, the piece is moved
    */
    var pieceAtBlock = getPieceAtBlock(clickedBlock);

    if (pieceAtBlock !== null) {
        removeSelection(selectedPiece);
        checkIfPieceClicked(clickedBlock);
    }

    else if (canSelectedMoveToBlock(selectedPiece.position, clickedBlock) === true)
        //move(clickedBlock.col, clickedBlock.row, arr[clickedBlock.col][clickedBlock.row]);
        movePiece(clickedBlock);
}


function canSelectedMoveToBlock(position, clickedBlock)
{
    /*
    Input: position = position of selectedPiece or ball
           clickedBlock = block selected to move to

    Output: bNextRowEmpty = True/False depending on whether a piece can move to clicked block
    */
    var occupied = surroundingSpaces(position);
    var occounter,  bNextRowEmpty;
    var nextMove=[];
    
    for(occounter=0; occounter<occupied.length; occounter++) {
        if (occupied[occounter].row == clickedBlock.row &&
            occupied[occounter].col == clickedBlock.col &&
            occupied[occounter].col>=0 && occupied[occounter].col<=field_width) {
            nextMove = occupied[occounter];
        }
    }
    // Ensure next space is empty or has a ball on it 
    if(arr[nextMove.col][nextMove.row]=='E' || arr[nextMove.col][nextMove.row] == 'B')
        bNextRowEmpty = true;
    else bNextRowEmpty = false;
    console.log(bNextRowEmpty);
    return bNextRowEmpty;
}

function adjacentEnemy(selectedPiece, clickedBlock) {
    /*
    Input: selectedPiece = Global selectedPiece variable
           clickedBlock = coordinates of the clicked block selected

    Outpu: enemy: boolean that's true if there is an enemy at the clicked block, false otherwise
    */
    var enemy,
        occupied = surroundingSpaces(selectedPiece.position),
        occounter, nextMove=[];
    
    nextMove.col = selectedPiece.position.xpos;
    nextMove.row = selectedPiece.position.ypos;

    for(occounter=0; occounter<occupied.length; occounter++) {
        if (occupied[occounter].row == clickedBlock.row &&
            occupied[occounter].col == clickedBlock.col &&
            occupied[occounter].col>=0 && occupied[occounter].col<=field_width) {
            nextMove = occupied[occounter];
        }
    }
    var ind = arr[selectedPiece.position.xpos][selectedPiece.position.ypos],
        cur_team = ind.charAt(ind.length-1),
        nextInd = arr[nextMove.col][nextMove.row],
        nextSpaceTeam = nextInd.charAt(nextInd.length-1);
    // Ensure next space is empty or has a ball on it ]
    if(nextSpaceTeam != cur_team)
        enemy = true;
    else enemy = false;
    return enemy;
}


function movePiece(clickedBlock) {
    /*

    Input: clickedBlock = coordinates of the block that have been clicked

    This function moves the selected piece to the clickedBlock onthe canvas and global variable arr
    */
    var ind = arr[selectedPiece.position.xpos][selectedPiece.position.ypos],
        cur_team = ind.charAt(ind.length-1);
        console.log(cur_team);
    if(arr[clickedBlock.col][clickedBlock.row] === 'B'){
        pickupBall(selectedPiece);
    }
    // Clear the block in the original position
    fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos, 'E');
    // fill next space
    fill_space(clickedBlock.col, clickedBlock.row, ind);
    
    
    //update game board
    arr[clickedBlock.col][clickedBlock.row] = ind;
    arr[selectedPiece.position.xpos][selectedPiece.position.ypos] = 'E';
    
    moves-=1;
    print_move();   

    // update piece object to match board status, possibly it's own function later
    var team = (currentTurn === AWAY_TEAM ? away : home);

    team[selectedPiece.itr].position.xpos = clickedBlock.col;
    team[selectedPiece.itr].position.ypos = clickedBlock.row;

    
    var occupied = surroundingSpaces(selectedPiece.position);
    for(var i = 0; i < occupied.length; i++){
        var space = occupied[i];
        console.log(space);        
        var adj_ind = arr[space.col][space.row];
        console.log(adj_ind);
        if(adj_ind !== 'E' && adj_ind !== 'B' && adj_ind !== 'X'){
            team = adj_ind.charAt(adj_ind.length-1);
            console.log(team); 
            if(team !== cur_team){
                tackle = true;
            }
        }
    }

    if (currentTurn === HOME_TEAM && selectedPiece.has_ball === true && clickedBlock.col === field_width)
        processTouchdown(HOME_TEAM);

    else if (currentTurn === AWAY_TEAM && selectedPiece.has_ball === true && clickedBlock.col === 0)
        processTouchdown(AWAY_TEAM);

    if(tackle === false && moves === 0 && touchdown === false && fumble === false) {
        clear_print_move();
        selectedPiece = null;
        moves = -1;
        if (home_pieces === 0) currentTurn = AWAY_TEAM;
        else if (away_pieces === 0) currentTurn = HOME_TEAM;
        else currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
        print_turn();
    }
}

function surroundingSpaces(position){
    /* 

    Input: position = coordinates {xpos: x, ypos: y} 
    
    This function returns a list of the surrounding spaces
    relative to the selected piece
    */
    var col = position.xpos,
        row = position.ypos,
        u={}, d={}, ul={}, dl={}, ur={}, dr={}, l={}, r={},
        occupied=[];
    d.col = u.col = col;
    ul.col = dl.col = l.col = col-1;
    ur.col = dr.col = r.col = col+1;
    d.row = row-1;
    u.row = row+1;
    // Push only appropriate spots
    if(col === 0) {
        r.row = row;
        ur.row = row+1;
        dr.row = row-1;
        if(row === 0) occupied.push(u, ur, r);
        else if(row == long_row) occupied.push(d, r, dr);
        else occupied.push(u, ur, r, dr, d);
    }
    else if(col == field_width) {
        l.row = row;
        ul.row = row+1;
        dl.row = row-1;
        if(row === 0) occupied.push(u, l, ul);
        else if (row == long_row) occupied.push(d, l, dl);
        else occupied.push(u, ul, l, dl, d);
    }
    else if(col == 1) {
        l.row = ur.row = row;
        ul.row = row+1;
        dl.row = dr.row = row-1;
        if(row === 0) occupied.push(l, ul, u, ur);
        else if (row == long_row) occupied.push(l, dl, d, dr);
        else occupied.push(u, ul, l, dl, d, dr, ur);
    }
    else if(col == field_width-1) {
        ul.row = r.row = row;
        dl.row = dr.row = row-1;
        ur.row =row+1;
        if(row === 0) occupied.push(ul, u, ur, r);
        else if (row == long_row) occupied.push(dl, d, dr, r);
        else occupied.push(u, ul, dl, d, dr, r, ur);
    }
    else if(col%2 === 0) {
        ul.row = ur.row = row+1;
        dl.row = dr.row = row;
        if(row === 0) occupied.push(dl, ul, u, ur, dr);
        else if(row == short_row) occupied.push(ul, dl, d, dr, ur);
        else occupied.push(u, ul, dl, d, dr, ur);
    }
    else if(col%2 !== 0) {
        ul.row = ur.row = row;
        dl.row = dr.row = row-1;
        if(row === 0) occupied.push(ul, u, ur);
        else if(row == long_row) occupied.push(dl, d, dr);
        else occupied.push(u, ul, dl, d, dr, ur);
    }
    return occupied;
}

function pickupBall(piece){
    // This function allows a piece to pick up
    // the game ball
    piece.has_ball = true;
}

function processTackle(clickedBlock){
    //This function checks whether the clicked block has an enemy piece
    // Then resolves the tackle
    // updates field

    var enemy_piece = getPieceAtBlock(clickedBlock),
        neighbor = adjacentEnemy(selectedPiece, clickedBlock);
    if(enemy_piece !== null && neighbor === true){
        var tackle_roll = roll(selectedPiece.roll_size),
            defend_roll = roll(enemy_piece.roll_size);
        alert('your piece rolled a ' + tackle_roll + ' the opposing team rolled a ' + defend_roll);
        //if tackling piece wins
        if(tackle_roll < defend_roll){
            if(tackle_roll === 1){
                enemy_piece.injured = 2;
            }
            if(enemy_piece.has_ball === true) {
                selectedPiece.has_ball = true;
                enemy_piece.has_ball = false;
                fill_space(selectedPiece.position.xpos, selectedPiece.position.ypos,
                    arr[selectedPiece.position.xpos][selectedPiece.position.ypos]);
            }
            enemy_piece.injured = 1;
            fill_space(enemy_piece.position.xpos,enemy_piece.position.ypos, 'X');
            arr[clickedBlock.col][clickedBlock.row] = 'X';
            removePlayer(false);
        }

         //if defending piece wins
        else if(tackle_roll > defend_roll){
            if(defend_roll === 1){
                selectedPiece.injured = 2;
            }
            if(selectedPiece.has_ball === true) {
                enemy_piece.has_ball = true;
                selectedPiece.has_ball = false;
                fill_space(enemy_piece.position.xpos, enemy_piece.position.ypos,
                    arr[enemy_piece.position.xpos][enemy_piece.position.ypos]);
            }
            selectedPiece.injured = 1;
            fill_space(selectedPiece.position.xpos,selectedPiece.position.ypos, 'X');
            arr[selectedPiece.position.xpos][selectedPiece.position.ypos] = 'X';
            removePlayer(true);
        }
        
        else {
            if(defend_roll === 1){
                selectedPiece.injured = 2;
                enemy_piece.injured = 2;
            }
            else {
                selectedPiece.injured = 1;
                enemy_piece.injured = 1;
                }
            fill_space(selectedPiece.position.xpos,selectedPiece.position.ypos, 'X');
            fill_space(enemy_piece.position.xpos,enemy_piece.position.ypos, 'X');
            arr[clickedBlock.col][clickedBlock.row] = 'X';
            arr[selectedPiece.position.xpos][selectedPiece.position.ypos] = 'X';
            if(selectedPiece.has_ball || enemy_piece.has_ball){
                fumble = true;
                if(selectedPiece.has_ball === true){ 
                    fumble_pos = selectedPiece.position;
                    currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
                    print_turn();
                }
                else{ 
                    fumble_pos = enemy_piece.position;
                }
            }            
            removePlayer(true);
            removePlayer(false);
        }

        tackle = false;
        moves = -1;
        clear_print_move();
        if(!fumble){            
            selectedPiece = null;
            if (home_pieces === 0) currentTurn = AWAY_TEAM;
            else if (away_pieces === 0) currentTurn = HOME_TEAM;
            else currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
            print_turn();
        }
        
    }
}

function processTouchdown (team) {
    var i;
    if (team === HOME_TEAM) home_score++;
    else if (team === AWAY_TEAM) away_score++;

    if (home_score == 2) processEndGame(HOME_TEAM);
    else if (away_score == 2) processEndGame(AWAY_TEAM);

    else {
        arr = [     ['E', 'E', 'E', 'E', 'E', 'E'],
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

        home[0].position.xpos = 2;
        home[0].position.ypos = 1;
        home[1].position.xpos = 2;
        home[1].position.ypos = 3;
        away[0].position.xpos = 10;
        away[0].position.ypos = 1;
        away[1].position.xpos = 10;
        away[1].position.ypos = 3;

        for (i = 0; i<home.length; i++) {
            if(home[i].injured == 1) home[i].injured = 0;
            else if(home[i].injured == 2) {
                home[i].position.xpos = -1;
                home[i].position.ypos = -1;
            }
            home[i].has_ball = false;
        }

        for (i = 0; i<away.length; i++) {
            if(away[i].injured == 1) away[i].injured = 0;
            else if(away[i].injured == 2) {
                away[i].position.xpos = -1;
                away[i].position.ypos = -1;
            }
            away[i].has_ball = false;
        }
        
        home_pieces = 2;
        away_pieces = 2;
        moves = 0;
        currentTurn = ((home_score+away_score+1)%2 === 0 ? AWAY_TEAM : HOME_TEAM);
        draw();
    }
}

function processFumble(clickedBlock) {
    
    console.log('fumble function');
    // Can the ball be placed on the current block
    if(canSelectedMoveToBlock(fumble_pos, clickedBlock)){
        
        arr[clickedBlock.col][clickedBlock.row] = 'B';
        fill_space(clickedBlock.col,clickedBlock.row,'B');

        // Decide whose turn is next
        if(!selectedPiece.has_ball){
            currentTurn = (currentTurn === AWAY_TEAM ? HOME_TEAM : AWAY_TEAM);
            }
        // Reset Necessary variables to start turn
        fumble = false;
        selectedPiece.has_ball = false;
        selectedPiece = null;
        print_turn();
    }
}

function removePlayer(loser){
    /* This function will decrease
       the number of players on the loser's team*/

    if(loser){
        if(currentTurn == HOME_TEAM) home_pieces -= 1;
        else away_pieces -= 1;
    }
    else{
        if(currentTurn == AWAY_TEAM) home_pieces -= 1;
        else away_pieces -= 1;
    }
}

function processEndGame(team) {
    clear_print_turn();
    clear_print_move();
    endGame = true;
    var winner;
    if (team == HOME_TEAM){
        winner = "Home Team";
        ctx.fillStyle="blue";
    }

    else if (team == AWAY_TEAM) {
        winner = "Away Team";
        ctx.fillStyle="red";
    }

    winner += " Wins!";
    ctx.font = "30px Arial";
    ctx.fillText(winner, border, long_row*sqSize+sqSize);
}