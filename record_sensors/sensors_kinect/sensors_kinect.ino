#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define TCAADDR 0x70
 
Adafruit_BNO055 bno0 = Adafruit_BNO055(55);
Adafruit_BNO055 bno1 = Adafruit_BNO055(56);
Adafruit_BNO055 bno2 = Adafruit_BNO055(57);
Adafruit_BNO055 bno3 = Adafruit_BNO055(58);
Adafruit_BNO055 bno4 = Adafruit_BNO055(59);
Adafruit_BNO055 bno5 = Adafruit_BNO055(60);
Adafruit_BNO055 bno6 = Adafruit_BNO055(61);
Adafruit_BNO055 bno7 = Adafruit_BNO055(62);


int pin_kinect = 2;
int pin_LEDs = 4;

int LEDcounter = 0;

volatile bool state = false;
volatile bool test = false;

void sensor_init(uint8_t i, Adafruit_BNO055 bno){
  tcaselect(i);
    if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  } 
  else{
    String msg = "#" + String(i)+" is all ok!";
    Serial.println(msg);
  }
  delay(100);
  bno.setExtCrystalUse(true);
  
}


void printIMU(imu::Vector<3> acc) {
  /* Display the floating point data */
  Serial.print(acc.x());
  Serial.print(",");
  Serial.print(acc.y());
  Serial.print(",");
  Serial.print(acc.z());
  Serial.print(",");
  //Serial.println("");
}

void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission(); 
}
 
void setup(void)
{
  Serial.begin(2000000);
  Wire.begin();
  //Serial.println("Orientation Sensor Test"); Serial.println("");
  delay(1000);
  pinMode(pin_kinect, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pin_kinect), readAudio, RISING);
  pinMode(pin_LEDs, OUTPUT);
  
// Initialise the sensors

  tcaselect(0);
  bno0.begin();
  tcaselect(1);
  bno1.begin();
  tcaselect(2);
  bno2.begin();   
  tcaselect(3);
  bno3.begin(); 
  tcaselect(4);
  bno4.begin();
  tcaselect(5);
  bno5.begin(); 
  tcaselect(6);
  bno6.begin();
  tcaselect(7);
  bno6.begin();
  

  tcaselect(0);
  sensor_init(0,bno0);
  
  tcaselect(1);
  sensor_init(1,bno1);
  
  tcaselect(2);
  sensor_init(2,bno2);
  
  tcaselect(3);
  sensor_init(3,bno3);
  
  tcaselect(4);
  sensor_init(4,bno4);
  
  tcaselect(5);
  sensor_init(5,bno5);
  
  tcaselect(6);
  sensor_init(6,bno6);
  
  tcaselect(7);
  sensor_init(7,bno7);

}
 
void loop(void)
{
  /* Get a new sensor event */
  sensors_event_t event; 
  
  tcaselect(0);   // select port 1
  imu::Vector<3> acc0 = bno0.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  
  tcaselect(1);   // select port 1
  imu::Vector<3> acc1 = bno1.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  
  tcaselect(2);   // select port 1
  imu::Vector<3> acc2 = bno2.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  
  tcaselect(3);   // select port 1
  imu::Vector<3> acc3 = bno3.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  tcaselect(4);   // select port 1
  imu::Vector<3> acc4 = bno4.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  tcaselect(5);   // select port 1
  imu::Vector<3> acc5 = bno5.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  tcaselect(6);   // select port 1
  imu::Vector<3> acc6 = bno6.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  
  tcaselect(7);   // select port 1
  imu::Vector<3> acc7 = bno7.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  // Print sensor values if there is a clock tick
  if(state){
    printIMU(acc0);
    printIMU(acc1);
    printIMU(acc2);
    printIMU(acc3);
    printIMU(acc4);
    printIMU(acc5);
    printIMU(acc6);
    printIMU(acc7);
    Serial.println("");
    state = 0;
  }

  // LED blinking
  if(LEDcounter == 1000){
    digitalWrite(pin_LEDs, HIGH);
    LEDcounter = 0;
  }
   if(LEDcounter == 5){
    digitalWrite(pin_LEDs, LOW);
  }

  LEDcounter++;

}

void readAudio(){
  state = 1;
}
