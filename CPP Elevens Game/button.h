#pragma once

#include "raylib.h"
#include <string>
#include "ButtonEventHandler.h"

class Button {
    protected:
        float width = 10.0;
        float height = 10.0;
        float x = 10.0; // Top Left x
        float y = 10.0; // Top Left y
        bool trueButton = true;

    private:

        int state = 0; // 0 = Normal, 1 = Mouse Hovered, 2 = Pressed
        bool btnActive = true; // false = button cannot be pressed, true = button can be pressed
        
        Color buttonColor; // Current color
        Color buttonColorN = GREEN; // Color when normal
        Color buttonColorMH = BLUE; // Color when mouse is hovered
        Color buttonColorP = RED; // Color when pressed
        Color buttonColorD = GRAY; // Color when disabled

        Rectangle sourceRec;
        Rectangle btnBounds;
        Vector2 mousePoint;

        std::string buttonText = "";
        float textFontSize = 10.0;
        float textFontSpacing = 2.0;
        Font textFont = GetFontDefault();
        Color textColor = BLACK;
        Vector2 textMeasure1;

        ButtonEventHandler *buttonEventHandler = NULL;

    public:
        Button();
        Button(const Button &btn);
        Button(float setWidth, float setHeight, float setX, float setY);
        virtual ~Button() {}
        void registerCallback(ButtonEventHandler *btnEventHandler);

        void geometry(float setWidth, float setHeight, float setX, float setY);

        void color(Color setColorNormal, Color setColorMouseHover, Color setColorPressed, Color setColorDisabled) {
            buttonColorN = setColorNormal;
            buttonColorMH = setColorMouseHover;
            buttonColorP = setColorPressed;
            buttonColorD = setColorDisabled;
        }

        void text(std::string setText, float setFontSize, float setFontSpacing, Font setFont, Color setTextColor) {
            buttonText = setText;
            textFontSize = setFontSize;
            textFontSpacing = setFontSpacing;
            textFont = setFont;
            textColor = setTextColor;
            textMeasure1 = MeasureTextEx(textFont, buttonText.c_str(), textFontSize, textFontSpacing);
        }

        void active(bool setActive) {
            btnActive = setActive;
        }

        bool getActive() {
            return btnActive;
        }

        std::string getText() {
            return buttonText;
        }

        Color getColor() {
            return buttonColor;
        }

        Vector2 getPosition() {
            return (Vector2){x, y};
        }

        Vector2 getSize() {
            return (Vector2){width, height};
        }

        bool update();

        virtual void draw();
};