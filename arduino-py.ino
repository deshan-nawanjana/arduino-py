// pins for display
#define LCD_PIN_RS 52 // RS
#define LCD_PIN_E0 50 // E
#define LCD_PIN_D4 48 // D4
#define LCD_PIN_D5 46 // D5
#define LCD_PIN_D6 44 // D6
#define LCD_PIN_D7 42 // D7

// include module
#include <LiquidCrystal.h>

// create display
LiquidCrystal lcd(
    LCD_PIN_RS,
    LCD_PIN_E0,
    LCD_PIN_D4,
    LCD_PIN_D5,
    LCD_PIN_D6,
    LCD_PIN_D7
);

void setup() {
    // start display
    lcd.begin(16, 2);
    // set write cursor to 0, 0
    lcd.setCursor(0,0);
    // print first text
    lcd.print("Hello World!");
    // start serial communication
    Serial.begin(9600);
    Serial.println("Input text to display !");
}

void loop() {
    String text;
    if(Serial.available() > 0) {
        // set write cursor to 0, 0
        lcd.setCursor(0,0);
        // read line
        text = Serial.readString();
        // pint received text
        lcd.print(text);
        // callback print
        Serial.print("PRINTED : ");
        Serial.println(text);
    }
}