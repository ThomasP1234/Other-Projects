#include "button.h"
#include "iostream"

Button::Button() {}

Button::Button(const Button &btn) { // Copy Constructor
    this->width = btn.width;    
    this->height = btn.height;
    this->x = btn.x;
    this->y = btn.y;

    this->state = btn.state;
    this->btnActive = btn.btnActive;

    this->buttonColorN = btn.buttonColorN;
    this->buttonColorMH = btn.buttonColorMH;
    this->buttonColorP = btn.buttonColorP;
    this->buttonColorD = btn.buttonColorD;

    this->buttonText = btn.buttonText;
    this->textFontSize = btn.textFontSize;
    this->textFontSpacing = btn.textFontSpacing;
    this->textFont = btn.textFont;
    this->textColor = btn.textColor;
    this->textMeasure1 = btn.textMeasure1;
}
Button::Button(float setWidth, float setHeight, float setX, float setY) { // Geometry Constructor
    width = setWidth;
    height = setHeight;
    x = setX;
    y = setY;
}

void Button::registerCallback(ButtonEventHandler *btnEventHandler) { // Callback register
    buttonEventHandler = btnEventHandler;
}

void Button::geometry(float setWidth, float setHeight, float setX, float setY) { // Geometry setter
    width = setWidth;
    height = setHeight;
    x = setX;
    y = setY;
}

bool Button::update() {
    // std::cout << "updating: " << x << ", " << y << std::endl;
    btnBounds = { x, y, width, height }; // Set the bounding/collision box of the button
    mousePoint = GetMousePosition();
    bool result = false;

    if (btnActive == true) { // If the button is not disabled
        if (CheckCollisionPointRec(mousePoint, btnBounds)) { // If the mouse if touching it
            if (IsMouseButtonDown(MOUSE_BUTTON_LEFT)) state = 2; // If the left mouse button is down (the button has been pressed)
            else state = 1; // Mouse hover
            if (buttonEventHandler) {
                if (IsMouseButtonReleased(MOUSE_BUTTON_LEFT)) {
                    result = true;
                    buttonEventHandler->invoke(this); // Callback on mouse button release
                }
            }
        }
        else state = 0; // Button is untouched

        if (state == 0) { // Set the right colour for the state it is in
            buttonColor = buttonColorN; // Normal
        }
        else if (state == 1) {
            buttonColor = buttonColorMH; // Mouse Hover
        }
        else if (state == 2) {
            buttonColor = buttonColorP; // Pressed
        }
    }
    else {
        buttonColor = buttonColorD; // Disabled/off
    }           

    sourceRec.y = state*height;
    
    return result;
}

void Button::draw() {
    DrawRectangleRec(btnBounds, buttonColor);

    DrawTextEx(textFont, buttonText.c_str(), (Vector2){(width/2.0f) - textMeasure1.x/2 + x, (height/2.0f) - textMeasure1.y/2 + y }, textFontSize, textFontSpacing, textColor);
}