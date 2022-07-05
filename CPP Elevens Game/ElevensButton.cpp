#include "button.h"
#include "ElevensButton.h"
#include "Elevens.h"

ElevensButton::ElevensButton(Image setCard, float setWidth, float setHeight, float setX, float setY, float setScale) 
    :
    card(setCard),
    cardTexture(LoadTextureFromImage(card)),
    scale(setScale)
{
    trueButton = false;
    //scale = setScale;
    //card = setCard;
    width = setWidth*scale;
    height = setHeight*scale;
    x = setX;
    y = setY;

    //cardTexture = LoadTextureFromImage(card);

    UnloadImage(card);
}

void ElevensButton::draw() {
    if (trueButton == false) {
        Elevens *Game = Game->getInstance();
        if (Game->selected.size() >= 1) {
            for (auto btn : Game->selected) {
                if (btn == this) {
                    DrawRectangle(x-5, y-5, width+10, height+10, YELLOW);
                }
            }
        }
        DrawTextureEx(cardTexture, {x, y}, 0, scale, WHITE);
    }
    else {
        Button::draw();
    }
}

ElevensButton::~ElevensButton() {
    UnloadTexture(cardTexture);
}