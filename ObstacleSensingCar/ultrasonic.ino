#include <Ultrasonic.h> 

Ultrasonic sensor(9,8,30000); // (Trig핀, Echo핀, 최대거리 단위는 us) 즉 30000us = 약 5미터

int distance = 0; //거리를 저장할 변수를 선언합니다.

void setup() {
  
Serial.begin(9600); //시리얼포트를 초기화합니다.
  
}

void loop() {
  
  distance = sensor.Ranging(CM);  // 거리를 측정하고 distance 변수에 저장합니다.
  Serial.print("Distance "); // "Distance "를 시리얼모니터에 출력합니다.
  Serial.print(distance); // distance 변수에 저장된 값을 출력합니다.
  Serial.println(" cm"); // 센티미터 단위를 출력합니다.
  delay (2000); // 2초간 딜레이를 한 후에 다시 반복합니다.
  
}
