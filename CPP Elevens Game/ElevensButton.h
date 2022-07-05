#pragma once

#include <raylib.h>

#include "button.h"

class Button;
class ElevensButton : public Button {
    private:
        Image card;
        Texture2D cardTexture;

        float scale = 1;
    public:
        std::string cardVal = "NONE";
        ElevensButton(Image setCard, float setWidth, float setHeight, float setX, float setY, float setScale);

        void draw();

        ~ElevensButton();
};
