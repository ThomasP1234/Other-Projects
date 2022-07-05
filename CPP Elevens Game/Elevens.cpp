#include "Elevens.h"
#include <iostream>

Elevens::Elevens() {
    btnEventHandler = new ElevensButtonEventHandler(this);
    ((ElevensButtonEventHandler*)btnEventHandler)->registerButtonManager(&elevensBtnMgr);

    btnEventHandlerDraw = new ElevensButtonEventHandlerDrawCard(this);
    ((ElevensButtonEventHandlerDrawCard*)btnEventHandler)->registerButtonManager(&elevensBtnMgr);
    gameLogic();
    window();
}

void Elevens::gameLogic() {
    {
        std::vector<std::string> suits = {"club", "diamond", "heart", "spade"};
        std::vector<std::string> values = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
        for (std::string suit : suits) {
            for (std::string value : values) {
                deck.push_back(suit+value);
            }
        }

        std::shuffle(deck.begin(), deck.end(), std::random_device());

        // std::cout << "deck = { ";
        // for (std::string n : deck) {
        //     std::cout << n << ", ";
        // }
        // std::cout << "}; \n";
    }
}

void eraseSubStr(std::string & mainStr, const std::string & toErase)
{
    // Search for the substring in string
    size_t pos = mainStr.find(toErase);
    if (pos != std::string::npos)
    {
        // If found then erase it from string
        mainStr.erase(pos, toErase.length());
    }
}

void Elevens::newButton(int newRow, int newColumn) {
    bool swapped = false;
    int oldRow;
    int oldColumn;
    if (newRow >= 0 && newColumn >= 0) {
        oldRow = row;
        oldColumn = column;
        row = newRow;
        column = newColumn;
        swapped = true;
    }
    if (row < 3 && column < 3) {
        if (!deck.empty()) {
            std::string file = "./resources/deck/" + deck.front() + ".png";

            // deck.push_back(deck[0]);
            deck.erase(deck.begin());

            // std::cout << file << std::endl;

            Image img = LoadImage(file.c_str());

            ElevensButton *btn = new ElevensButton(img, 124, 180, float(row*150+50), float(column*206+60), 1);
            
            eraseSubStr(file, "./resources/deck/club");
            eraseSubStr(file, "./resources/deck/spade");
            eraseSubStr(file, "./resources/deck/diamond");
            eraseSubStr(file, "./resources/deck/heart");
            eraseSubStr(file, ".png");

            btn->cardVal = file;

            // file.erase(std::find(std::begin(file), std::end(file), "./resources/deck/club"));
            // file.erase(std::find(std::begin(file), std::end(file), "./resources/deck/spade"));
            // file.erase(std::find(std::begin(file), std::end(file), "./resources/deck/diamond"));
            // file.erase(std::find(std::begin(file), std::end(file), "./resources/deck/heart"));
            // file.erase(std::find(std::begin(file), std::end(file), ".png"));
            std::cout << file << std::endl;

            btn->registerCallback(btnEventHandler);

            elevensBtnMgr.add(btn);


            if (swapped == true) {
                row = oldRow;
                column = oldColumn;  
            }
            else {
                row++;

                if (row > 2) {
                    row = 0;
                    column++;
                }
            }
        }
    }
}

void Elevens::window() {
    InitWindow(screenWidth, screenHeight, "Elevens");
    SetTargetFPS(60);
    

    newButton();
    Button *drawCard = new Button(424, 40, 50, 669);
    drawCard->registerCallback(btnEventHandlerDraw);
    drawCard->text("Deal a Card", 40, 2, GetFontDefault(), BLACK);
    elevensBtnMgr.add(drawCard);

    // Button *newbtn = new Button(20, 20, 200, 200);
    // elevensBtnMgr.add(reinterpret_cast<ElevensButton*>(newbtn));
}

void Elevens::gameLoop() {
    while (!WindowShouldClose()){        
        update();
        draw();
    }
}

