//
//  Brightness.swift
//  untitled
//
//  Created by MusicMaker on 22/12/2022.
//

import Foundation
import UIKit

class Brightness {
    
}

extension Brightness: Brightness_PyProtocol {
    
    var level: Double {
        get { UIScreen.main.brightness }
        set { UIScreen.main.brightness = newValue }
    }
    
    func current_level() -> Double {
        UIScreen.main.brightness
    }
    
    func set_level(level: Double) {
        UIScreen.main.brightness = level
    }
    
    
}
