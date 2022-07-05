#pragma once
#include <raylib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <random>

#include "ElevensButtonManager.h"
#include "ElevensButton.h"
#include "button.h"
#include "ElevensButtonEventHandler.h"
#include "ElevensButtonEventHandlerDrawCard.h"

class Elevens {
    private:
        static Elevens *instance;
        Elevens();

    public:
        static Elevens *getInstance() {
            if (!instance) {
                instance = new Elevens;
            }
            return instance;
        }

    public:
        const int screenWidth = 524; // Window geometry
        const int screenHeight = 727;
        Color backgroundColor = {48, 48, 48, 255}; // Grey Colour
        ElevensButtonManager elevensBtnMgr;
        ButtonEventHandler *btnEventHandler;
        ButtonEventHandler *btnEventHandlerDraw;
        std::vector<std::string> deck;
        std::vector<ElevensButton*> selected;

        int column = 0;
        int row = 0;

    public:
        void gameLogic();
        void window();

        void newButton(int newRow = -1, int newColumn = -1);

        void gameLoop();
        void draw();
        void update();

        ~Elevens();
};