// ######################################################################
// 
// arduino_randompicker.ino - demo to use pseudo-random number
// generation combined with floating analog pin values to pick
// sets of "game" numbers.
//
// Currently configured for 5 + 1 picks ("P0werB4ll")
// Picks #1 - #5 uses numbers 1 - 69
// Pick #6 uses numbers 1 - 26
// 
// Bart Spainhour <bart@tinkernauts.org>
//
// ######################################################################

void setup(){

  // open serial port at 9600 baud
  Serial.begin(9600);

  // print header for formatting
  Serial.println();
  Serial.println("|-------------------------------|");
}

void loop() {

// return 5 sets of results 
  for (int i=0; i <= 4; i++){
    
    top:
    // flush random number vars
    int randNumber0 = NULL;
    int randNumber1 = NULL;
    int randNumber2 = NULL;
    int randNumber3 = NULL;
    int randNumber4 = NULL;
    int randNumber5 = NULL;

    // generate randNumber0
    number0:

    // reset random seed
    //cycles through all 6 "floating" 
    //unused analog pins for entropy
    randomSeed(analogRead(millis()%6));

    //pick number 0
    randNumber0 = random(1,70);

    // generate randNumber1
    number1:

    // reset random seed 
    randomSeed(analogRead(millis()%6));

    //pick number 1
    randNumber1 = random(1,70);

    // check for duplicate
    if (randNumber1 == randNumber0)
    {goto number1;}

    // generate randNumber2
    number2:

    // reset random seed 
    randomSeed(analogRead(millis()%6));

    //pick number 2
    randNumber2 = random(1,70);

    // check for duplicate
    if (randNumber2 == randNumber1 || randNumber2 == randNumber0)
    {goto number2;}

    // generate randNumber3
    number3:

    // reset random seed 
    randomSeed(analogRead(millis()%6));

    //pick number 3
    randNumber3 = random(1,70);

    // check for duplicate
    if (randNumber3 == randNumber2 || randNumber3 == randNumber1 || randNumber3 == randNumber0)
    {goto number3;}

    // generate randNumber4
    number4:

    // reset random seed 
    randomSeed(analogRead(millis()%6));

    //pick number 4
    randNumber4 = random(1,70);

    // check for duplicate
    if (randNumber4 == randNumber3 || randNumber4 == randNumber2 || randNumber4 == randNumber1 || randNumber4 == randNumber0 )
    {goto number4;}

    // generate randNumber5
    number5:

    // reset random seed 
    randomSeed(analogRead(millis()%6));

    //pick number 5
    randNumber5 = random(1,27);

    // text formatting for printing
    String strPickOne = String(randNumber0);
    String strPickTwo = String(randNumber1);
    String strPickThree = String(randNumber2);
    String strPickFour = String(randNumber3);
    String strPickFive = String(randNumber4);
    String strPickSix = String(randNumber5);

    // add leading spaces for single-digit numbers
    if (strPickOne.length() == 1 )
    {strPickOne = " " + strPickOne;}
    if (strPickTwo.length() == 1 )
    {strPickTwo = " " + strPickTwo;}
    if (strPickThree.length() == 1 )
    {strPickThree = " " + strPickThree;}
    if (strPickFour.length() == 1 )
    {strPickFour = " " + strPickFour;}
    if (strPickFive.length() == 1 )
    {strPickFive = " " + strPickFive;}
    if (strPickSix.length() == 1 )
    {strPickSix = " " + strPickSix;}

    // print result to serial 
    String strResult;
    strResult ="| " + strPickOne + " - " + strPickTwo + " - " + strPickThree + " - " + strPickFour + " - " + strPickFive + "  |  " + strPickSix + " |";
    Serial.println(strResult);
    Serial.println("|-------------------------------|");        
  }
  
  Serial.println();
  
  // wait 1 day (60*60*24)*1000
  delay(86400000);
  
}
