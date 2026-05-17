#include <IRremote.h>
int RECV_PIN = 10;

IRrecv irrecv(RECV_PIN);

decode_results results;
unsigned long int value = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // In case the interrupt driver crashes on setup, give a clue
  // to the user what's going on.
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("Enabled IRin");

}

void loop() {
  // put your main code here, to run repeatedly:
  if (irrecv.decode(&results)) {
    value = results.value;
    Serial.println(value, HEX);
    irrecv.resume(); // Receive the next value
    delay(200);
  }
}
