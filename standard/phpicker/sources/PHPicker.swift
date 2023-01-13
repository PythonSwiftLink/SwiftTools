//
//  PHPicker.swift
//  test
//
//  Created by MusicMaker on 06/01/2023.
//

import Foundation
import PhotosUI
import UniformTypeIdentifiers




extension NSItemProvider: PyConvertible {
    public var pyObject: PythonObject {
        .init(getter: pyPointer)
    }
    
    public var pyPointer: PyPointer {
        create_pyNSItemProvider(self)
    }
    
    
}

class PHPickerResults: PHPickerResults_PyProtocol {
    func __getitem__(idx: Int) -> PyPointer {
        guard idx < results.count else { return nil }
        return results[idx].itemProvider.pyPointer
    }
    
    
    var results: [PHPickerResult]
    
    internal init(results: [PHPickerResult]) {
        self.results = results
        
    }
}

class PHPicker {
    var view: PHPickerViewController?
    var py_callback: PHPickerPyCallback?
    
    init() {

    }
    
    func newView(limit: Int) {
        var config = PHPickerConfiguration()
        config.filter = .images
        config.selectionLimit = limit
        config.preferredAssetRepresentationMode = .current
        view = .init(configuration: config)
        view?.delegate = self
    }
}

extension PHPicker: PHPickerViewControllerDelegate {
    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        py_callback?.picker_didFinishPicking(
            results: create_pyPHPickerResults(
                .init(results: results)
            )
        )
    }
    
}

extension PHPicker: PHPicker_PyProtocol {
    
    func open(limit: Int) {
        newView(limit: limit)
        guard let view = view, let vc = get_viewcontroller() else { return }
        vc.present(view, animated: true)
    }
    func dismiss() {
        guard let view = view else { return }
        view.dismiss(animated: true)
    }
    
}
