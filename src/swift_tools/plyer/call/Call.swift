//
//  call.swift
//  untitled
//
//  Created by MusicMaker on 22/12/2022.
//

import Foundation
import UIKit

class Call: Call_PyProtocol {
    
    func makecall(tel: String) {
        let _url = "tel://\(tel)"
        if let url = URL(string: _url) {
            UIApplication.shared.open(url)
        }
    }
}
