//
//  AudioRecorder.swift
//  my_project
//
//  Created by MusicMaker on 16/01/2023.
//

import Foundation
import AVFoundation


class Audio: NSObject, AVAudioRecorderDelegate {
    var recordingSession: AVAudioSession!
    var audioRecorder: AVAudioRecorder!
    
    var audioPlayer: AVAudioPlayer!
    
    var _file_path: URL?
    var file_path: String {
        get { _file_path?.path ?? "" }
        set {
            _file_path = .init(fileURLWithPath: newValue)
        }
    }
    
    override init() {
        super.init()
        recordingSession = AVAudioSession.sharedInstance()
        
        do {
            try recordingSession.setCategory(.playAndRecord, mode: .default)
            try recordingSession.setActive(true)
            recordingSession.requestRecordPermission() { [unowned self] allowed in
                DispatchQueue.main.async {
                    if allowed {
                        // self.loadRecordingUI()
                        
                    } else {
                        // failed to record!
                    }
                }
            }
        } catch {
            // failed to record!
        }
    }
    
    func startRecording() {
        guard let audioFilename = _file_path else { return }
        print("recording to: \(audioFilename)")
        let settings = [
            AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
            AVSampleRateKey: 44100,
            AVNumberOfChannelsKey: 2,
            AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
        ]
        
        do {
            audioRecorder = try AVAudioRecorder(url: audioFilename, settings: settings)
            audioRecorder.delegate = self
            audioRecorder.prepareToRecord()
            audioRecorder.record()
            print(audioRecorder.isRecording)
            // send to kivy instead ?
            //recordButton.setTitle("Tap to Stop", for: .normal)
        } catch {
            print(error.localizedDescription)
            finishRecording(success: false)
        }
    }
    
    func getDocumentsDirectory() -> URL {
        let paths = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)
        return paths[0]
    }
    
    func finishRecording(success: Bool) {
        guard audioRecorder != nil else { return }
        audioRecorder.stop()
        audioRecorder = nil
        
        if success {
            
        } else {
            
            // recording failed :(
        }
    }
    
    func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) {
        if !flag {
            finishRecording(success: false)
        }
    }
}


extension Audio: Audio_PyProtocol {
    func start() {
        startRecording()
    }
    
    func stop() {
        if audioRecorder != nil {
            finishRecording(success: true)
            return
        }
        if audioPlayer != nil {
            audioPlayer.stop()
            audioPlayer = nil
            return
        }
        
    }
    
    func play() {
        let url = URL(fileURLWithPath: file_path)
        guard
            audioRecorder == nil,
            
            let player: AVAudioPlayer = try? .init(contentsOf: url)
        else {
            return
        }
        if !player.isPlaying {
            player.prepareToPlay()
            player.play()
        }
        
        audioPlayer = player
        
    }
    
    
}
