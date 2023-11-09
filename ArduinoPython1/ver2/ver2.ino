#include <Servo.h>

Servo servoBase;
Servo servoHombro;
Servo servoCodo;
Servo servoPinza;

String msg;
int pos = 0;

int homeBase = 90;
int homeHombro = 130;
int homeCodo = 180;
int homePinza = 0;

void setup() {
  servoBase.attach(2);
  servoHombro.attach(3);
  servoCodo.attach(4);
  servoPinza.attach(5);
  Serial.begin(9600);

  servoBase.write(homeBase);
  servoHombro.write(homeHombro);
  servoCodo.write(homeCodo);
  servoPinza.write(homePinza);
}

void loop() {
  if (Serial.available() > 0) {
    msg = Serial.readStringUntil('\n');
    
    if (msg.startsWith("s1")) {
      String msgAux = msg.substring(2, msg.length());
      pos = msgAux.toInt();
      servoBase.write(pos);
    }

    if (msg.startsWith("s2")) {
      String msgAux = msg.substring(2, msg.length());
      pos = msgAux.toInt();
      servoHombro.write(pos);
    }

    if (msg.startsWith("s3")) {
      String msgAux = msg.substring(2, msg.length());
      pos = msgAux.toInt();
      servoCodo.write(pos);
    }

    if (msg.startsWith("s4")) {
      String msgAux = msg.substring(2, msg.length());
      pos = msgAux.toInt();
      servoPinza.write(pos);
    }
  }
  delay(1);
}
