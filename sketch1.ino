const int LED = 13; //This is creating a constant called LED that is of type integer corresponding to the pin 
// The led is connected to 

void setup() { //void is the return type of this function, as in it returns nothing
  // put your setup code here, to run once:
  // For arduino, the setup function allows you to set pin modes (output or input)
  // Allows to declare variables you need, just generally call setup functions beforehand 
  pinMode(LED,OUTPUT); //This defines our LED as an output pin 

}

void loop() {
  // put your main code here, to run repeatedly:
  // things that our program actually does
  digitalWrite(LED,HIGH); //Turning the LED by setting the output to HIGH
  delay(5000); //Wait one second
  digitalWrite(LED,LOW); //This is turning off the LED
  delay(1000); 
}

//10:20