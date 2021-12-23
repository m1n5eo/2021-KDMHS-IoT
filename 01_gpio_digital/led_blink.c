#include <wiringPi.h>
#define LED_PIN 4

int main (void) {
    //wiringPiSetup(); // WPi
    wiringPiSetupGpio(); // BCM
    pinMode (LED_PIN, OUTPUT);
    for (int i=0; i<5; i++) {
        digitalWrite (LED_PIN, HIGH); delay (700);      // HIGH=1
        digitalWrite (LED_PIN,  LOW); delay (300);      // LOW=0
    }
    return 0;
}
