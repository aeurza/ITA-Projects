#include <Servo.h> //Biblioteca para los servomotores
 // Creamos el objeto para cada Servomotor
Servo cuerpo; 
Servo hombro;
Servo brazo;
Servo mano1;
Servo mano2;
Servo mano3;
Servo pinza;
String msg; //Variable para recibir mensaje
int pos = 0; //Variable de posicion para los servos
// Variables de HOME para los servos
int home_cero = 0; 
int home_hombro = 130;
int home_brazo = 180;
int home_mano1 = 90;

void setup() {
  //Asignamos cada servomotor a su PIN
  cuerpo.attach(2);
  hombro.attach(3);
  brazo.attach(4);
  mano1.attach(5);
  mano2.attach(6);
  mano3.attach(7);
  pinza.attach(8);
  Serial.begin(9600); //Iniciamos puerto serie
  // Mandamos a HOME a todos los servos
  cuerpo.write(home_cero);
  hombro.write(home_hombro);
  brazo.write(home_brazo);
  mano1.write(home_mano1);
  mano2.write(home_cero);
  mano3.write(home_cero);
  pinza.write(home_cero);
}

void loop() {
  // En cada ciclo verificamos si hay un mensaje por el puerto serie
  if (Serial.available() > 0)
   {
     msg = Serial.readStringUntil('\n'); //Leemos el serial
     //Cuerpo
     if (msg.startsWith("s1")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      cuerpo.write(pos); //Movemos el cuerpo
     }
     
     // Hombro
     if (msg.startsWith("s2")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      hombro.write(pos); //Movemos el hombro
     }

     // Brazo
     if (msg.startsWith("s3")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      brazo.write(pos); //Movemos el brazo
     }

     // Mano1 (Roll/Alabeo)
     if (msg.startsWith("s4")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      mano1.write(pos); //Movemos muñeca roll
     }

     // Mano2 (Pitch/Elevación)
     if (msg.startsWith("s5")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      mano2.write(pos); //Movemos el brazo
     }

     // Mano3 (Yaw/Cabeceo)
     if (msg.startsWith("s6")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      mano3.write(pos); //Movemos el brazo
     }

     // Pinza
     if (msg.startsWith("s7")) {
      String msg_aux = msg.substring(2, msg.length());
      pos = msg_aux.toInt();
      pinza.write(pos); //Movemos el servo
     }
   }
   delay(1);
}
