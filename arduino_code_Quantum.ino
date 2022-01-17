int x;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);

}

void loop() {

  digitalWrite(8, LOW);
  digitalWrite(9, LOW);

    while (!Serial.available());
  x = Serial.readString().toInt();


if (x==0)
{  
digitalWrite(8, HIGH);
}

else
{
digitalWrite(9, HIGH);  
}

delay(5000);

}
