//int LED = 13; 
#include <Servo.h>
Servo myservo;
int pos = 0;

void setup() {
  // put your setup code here, to run once:
//pinMode(LED,OUTPUT);
myservo.attach(9);

}

void loop() {
  // put your main code here, to run repeatedly:
//digitalWrite(LED,1);
//delay(30);
//digitalWrite(LED,0);
//delay(15);
  for (pos = 0; pos <= 180; pos +=1){
  myservo.write(pos);
  delay(3000);
  }
  for (pos = 180; pos >= 0; pos -=1){
  myservo.write(pos);
  delay(3000);
  }
}

