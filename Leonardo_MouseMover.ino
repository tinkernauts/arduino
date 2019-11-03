// ######################################################################
// 
// Leonardo_MouseMover.ino - auto mouse mover for Arduino Leonardo
// https://www.arduino.cc/en/Main/Arduino_BoardLeonardo
// based on Longan Labs IRduino https://www.longan-labs.cc/1040001.html
//
// IRduino library https://github.com/Longan-Labs/IRduino
// IRduino documentation https://docs.longan-labs.cc/1040001/
// 
// Bart Spainhour <bart@tinkernauts.org>
//
// ######################################################################

// include libraries for mouse and irduino
#include <Mouse.h>
#include <IRDuino.h>
// also does a sub-include of Keyboard.h

// note: using irduino library for easy LED control.
// LEDs are wired to analog GPIO pins, so no PWM control of RGB
// options are Red, Green, Blue for each eye

// run this "setup()" section once at startup
void setup()
{
  // start mouse and IRDuino devices
  Mouse.begin();
  iRduino.begin();

  // flash green for good startup (250ms)
  iRduino.led(G1, 1);
  iRduino.led(G2, 1);
  delay(250);
  iRduino.releaseAll();
  iRduino.all_led_off();

  // pause one second after init
  // this can be longer for the oh-sh1t moment 
  // if you need to unplug
  delay(1000);  
}

// loop contents of "loop()" section forever
void loop()
{
  // vars for mouse movements
  int xMovePixels = 5; // consider some elaborate randomization?
  int yMovePixels = 5; // or trig functions?
  int responseDelay = 2; // de-bounce for mouse output

  // how long to cycle delay
  // 30 seconds default
  int pauseDelay = 30000;

  // to-do: put the green-flash into a loop
  delay(pauseDelay); // 1 of 3 default 30 seconds

  // flash green (500ms)
  iRduino.led(G1, 1);
  iRduino.led(G2, 1);
  delay(500);
  iRduino.all_led_off();

  delay(pauseDelay); // 2 of 3 default 30 seconds

  // flash green (500ms)
  iRduino.led(G1, 1);
  iRduino.led(G2, 1);
  delay(500);
  iRduino.all_led_off();

  delay(pauseDelay); // 3 of 3 default 30 seconds

  // flash green (500ms)
  iRduino.led(G1, 1);
  iRduino.led(G2, 1);
  delay(500);
  iRduino.all_led_off();
  delay(500);

  // to-do: put this into a loop
  // warning before mouse move
  // flash red 1 of 3 (500ms)
  iRduino.led(R1, 1);
  iRduino.led(R2, 1);
  delay(500);
  iRduino.all_led_off();
  delay(500);

  // flash red 2 of 3 (500ms)
  iRduino.led(R1, 1);
  iRduino.led(R2, 1);
  delay(500);
  iRduino.all_led_off();
  delay(500);

  // flash red 3 of 3 (500ms)
  iRduino.led(R1, 1);
  iRduino.led(R2, 1);
  delay(500);
  iRduino.all_led_off();
  delay(500);
  
  // release keyboard just in case
  iRduino.releaseAll();
  // move mouse
  Mouse.move(xMovePixels, yMovePixels, 0); // (x, y, wheel)
  delay(responseDelay);

  // flash blue for all clear
  iRduino.led(B1, 1);
  iRduino.led(B2, 1);
  delay(500);
  iRduino.all_led_off();
  iRduino.releaseAll();

  // return to top of loop section
}
