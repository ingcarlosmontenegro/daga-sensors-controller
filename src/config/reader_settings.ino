#include<DHT.h>

// DHT11 temp-Humidity
#define DHTPIN 3
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);


void setup()
{
  Serial.begin(9600); //serial port - 9600 bps
  dht.begin();
}

void loop()
{
  // MIKROE-1630 CO2 Sensor
  float gas_ac = analogRead(A0);
    
  //MQ-135 Gas Sensor
  float gas = analogRead(A1);

  //DHT11 - temp-humidity
  float humedity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // GUVA P1918
  float lightUV = analogRead(A2);
  
  //DFROBOT - Moisture
  float moisture = analogRead(A3);

  Serial.println("{\"measure_co2\":" + (String)gas_ac + ",\"gas\":" + (String)gas + ",\"humedity\":" + (String)humedity + ",\"temperature\":" + (String)temperature + ",\"light_uv\":" + (String)lightUV + ",\"moisture\":" + (String)moisture +"}");
  delay(1000);
}
