//
//  FileChooser.swift
//  untitled
//
//  Created by MusicMaker on 22/12/2022.
//

import Foundation
import UIKit

func some_module_func() -> PyPointer {
    print("running some_module_func")
    return "some_string"
}

class FileChooser: NSObject {
    var picker: UIImagePickerController?
    
    var py_callback: FileChooserPyCallback?
    
    required override init() {
        
    }
}

extension FileChooser: FileChooser_PyProtocol {


    func open() {
        print(self,"open")
        picker = .init()
        picker?.sourceType = .photoLibrary
        picker?.delegate = self
        if let vc = UIApplication.shared.windows.first?.rootViewController, let picker = picker {
            vc.present(picker, animated: true)
        }
    }
    
    func __getitem__(idx: Int) -> PyPointer {
        print(self,"__getitem__", idx)
        return .init("\(self)")
    }
    
    func __setitem__(idx: Int, newValue: PythonPointer) -> Bool {
        print(self,"__setitem__", idx)
        return true
    }
    
    
}

extension FileChooser: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        py_callback?.didFinishPicking(results: [])
    }
    
}