void Elevens::update() {
    elevensBtnMgr.update();

    if (selected.size() >= 2) {
        std::cout << "size greater than 2" << std::endl;
        if (selected.size() == 2) {
            std::cout << "size equal to 2" << std::endl;
            int total = 0;
            for (auto btn : selected) {
                if (btn->cardVal == "Ace") {
                    std::cout << "Ace - 1" << std::endl;
                    total += 1;
                }
                else if (btn->cardVal == "2") {
                    std::cout << "2" << std::endl;
                    total += 2;
                }
                else if (btn->cardVal == "3") {
                    std::cout << "3" << std::endl;
                    total += 3;
                }
                else if (btn->cardVal == "4") {
                    std::cout << "4" << std::endl;
                    total += 4;
                }
                else if (btn->cardVal == "5") {
                    std::cout << "5" << std::endl;
                    total += 5;
                }
                else if (btn->cardVal == "6") {
                    std::cout << "6" << std::endl;
                    total += 6;
                }
                else if (btn->cardVal == "7") {
                    std::cout << "7" << std::endl;
                    total += 7;
                }
                else if (btn->cardVal == "8") {
                    std::cout << "8" << std::endl;
                    total += 8;
                }
                else if (btn->cardVal == "9") {
                    std::cout << "9" << std::endl;
                    total += 9;
                }
                else if (btn->cardVal == "10") {
                    std::cout << "10" << std::endl;
                    total += 10;
                }
                else if (btn->cardVal == "Jack") {
                    std::cout << "Jack - 11" << std::endl;
                    total += 11;
                }
                else if (btn->cardVal == "Queen") {
                    std::cout << "Queen - 12" << std::endl;
                    total += 12;
                }
                else if (btn->cardVal == "King") {
                    std::cout << "King - 13" << std::endl;
                    total += 13;
                }
            }
            std::cout << total << std::endl;
            if (total == 11) {
                for (auto btn : selected) {
                    newButton((btn->getPosition().x-50)/150, (btn->getPosition().y-60)/206);

                    elevensBtnMgr.remove(reinterpret_cast<ElevensButton*>(btn));
                    delete btn;
                }
                selected.clear();
            }
            else if (total > 22) {
                ;
            }
            else {
                selected.clear();
            }
        }
        else {
            std::cout << "size equal to 3" << std::endl;
            int total = 0;
            for (auto btn : selected) {
                if (btn->cardVal == "Jack") {
                    std::cout << "Jack - 11" << std::endl;
                    total += 11;
                }
                else if (btn->cardVal == "Queen") {
                    std::cout << "Queen - 12" << std::endl;
                    total += 12;
                }
                else if (btn->cardVal == "King") {
                    std::cout << "King - 14" << std::endl;
                    total += 13;
                }
            }
            std::cout << total << std::endl;
            if (total == 36) {
                for (auto btn : selected) {
                    newButton((btn->getPosition().x-50)/150, (btn->getPosition().y-60)/206);

                    elevensBtnMgr.remove(reinterpret_cast<ElevensButton*>(btn));
                    delete btn;
                }
            }
            selected.clear();
        }
    }
}

void Elevens::draw() {
    BeginDrawing();

        ClearBackground(backgroundColor);

        Vector2 pos;
        std::string text;

        text = "Elevens";
        pos = MeasureTextEx(GetFontDefault(), text.c_str(), 50.0, 2.0);
        DrawTextEx(GetFontDefault(), text.c_str(), {(screenWidth/2)-(pos.x/2), 10}, 50.0, 2.0, WHITE);

        elevensBtnMgr.draw();

        EndDrawing();
}

Elevens::~Elevens() {
    delete static_cast<ElevensButtonEventHandler*>(btnEventHandler);
    delete static_cast<ElevensButtonEventHandlerDrawCard*>(btnEventHandlerDraw);
    elevensBtnMgr.destroy();
    CloseWindow();
}