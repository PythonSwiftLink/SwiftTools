//
//  TextToSpeech.swift
//  untitled
//
//  Created by MusicMaker on 22/12/2022.
//

import Foundation
import AVFoundation

class TextToSpeech {
    
    let synth = AVSpeechSynthesizer()
    var voice: AVSpeechSynthesisVoice?
    
    init() {
        
    }
}

extension TextToSpeech: TextToSpeech_PyProtocol {
    func set_locale(locale: String) {
        self.voice = .init(language: locale)
    }
    
    func speak(message: String) {
        
        if self.voice == nil {
            set_locale(locale: "en-US")
        }
        
        let utterance = AVSpeechUtterance(string: message)
        utterance.voice = self.voice
        
        synth.speak(utterance)
    }
    
    
}
