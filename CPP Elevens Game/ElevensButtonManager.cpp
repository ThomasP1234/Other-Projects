#include <iostream>
#include "button.h"
#include "ElevensButtonManager.h"
//#include "ElevensButton.h"

ElevensButtonManager::ElevensButtonManager() {
    buttons.reserve(16);
}

void ElevensButtonManager::add(Button *btn) {
    buttons.push_back(btn); // Add buttons to a list
}

void ElevensButtonManager::remove(Button *btn) {
    // std::list<ElevensButton *>::iterator it = buttons.begin();
    // for (ElevensButton *ibtn : buttons) {
    //     if (btn == ibtn) {
    //         buttons.erase(it);
    //     }
    //     advance(it, 1);
    // }
    // std::vector<ElevensButton *>::iterator it = buttons.begin();
    auto it = buttons.begin();
    for (Button *currentBtn : buttons) {
        if (btn == currentBtn) {
            buttons.erase(it);
            return;
        }
        std::advance(it, 1);
    }
}

void ElevensButtonManager::update() {
    // std::cout << buttons.size() << std::endl;
    for (Button *btn : buttons) {
        //reinterpret_cast<ElevensButton*>(btn)->update(); // Update all buttons
        
        if (btn->update()) { // Update all buttons unless buttons collection is updated
            return;
        } 
    }
}

void ElevensButtonManager::draw() {
    for (Button *btn : buttons) {
        //ElevensButton* b = static_cast<ElevensButton*>(btn); // Draw all buttons           
        //ElevensButton* b = dynamic_cast<ElevensButton*>(btn); // Draw all buttons   
        btn->draw();
    }
}

void ElevensButtonManager::destroy() {
    for (Button *btn : buttons) {
        //delete dynamic_cast<ElevensButton*>(btn); // Delete all buttons
        //delete static_cast<ElevensButton*>(btn); // Delete all buttons
        delete btn;
    }
}

// std::vector<Button *> ElevensButtonManager::get() {
//     return buttons; // Get the list of all buttons
// }